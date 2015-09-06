##NeuroLines: A Subway Map Metaphor for Visualizing Nanoscale Neuronal Connectivity

![NeuroLines](img/NeuroLines.jpg)

这篇论文主要描述了利用2D地铁图的简洁可视化模型去可视化复杂的3D神经元连接结构。使神经学家在神经元重组的过程中，有可视化的工具来辅助分析，简化工作的流程。

本文主要总结论文的写作思路，至于论文的内容本身，可以参考浙江大学可视化分析小组的文章：[Neurolines:用地铁图隐喻可视化纳米级的神经连接信息](http://www.cad.zju.edu.cn/home/vagblog/?p=2590)


###1. Introduction
描绘连接组学领域的神经学家重构神经元的工作。而计算机辅助科学家来分析神经元的前人工作主要集中在可视化完全抽象的连接图（舍弃形态学和结构信息）和渲染原始电子显微镜图（复杂混乱的可视化图）。所以文章提出了一种新的可视化技术（a novel multi-scale visualization technique）来帮助神经学家更好的分析神经元结构和探索新的假设。

所以，论文的主要贡献有：
1. 将神经轴突结构抽象表示为没有视觉重叠的2D表示模型，同时保留拓扑结构和连接信息
2. multi-scale的可视化和导航模式，可以很好同时可视化数千个神经元，并通过zoom定位到某个具体组织探索并保留邻近轴突的关系
3. 开发NeuroLines应用，并成为ConectomeExplorer的一个插件
4. 通过两个case studies演示了NeuroLines的可用性

###2. Related Work
1. 连接组学
2. 多层次导航（Multi-scale Navigation）

###3. 生物学背景
1. 神经组织学术语
2. 神经组织学工作流 （知道神经学家怎样工作，才能更好的设计出能够真正帮助他们的工具）

###4.NeuroLines Design
####4.1.设计考虑 
这里首先分析了现有的神经元组织渲染的模式，并指出现有模式的缺点

####4.2.任务分析
#####4.2.1 总体目标（Domain Goals）描述神经学家工作需要探索神经元组织的哪几个方面（整体分析，局部分析，连接分析等等）
#####4.2.2 根据总体目标驱动任务（Domain-Driven Tasks）
* T1-Selecting a neurite subset 选择一个轴突子集
* T2-Single-neurite analysis 单轴突分析
* T3-Multi-neurite analysis 多个轴突分析
* T4-Synapse analysis 突触分析
* T5-Connectivity analysis 连接分析

将总目标分解到5个单个任务，并描述神经学家工作时所要使用的任务
* 探索突触连接---使用到T1,T4,T5
* 探索分支结构---使用到T1,T2,T3
* 探索突触路径---使用到T1,T3,T4,T5

####4.2 可扩展性挑战（Scalability Challenges）抛出挑战，并后续讲到挑战将如何解决
* S1-Many neurons
* S2-Many neurites
* S3-Many branches
* S4-Many synapses
* S5-Many connections between neurites

###5 Visual Elements 描述可视化中每个可视化元素的设计思路（并不是瞎设计，而是个个有理有据）
####5.1 Multi-Scale, Three-Tier Main View 多尺度，三层主视图
* 导航设计（Navigation bar）
* 突触预览（Neurite Overview）
* 工作区视角（Workspace View）
* 按需选择电子显微镜视角（On-Demand Electron Microscopy Views）

###5.2 Neurite Abstraction Levels 突触抽象层面
计算抽象的突触，即如何根据突触的结构去绘成地铁图
#####Branching 
* 贪婪算法，先画树干，再迭代地从右向左添加树枝；每次添加都改变垂直方向，避免视觉交叉
* 如果树枝的高度超过当前层次的高度范围，进行折叠
#####Synapses 突触
* 突触原本不在神经突的切分结构上吗，所以要根据原始3D结构将突触位置投影到神经突上，用CircleNode表示
* Mean-shift cluster – 对于一组投影位置重叠的突触，每条树枝单独计算
#####Synapse links
解决突触连接的混乱(clutter)方法：
* 只在需要时画
* 用stubs代替lines
* 高亮不同结构中的相同突触

###6.Interaction
####Sorting and Filtering
根据科学家的需要去筛选数据集中的部分数据，并根据不同属性来进行排序，使科学家可以缩小探索范围和从不同的角度去查看数据

####Workspace, Pinning, and Pivoting
* Pinning 保持标记状态
* Pivoting   基于选定pivot对全局其他对象进行排序和缩放，使易于找到neighbors
###Connectivity Exploration

###7. Analysis Tools
* Neurite Analysis
* Synapse Analysis

###8. Implementation and Evlauation
####Data
这是文章测试可扩展性的一种思路。目前神经突的已知标记数据集是相对少的，很多的神经突结构并不是很清楚。所以当前无法提供大规模的真实数据来测试系统的可扩展性。所以文章开发了一个 神经元生成模拟器（a simple parameterized neuron simulator）来生成人工合成数据（Synthesized Data）。

###9.Case Studies
通过两个case studies来说明NeuroLines如何改善科学家工作的方式

###MBL总结：
1. 论文从提出问题，连接组学中的神经学家缺乏很好的可视化工具来帮助他们进行神经元重构工作。分析现有的可视化存在的问题。
2. 另设计新的可视化方式，根据科学家的需求而设计，文章非常强调其可视化设计听取神经学家的大量建议和意见，使其可视化的实用性得到保
3. 分析神经学家工作时所探索的几个方面，根据实际情况拆分总体目标为几个小的任务模块
4. 对每个小的可视化元素进行设计
5. 交互设计
6. 分析工具
7. 程序实现与测试
8. Case studies真实例子验证

