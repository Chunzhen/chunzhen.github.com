#bubble_chart.html知识点
##Formatting
###d3.format(specifier)
将数字转化成指定格式的字符串。
函数根据一个指定的字符串格式（specifier）参数返回一个格式化的字符串
```
var zero=d3.format("04d");
zero(2); // “0002"
zero(123); // "0123"
```
本次bubble_chart中的例子
```
format=d3.format(',d');
```

将数字以千位为单位用','号来隔开
```
format(12345); // "12,345"
```
###d3.formatPrefix(value[,precision])
以指定的值和精度获得一个[SI prefix]对象。加上precision可以实现scale后的精度
这个函数可用来自动判断数据的量级， 如K(千)，M(百万)等等。
函数返回对象有两个属性

`symbol` - 量级单位，如'K','M','G'

`scale` - 量级单位下得到的数目，如123000 量级单位为K scale后为123
```
var prefix=d3.formatPrefix(123000);
console.log(prefix.symbol); //'K'
console.log(prefix.scale(123000)); // '123'
```
###d3.round(x,[n])
设置按小数后多少位取整。和toFixed()类似
```
d3.round(1.23); // 1
d3.round(1.23, 1); // 1.2
d3.round(1.25, 1); // 1.3
d3.round(12.5, 0); // 13
d3.round(12, -1); // 10
```
###d3.requote(string)
返回正则表达式中能够使用的字符
```
d3.requote("[]"); // "\[\]"
```

##Pack Layout
`d3.layout.pack` - 用递归的圆-包生成一个层次布局。

`pack.children` - 取得或设置子节点的访问器。

`pack.links` - 计算树节点中的父子链接。

`pack.nodes` - 计算包布局并返回节点数组。

`pack.padding` - 指定布局间距（以像素为单位）

`pack.radius` - 指定节点半径（不是由值派生来的）

`pack.size` - 指定布局尺寸。

`pack.sort` - 控制兄弟节点的遍历顺序。

`pack.value` - 取得或设置用于圆尺寸的值访问器。

`pack` - pack.nodes的别名。

通过多个圆圈的多层次嵌套来表示层次结构关系。每个叶节点的圆的大小代表各个数据点的定量尺寸。由多个子节点累积形成的大圆圈近似代表父节点的大小。但是这样的排布会产生许多空白，从而造成空间浪费，显然其不够treemap等结构高效。但是其比treemap更加凸显层次结构。
典型的例子为[Circle Packing](http://bl.ocks.org/mbostock/4063530)。
而本例只利用到两个层次的关系来形成bubble chart。根据bubble_chart.json文件，只用到最后一层叶节点来画bubble的大小。而利用最后一层叶节点同属一个父节点的关系来进行颜色划分。

Pack下的数据结构如下：

###Pack(root) Pack.nodes(root)

+ parent - 父节点，为空或root
+ children - 子节点数组，为空或叶子节点
+ value - 节点的值
+ depth - 节点的层次
+ x - 中心x坐标位置
+ y - 中心y坐标位置
+ r - 半径大小
    
###Pack.links
     source - 父节点
     target - 子节点
###Pack.children([children])

###Pack.sort([comparator])
传入比较器，优先绘制数据的关系
```
function comparator(a,b){
     return a.value-b.value;
}
```
###pack.value()
可以规定默认值
###pack.size([w,h])
传入pack的大小
###pack.radius([radius])
默认值
###pack.padding([padding])
每个圆圈最小的距离，默认为0