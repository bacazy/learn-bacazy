# 计算机网络-数据链路层

数据链路层的功能是为网络层提供服务。最主要的服务是将数据从源机器的网络层传输到目标机器的网络层。数据链路层提供的服务可以分为以下3类：
1. 无确认的无连接服务:源机器向目标机器发送独立的帧，目标机器并不对这些帧进行确认。事先不建立逻辑连接，时候也不用释放逻辑连接。可能出现丢帧现象，但不进行检测。
1. 有确认的无连接服务：仍任没有使用逻辑连接，但是发送每一帧都需要进行确认。
1. 有确认的面向连接服务：传输过程可以分成三个阶段，第一个阶段，建立连接，双方初始化各种变量和计数器，这些变量和计数器记录了哪些帧已经接收到了，那些还没有，第二阶段，一个或者多个数据帧被发送出去。第三个阶段，连接被释放，所有的变量、缓冲区，以及其他用于维护该链接的资源也随之被释放。


## 错误检测和纠正
 
