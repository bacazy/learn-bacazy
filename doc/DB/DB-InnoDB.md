# InnoDB存储引擎
## 简介
### 体系结构
InnoDB的存储引擎是多线程架构，Oracle是多进程结构。默认的后台线程有IO线程、
mater线程，锁监控线程以及错误监控线程。IO线程默认有四个，分别是插入缓冲线程、
日志线程、读线程、写线程。

InnoDB存储引擎内存由三部分组成：缓冲池、重做日志缓冲池以及额外的内存池。缓冲
池是占用最大的部分，用来存放各种数据的缓存。缓冲池中缓存的数据页类型有：索引
页、数据页、undo页、插入缓冲、自适应哈希索引，锁信息、数据字典信息等。日志缓
冲将重做日志信息先放入这个缓冲区中，然后按照一定的频率刷新到重做日志文件。
在对一些数据结构本身分配内存时，需要从额外的内存池中申请，当该区域的内存不够
时，会从缓冲池中申请。

### 关键特性

- 插入缓冲。InnoDB的存储引擎对于非聚集索引的插入或更新操作，不是每一次直接
    插入索引页中，而是先判断插入的非聚集索引页是否在缓冲区中。如果在，则直接
    插入；如果不在，则先放入一个插入缓冲区中，然后再以一定的频率执行插入缓冲
    和非聚集索引页子节点的合并操作，这时就可以将多个插入合并到一个操作中，这
    就大大提高了对非聚集索引执行插入和修改操作的性能。插入缓冲的使用需要满足
    缩影的数据类型的是辅助索引，并且不是唯一的。
- 两次写。保证数据的可靠性。当数据库发生宕机时，可能数据库正在写一个页面，而
    这个页面只写了一部分，即发生了写失效。(TODO:再看看)
- 自适应哈希索引。

## 文件
数据库和InnoDB存储引擎表的各种文件包括：
* 参数文件
* 日志文件
* socket文件：当用Unix域套接字方式连接时需要的文件
* pid文件
* MySQL表结构文件
* 存储引擎文件

### 日志文件
日志文件包括错误日志、二进制文件、慢查询日志和查询日志。错误日志对MySQL的启动、
运行、关闭过程进行记录。
慢查询日志能为SQL语句的优化提供帮助。可以设置一个阈值，将运行时间超过该值的SQL语
句都记录下来

