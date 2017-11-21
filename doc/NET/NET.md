# 计算机网络

- [物理层](physical-layer.md)
- [数据链路层](data-link-layer.md)
- [网络层](network-layer.md)
- [传输层](transport-layer.md)
- [应用层](application-layer.md)
- [网络安全](security.md)

## OSI（Open Systems Interconnection）参考模型
OSI模型有7层，分层原则如下：
* 当需要一个不同抽象体时，应该创建一层
* 每一层都应该执行一个明确定义的功能
* 选择每一层功能时，应该考虑到定义国际化标准的协议
* 选择层边界的时候，应该使跨接口所需要的信息流尽可能的小
* 层数应该足够多，以保证不同的功能不会被混杂在同一层中，同时层数也不能太多，以免整个体系结构过于庞大

![](res/osi-model.png)

## TCP/IP参考模型
TCP/IP被专门设计用于网络互连的通信。
![](res/tcp-ip-model.png)

