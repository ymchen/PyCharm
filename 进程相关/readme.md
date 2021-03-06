
https://zhuanlan.zhihu.com/p/68828849
做个简单的比喻：进程=火车，线程=车厢线程在进程下行进（单纯的车厢无法运行）
一个进程可以包含多个线程（一辆火车可以有多个车厢）
不同进程间数据很难共享（一辆火车上的乘客很难换到另外一辆火车，比如站点换乘）
同一进程下不同线程间数据很易共享（A车厢换到B车厢很容易）
进程要比线程消耗更多的计算机资源（采用多列火车相比多个车厢更耗资源）
进程间不会相互影响，一个线程挂掉将导致整个进程挂掉（一列火车不会影响到另外一列火车，但是如果一列火车上中间的一节车厢着火了，将影响到所有车厢）
进程可以拓展到多机，进程最多适合多核（不同火车可以开在多个轨道上，同一火车的车厢不能在行进的不同的轨道上）
进程使用的内存地址可以上锁，即一个线程使用某些共享内存时，其他线程必须等它结束，才能使用这一块内存。（比如火车上的洗手间）－"互斥锁"
进程使用的内存地址可以限定使用量（比如火车上的餐厅，最多只允许多少人进入，如果满了需要在门口等，等有人出来了才能进去）－“信号量”


单个CPU在任一时刻只能执行单个线程，只有多核CPU还能真正做到多个线程同时运行
一个进程包含多个线程，这些线程可以分布在多个CPU上
多核CPU同时运行的线程可以属于单个进程或不同进程
所以，在大多数编程语言中因为切换消耗的资源更少，多线程比多进程效率更高
坏消息，Python是个特例！

GIL锁
python始于1991年，创立初期对运算的要求不高，为了解决多线程共享内存的数据安全问题，引入了GIL锁，全称为Global Interpreter Lock，也就是全局解释器锁。

GIL规定，在一个进程中每次只能有一个线程在运行。这个GIL锁相当于是线程运行的资格证，某个线程想要运行，首先要获得GIL锁，然后遇到IO或者超时的时候释放GIL锁，给其余的线程去竞争，竞争成功的线程获得GIL锁得到下一次运行的机会。

正是因为有GIL的存在，python的多线程其实是假的，所以才有人说python的多线程非常鸡肋。但是虽然每个进程有一个GIL锁，进程和进程之前还是不受影响的。

GIL是个历史遗留问题，过去的版本迭代都是以GIL为基础来的，想要去除GIL还真不是一件容易的事，所以我们要做好和GIL长期面对的准备。

多进程 vs 多线程
那么是不是意味着python中就只能使用多进程去提高效率，多线程就要被淘汰了呢？

那也不是的。

这里分两种情况来讨论，CPU密集型操作和IO密集型操作。针对前者，大多数时间花在CPU运算上，所以希望CPU利用的越充分越好，这时候使用多进程是合适的，同时运行的进程数和CPU的核数相同；针对后者，大多数时间花在IO交互的等待上，此时一个CPU和多个CPU是没有太大差别的，反而是线程切换比进程切换要轻量得多，这时候使用多线程是合适的。

所以有了结论：

CPU密集型操作使用多进程比较合适，例如海量运算
IO密集型操作使用多线程比较合适，例如爬虫，文件处理，批量ssh操作服务器等等


进程间通讯
前面说到进程间是相互独立的，不共享内存空间，所以在一个进程中声明的变量在另一个进程中是看不到的。这时候就要借助一些工具来在两个进程间进行数据传输了，其中最常见的就是队列了。

队列（queue）在生产消费者模型中很常见，生产者进程在队列一端写入，消费者进程在队列另一端读取。

首先创建两个函数，分别扮演生产者和消费者
