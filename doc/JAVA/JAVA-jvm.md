# JAVA虚拟机
## VM的生命周期

典型的从调用java命令行的虚拟机启动需要经过几个典型的步骤：
1. 解析命令行选项，一些命令行选项被启动程序本身使用，例如 -client或-server用于确定和加载适当的VM库，而另一些则使用JavaVMInitArgs传递给VM 。
2. 堆大小和编译器类型（客户端或服务器），如果这些选项没有明确指定在命令行上。
3. 建立环境变量，如LD_LIBRARY_PATH和CLASSPATH。
4. 如果未在命令行中指定java Main-Class，则它会从JAR的清单中获取Main-Class名称。
5. 在新创建的线程（非原始线程）中使用JNI_CreateJavaVM创建VM 。注意：在原生线程中创建虚拟机大大降低了定制虚拟机的能力，例如Windows上的堆栈大小以及许多其他限制
6. 一旦VM被创建和初始化，Main-Class被加载，启动程序从Main-Class获取主要方法的属性。
7. 然后使用CallStaticVoidMethod在VM中使用命令行中的编组参数调用java main方法 。
8. 一旦java main方法完成，检查并清除任何可能发生的异常并返回退出状态非常重要，通过调用ExceptionOccurred清除 异常，如果成功，则返回值为0否则为其他值，这个值被传回给调用进程。
9. 主线程使用DetachCurrentThread进行分离，通过这样做，我们减少线程数量，因此可以安全地调用DestroyJavaVM，以确保线程不在vm中执行操作，并且在其堆栈中没有活动的java框架。

其中有两个比较重要的阶段——JNI_CreateJavaVM以及DestroyJavaVM

NI_CreateJavaVM
JNI调用方法执行如下：

1. 确保没有两个线程同时调用此方法，并且在同一进程中没有创建两个VM实例。注意到一旦到达初始化点，就不能在同一个进程空间创建一个虚拟机，即“不返回点”。这是因为虚拟机创建的静态数据结构目前无法重新初始化。
2. 检查以确保支持JNI版本，以及检查ostream是否初始化完成以用于loging记录。OS模块被初始化，例如随机数生成器，当前pid，高分辨率时间，内存页大小和其他保护页。
3. 传入的参数和属性被解析并保存起来以备后用。标准的java系统属性被初始化。
4. 操作系统模块进一步创建和初始化，基于解析的参数和属性，初始化为同步，堆栈，内存和安全点页面。此时，其他库如libzip，libhpi，libjava，libthread被加载，信号处理程序被初始化和设置，线程库被初始化。
5. 输出流记录器被初始化。任何代理程序库（hprof，jdi）都需要被初始化并启动。
6. 线程状态和线程本地存储（TLS），包含创建线程操作所需的几个指定数据，被初始化。
7. 全局数据初始化，如事件日志，OS同步原语，perfMemory（性能内存），chunkPool（内存分配器）。
8. 这时，我们可以创建线程。主线程的Java版本被创建并附加到当前的操作系统线程。然而这个线程不会被添加到已知的线程列表中。Java级同步已初始化并启用。
9. 其余的全局模块被初始化，例如 BootClassLoader，CodeCache， Interpreter，Compiler，JNI，SystemDictionary和Universe。注意到我们已经达到了我们的“不归路”，即。我们不能再在相同的进程地址空间中创建另一个虚拟机。
10. 主线程被添加到列表中，首先锁定 Thread_Lock。宇宙是一组必需的全球数据结构，已经过检查。执行所有VM关键功能的VMThread被创建。此时将发布相应的JVMTI事件以通知当前状态。
11. 下面的类是java.lang.String，java.lang.System，java.lang.Thread，java.lang.ThreadGroup，java.lang.reflect.Method，java.lang.ref.Finalizer，java.lang.Class和系统类的其余部分被加载和初始化。此时，虚拟机已初始化并可以运行，但尚未完全正常运行。
12. 信号处理程序线程启动，编译器被初始化，CompileBroker线程启动。启动其他帮助程序线程St​​atSampler和WatcherThreads，此时VM已完全正常运行，JNIEnv被填充并返回给调用方，并且VM已准备好为新的JNI请求提供服务。


DestroyJavaVM
这个方法可以从启动程序调用来销毁虚拟机，当发生非常严重的错误时，也可以由虚拟机自己调用。

虚拟机的销毁过程如下：

1. 等到最后一个执行的非守护线程时，注意到这个虚拟机仍然有效。
2. 调用java.lang.Shutdown.shutdown(), 会调用Java级关闭钩子
3. 调用before\_exit(),准备VM退出运行VM级关闭挂钩(它们通过JVM\_OnExit()注册），停止Profiler， StatSampler，Watcher和 GC 线程。将状态事件发布到JVMTI / PI，禁用JVMPI，并停止Signal线程。
4. 调用JavaThread :: exit（），释放JNI句柄块，删除堆栈保护页面，并从线程列表中删除此线程。从这个角度来说，我们不能执行更多的Java代码。
5. 停止虚拟机线程，它会将剩余的虚拟机置于安全点，并停止编译器线程。在安全的情况下，我们应该小心，不要使用任何可能被安全点阻挡的东西。
6. 禁用JNI / JVM / JVMPI的跟踪。
7. 为仍在运行本机代码的线程设置\_vm\_exited标志。
8. 删除这个线程。
9. 调用exit\_globals（），它将删除IO和PerfMemory 资源。
10. 返回给调用者。

运行时数据区：
1. pc，程序计数器。线程私有，指向将要执行的指令的地址。
1. 栈。线程私有，用于保存栈帧，存储局部变量和返回值。栈在内存中可以是固定大小，也可以是变长的，可以是连续的也可以是不连续的。栈空间不够时，会抛出StackOverflowError. 如果栈是动态分配的，那么则抛出OutOfMemoryError。
1. 堆。线程共享，所有类实例和数组的运行时数据区。同样，堆大小可以是固定分配也可以是动态分配，可连续，也可不连续。堆空间不够用时会抛出OutOfMemoryError.
1. 方法区。线程共享。
1. 运行时常量区。
1. 本地方法栈。
