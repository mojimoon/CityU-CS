# CS2115 Extra Note

## I/O 模式

I/O 模块（I/O module）：

- 连接总线和 I/O 设备
- 向各种 I/O 设备提供通用的接口，使得 CPU 可以通过统一的方式访问各种 I/O 设备
- 在中断 I/O 模式下，I/O 模块会向 CPU 发出中断信号

DMA 模块（DMA controller）：

- 连接总线、I/O 模块和内存
- 有独立的运算单元，用于执行内存和 I/O 设备之间的数据传输
- 代理 CPU 和 I/O 模块的通信，CPU 只需向 DMA 模块发出读写命令，DMA 模块会代替 CPU 和 I/O 模块通信，将数据传送到内存
- 会向 CPU 发出中断信号

### 程序控制 I/O（Programmed I/O）

- 程序周期性发出读指令，CPU 向 I/O 模块发出读命令（CPU→I/O）
- I/O 模块检查 I/O 设备状态，并发送状态信号给 CPU（I/O→CPU）
- 如果未 ready，CPU 会等待，直到 ready
- 如果 ready，I/O 模块将数据从设备 buffer 传送到 CPU（I/O→CPU）
- CPU 将数据存入内存（CPU→Memory）
- 如果数据长度大于 buffer，I/O 模块会重复上述过程，直到所有数据都传送完毕

![](https://img-blog.csdnimg.cn/b2f332ee9e2b4c4cb8539f0442b823dc.png)

优点：
- 实现简单

缺点：
- CPU 和 I/O 串行工作，CPU 等待 I/O 完成，浪费 CPU 时间

### 中断 I/O（Interrupt-Driven I/O）

- 进程需要读取设备时，CPU 向 I/O 模块发出读命令（CPU→I/O）
- CPU 可以继续执行其他指令
- I/O 模块检查 I/O 设备状态，但不发送状态信号给 CPU，直到设备 ready
- I/O 模块将数据从设备 buffer 传送到 CPU（I/O→CPU）
- I/O 模块向 CPU 发出中断信号（I/O→CPU）
- CPU 收到中断信号后，暂停当前进程，转而执行中断处理程序（Interrupt Service Routine，ISR）
- ISR 可执行各种工作，如将数据存入内存（CPU→Memory）
- 如果数据长度大于 buffer，I/O 模块会重复上述过程，直到所有数据都传送完毕

优点：
- 效率比程序控制 I/O 明显提高，CPU 和 I/O 可以并行工作，CPU 利用率提高

缺点：
- 频繁的中断会降低 CPU 效率

### 直接存储器访问（Direct Memory Access，DMA）

- CPU 向 DMA 模块发出读命令（CPU→DMA），其中信息除了外部 I/O 设备的地址外，还包括读入数据量、欲存入内存的地址等
- CPU 可以继续执行其他指令
- DMA 完全代理在中断 I/O 中 CPU 的工作，包括和 I/O 模块的通信、保存数据到指定内存地址等
- DMA 向 I/O 模块发出读命令（DMA→I/O）
- I/O 模块检查设备状态，然后将数据以块的形式传送到 DMA（I/O→DMA）
- DMA 将数据存入内存（DMA→Memory）
- DMA 向 CPU 发出中断信号（DMA→CPU）

优点：
- 由于数据以块的形式传送，不再受到 buffer 大小的限制，中断次数大大减少，CPU 利用率进一步提高
- 设备和内存之间的 I/O 不再途经 CPU

缺点：
- 每次传输的数据块必须是连续的
