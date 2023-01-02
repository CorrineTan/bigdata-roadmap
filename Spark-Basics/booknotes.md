## Spark技术内幕 = 内核架构设计与实现原理

Tez是hortonworks为了对抗spark里的DAG由Hortonworks研发出来的。

大数据4v问题：volume，velocity，variety，value。

Spark内核：Spark SQL, Spark Streaming, MLlib, GraphX

#### 第一章 Spark简介

大多数现有集群计算系统的流程 - 非循环数据流：稳定的物理存储（分布式文件系统）中加载记录 -> 传入一组确定性操作构成的DAG（Directed Acyclic Graph）-> 写回稳定存储。

但是有些情景需要循环数据流：<br>
ex1: 机器学习和图应用的迭代算法<br>
ex2: 交互式数据挖掘工具（用户反复查询一个数据子集）

由此spark实现RDD（resilient destirubted dataset）- 弹性分布式数据集，是一种分布式的内存抽象。将工作集缓存在内存中，后续查询能够重用数据集，提升了查询速度。

RDD高度受限 - 只读记录分区的集合。只能允许执行确定的转换操作（map join groupBy）。对比：<br>
分布式共享内存系统 如果丢失分区：检查点 回滚机制
RDD 如果丢失分区： Lineage重建丢失的分区

Spark架构基本概念：<br>
Driver：用户编写的数据处理逻辑，其中包含用户创建的sparkcontext。<br>
SparkContext： 用户逻辑与Spark集群的交互接口。与Cluster Manager交互以获取资源。<br>
Cluster Manager：负责集群的资源管理和调度。支持standalone，apache mesos和hadoop的yarn。<br>



Spark submit流程：<br>
1. 


#### 第二章 Spark环境搭建


#### 第三章 Spark RDD


#### 第四章 Spark Scheduler模块


#### 第五章 Spark Deploy模块


#### 第六章 Spark Executor模块


#### 第七章 Spark Shuffle模块


#### 第八章 Spark Storage模块