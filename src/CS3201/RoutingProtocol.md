# Control Plane 路由协议

## Intra-AS Routing（自治系统内部路由）

### RIP（Routing Information Protocol）

- Distance Vector
- 每个节点记录到其他节点的距离（单位：跳数）
- 每隔 30 秒向邻居节点发送路由表，然后根据收到的路由表更新自己的路由表

### OSPF（Open Shortest Path First）

- Link State
- 每个节点记录到其他节点的代价，然后广播自己的链路状态
- 每个节点预先知道整个网络的拓扑结构，可以通过 Dijkstra 算法计算最短路径

## Inter-AS Routing（自治系统间路由）

### BGP（Border Gateway Protocol）

- Path Vector，最短路径用 `AS-PATH` 表示，包括路径上的所有 AS
- 通过 `NEXT-HOP` 字段指定 AS 内部的下一跳
- eBGP：自治系统间的 BGP，AS 边界处的路由器之间交换路由信息
- iBGP：自治系统内部的 BGP，AS 通过边界路由器向所有内部路由器广播路由信息

