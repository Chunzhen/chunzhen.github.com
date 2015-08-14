#circle_packing.html 知识点

本来想这个例子用的知识应该和bubble_chart.html的知识是一样的。但是在代码中发现了这么一个函数`datum()`
```
var node=svg.datum(root).selectAll('.node')
     .data(pack.nodes)
     .enter()
     .append('g')
     .attr('class',function(d){return d.children?'node':'leaf node';})
     .attr('transform',function(d){return 'translate('+ d.x+','+ d.y+')';});
```
##selection.datum([value])

根据API，其实现代码如下：
```
d3.selection.prototype.datum=function(value){
     return arguments.length<1
          ? this.property("__data_")
          : this.property("__data__",value);

};
```
API的解析大概如下，为当前的选择元素添加一个`__data__`属性值，而这个值对应当前选择元素的数据。`datum()`传入的value为一个常数时，会将选择集中所有元素赋予相同的数据；如果传入一个函数，这根据以前的数据`d`和当前索引`i`作为当前dom元素的上下文关系，使用函数来设置每一个值。而设置为`null`时，会删除绑定的数据，不创建`__data__`属性。

值得注意的是，以前这个方法的名称是`map()`，map可能名字上更容易理解，即时为每个选择的元素分配相应的数据。

API给出了一个元素排序的例子。[link](http://bl.ocks.org/mbostock/1323729)
```
<ul id="list">
  <li data-username="shawnbot">Shawn Allen</li>
  <li data-username="mbostock">Mike Bostock</li>
</ul>
```
```
d3.selectAll("#list li")
    .datum(function() { return this.dataset; })
    .sort(function(a, b) { return d3.ascending(a.username, b.username); });
```
```
console.log(this.dataset);
```
输出
```
DOMStringMap{username="shawnbot"}
DOMStringMap{username="mbostock"}
```
`this.dataset` 返回选择集中的数据集合，再用`datum()`去分配数据。为选择元素加上`__data__`属性值，即存入一个`DOMStringMap`
##比较 datum() 与 data()
参考这边文章 [【 D3.js 选择集与数据详解 — 1 】 使用datum()绑定数据](http://blog.csdn.net/lzhlzz/article/details/42642847)

- `datum()` - 将指定数据赋值给被选择的元素
- `data()` - 将数据数组与数据集的元素结合

用下面几个例子来说明`datum()`的几种用法
####传入数值，改变选择集中所有元素的值。如：
```
var p=d3.selectAll('p')
               .datum("abc")
               .text(function(d,i){
                    return d+" "+i;
               });
```
那么页面上的所有p元素的值会变为abc0,abc1,abc2...等等。

####在元素后面添加新值
```
p.datum("def")
     .append("span")
     .text("function(d,i){
          return" "+d;
      });
```
那么在页面上的p元素后面会添加一个span，span里面的值是def。

