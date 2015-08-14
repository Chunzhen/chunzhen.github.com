#circle_packing.html ֪ʶ��

��������������õ�֪ʶӦ�ú�bubble_chart.html��֪ʶ��һ���ġ������ڴ����з�������ôһ������`datum()`
```
var node=svg.datum(root).selectAll('.node')
     .data(pack.nodes)
     .enter()
     .append('g')
     .attr('class',function(d){return d.children?'node':'leaf node';})
     .attr('transform',function(d){return 'translate('+ d.x+','+ d.y+')';});
```
##selection.datum([value])

����API����ʵ�ִ������£�
```
d3.selection.prototype.datum=function(value){
     return arguments.length<1
          ? this.property("__data_")
          : this.property("__data__",value);

};
```
API�Ľ���������£�Ϊ��ǰ��ѡ��Ԫ�����һ��`__data__`����ֵ�������ֵ��Ӧ��ǰѡ��Ԫ�ص����ݡ�`datum()`�����valueΪһ������ʱ���Ὣѡ��������Ԫ�ظ�����ͬ�����ݣ��������һ���������������ǰ������`d`�͵�ǰ����`i`��Ϊ��ǰdomԪ�ص������Ĺ�ϵ��ʹ�ú���������ÿһ��ֵ��������Ϊ`null`ʱ����ɾ���󶨵����ݣ�������`__data__`���ԡ�

ֵ��ע����ǣ���ǰ���������������`map()`��map���������ϸ�������⣬��ʱΪÿ��ѡ���Ԫ�ط�����Ӧ�����ݡ�

API������һ��Ԫ����������ӡ�[link](http://bl.ocks.org/mbostock/1323729)
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
���
```
DOMStringMap{username="shawnbot"}
DOMStringMap{username="mbostock"}
```
`this.dataset` ����ѡ���е����ݼ��ϣ�����`datum()`ȥ�������ݡ�Ϊѡ��Ԫ�ؼ���`__data__`����ֵ��������һ��`DOMStringMap`
##�Ƚ� datum() �� data()
�ο�������� [�� D3.js ѡ����������� �� 1 �� ʹ��datum()������](http://blog.csdn.net/lzhlzz/article/details/42642847)

- `datum()` - ��ָ�����ݸ�ֵ����ѡ���Ԫ��
- `data()` - ���������������ݼ���Ԫ�ؽ��

�����漸��������˵��`datum()`�ļ����÷�
####������ֵ���ı�ѡ��������Ԫ�ص�ֵ���磺
```
var p=d3.selectAll('p')
               .datum("abc")
               .text(function(d,i){
                    return d+" "+i;
               });
```
��ôҳ���ϵ�����pԪ�ص�ֵ���Ϊabc0,abc1,abc2...�ȵȡ�

####��Ԫ�غ��������ֵ
```
p.datum("def")
     .append("span")
     .text("function(d,i){
          return" "+d;
      });
```
��ô��ҳ���ϵ�pԪ�غ�������һ��span��span�����ֵ��def��

