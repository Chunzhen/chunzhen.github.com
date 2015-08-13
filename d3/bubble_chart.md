<h1 id="bubble_charthtml">bubble_chart.html知识点</h1>
<h2 id="formatting">Formatting</h2>
<h3 id="d3formatspecifier">d3.format(specifier)</h3>
<p>将数字转化成指定格式的字符串。
函数根据一个指定的字符串格式（specifier）参数返回一个格式化的字符串</p>
<pre><code>var zero=d3.format(&quot;04d&quot;);
zero(2); // “0002&quot;
zero(123); // &quot;0123&quot;
</code></pre>

<p>本次bubble_chart中的例子</p>
<pre><code>format=d3.format(',d');
</code></pre>

<p>将数字以千位为单位用','号来隔开</p>
<pre><code>format(12345); // &quot;12,345&quot;
</code></pre>

<h3 id="d3formatprefixvalueprecision">d3.formatPrefix(value[,precision])</h3>
<p>以指定的值和精度获得一个[SI prefix]对象。加上precision可以实现scale后的精度
这个函数可用来自动判断数据的量级， 如K(千)，M(百万)等等。
函数返回对象有两个属性</p>
<p><code>symbol</code> - 量级单位，如'K','M','G'</p>
<p><code>scale</code> - 量级单位下得到的数目，如123000 量级单位为K scale后为123</p>
<pre><code>var prefix=d3.formatPrefix(123000); 
console.log(prefix.symbol); //'K'
console.log(prefix.scale(123000)); // '123'
</code></pre>

<h3 id="d3roundxn">d3.round(x,[n])</h3>
<p>设置按小数后多少位取整。和toFixed()类似</p>
<pre><code>d3.round(1.23); // 1
d3.round(1.23, 1); // 1.2
d3.round(1.25, 1); // 1.3
d3.round(12.5, 0); // 13
d3.round(12, -1); // 10
</code></pre>

<h3 id="d3requotestring">d3.requote(string)</h3>
<p>返回正则表达式中能够使用的字符</p>
<pre><code>d3.requote(&quot;[]&quot;); // &quot;\[\]&quot;
</code></pre>

<h2 id="pack-layout">Pack Layout</h2>
<p><code>d3.layout.pack</code> - 用递归的圆-包生成一个层次布局。</p>
<p><code>pack.children</code> - 取得或设置子节点的访问器。</p>
<p><code>pack.links</code> - 计算树节点中的父子链接。</p>
<p><code>pack.nodes</code> - 计算包布局并返回节点数组。</p>
<p><code>pack.padding</code> - 指定布局间距（以像素为单位）</p>
<p><code>pack.radius</code> - 指定节点半径（不是由值派生来的）</p>
<p><code>pack.size</code> - 指定布局尺寸。</p>
<p><code>pack.sort</code> - 控制兄弟节点的遍历顺序。</p>
<p><code>pack.value</code> - 取得或设置用于圆尺寸的值访问器。</p>
<p><code>pack</code> - pack.nodes的别名。</p>
<p>通过多个圆圈的多层次嵌套来表示层次结构关系。每个叶节点的圆的大小代表各个数据点的定量尺寸。由多个子节点累积形成的大圆圈近似代表父节点的大小。但是这样的排布会产生许多空白，从而造成空间浪费，显然其不够treemap等结构高效。但是其比treemap更加凸显层次结构。
典型的例子为<a href="http://bl.ocks.org/mbostock/4063530">Circle Packing</a>。
而本例只利用到两个层次的关系来形成bubble chart。根据bubble_chart.json文件，只用到最后一层叶节点来画bubble的大小。而利用最后一层叶节点同属一个父节点的关系来进行颜色划分。</p>
<p>Pack下的数据结构如下：</p>
<h3 id="packroot-packnodesroot">Pack(root) Pack.nodes(root)</h3>
<ul>
<li>parent - 父节点，为空或root</li>
<li>children - 子节点数组，为空或叶子节点</li>
<li>value - 节点的值</li>
<li>depth - 节点的层次</li>
<li>x - 中心x坐标位置</li>
<li>y - 中心y坐标位置</li>
<li>r - 半径大小</li>
</ul>
<h3 id="packlinks">Pack.links</h3>
<pre><code> source - 父节点
 target - 子节点
</code></pre>
<h3 id="packchildrenchildren">Pack.children([children])</h3>
<h3 id="packsortcomparator">Pack.sort([comparator])</h3>
<p>传入比较器，优先绘制数据的关系</p>
<pre><code>function comparator(a,b){
     return a.value-b.value;
}
</code></pre>

<h3 id="packvalue">pack.value()</h3>
<p>可以规定默认值</p>
<h3 id="packsizewh">pack.size([w,h])</h3>
<p>传入pack的大小</p>
<h3 id="packradiusradius">pack.radius([radius])</h3>
<p>默认值</p>
<h3 id="packpaddingpadding">pack.padding([padding])</h3>
<p>每个圆圈最小的距离，默认为0</p>
