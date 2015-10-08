###H5开发流程说明与优化
&emsp;&emsp;H5的开发涉及到文案，交互，设计，最后才交付给程序进行实现。而在制作一个H5过程从设计到程序大概需要一个星期的时间。在程序上，初级版本的实现大概需要两天的时间。H5的程序实现追求早完成早解脱，所以一天的时间分为早上+下午+晚上三个时间段，一天工作下来从早上10点到晚上11点大概有11到12个小时的开发时间。第一天时间主要是**切图**（并不是所有的设计师都会帮程序猿切好图的）+**位置标记**+**写成相应的html和scss**。位置标记主要是将切成的小图在原图的位置所标记出来，这是一个相当耗时的过程。我使用`Mark Man`这个工具去进行位置的标记，标记后的图片效果如图所示。
[markdown](img/markdown.png)
而将位置标记后的(x,y)坐标变为scss代码和html代码也是一件非常耗时的工作。生成html代码也是重复性的工作，需要给每个子图片用唯一的className来标记，并写入图片的src位置。html代码如下例所示：
```
<img class="bd1 resize ani" src="img/p1/bd.png" swiper-animate-effect="swing_center" swiper-animate-duration="3s" swiper-animate-delay="0s"/>
```

一个子图片，使用绝对定位的方式来实现css的排版，那么需要`top`、`left`、`width`这三个属性并加上相应的`className`来标记到底是哪个子图片，所以还要看每一个子图片的大小也是非常的耗时。scss代码如下例所示：
```
.className{
     top:0px;
     left:0px;
     width:0px;
}
```
&emsp;&emsp;第一天的工作主要花在切图，标记并将标记转换为scss和html，可以看到在第一天的时间里居然还没有涉及到动画的实现和js来写逻辑。所以这部分的工作应该需要进行优化来缩减整个H5程序开发的周期。

&emsp;&emsp;第二天主要是**基础动画**+**用户交互的实现（比如tap，swipe等操作，用户输入）**+**可选部分（第三方app交互（微信用户信息交互、分享等等）+存储用户信息到数据库）**。第二天偏重功能的开发。
第一个当然是动画。因为整个H5的实现是基于`swiper`这个框架的，而swiper在动画的操作上选择了`animate.css`这个优秀的css动画库来实现。通过引入`swiper.animate.js`即可以在html上加入相应的`class="ani"`，配置相应的动画属性`swiper-animate-effect="动画类型" swiper-animate-duration="动画持续时间" swiper-animate-delay="开始延迟"`完成零js实现动画操作。当然，`animate.css本身也可以通过js的`addClass('animated 动画类型')`来实现动画的添加，但是swiper隐藏了js的实现方式，可以更加快捷的实现动画。

&emsp;&emsp;第二个是用户交互的实现，因为有一些H5需要用户通过**点击屏幕（tap）**，**滑动操作（swipe**），**拖动操作（drag**），**摇一摇（shake）**来实现相应的功能。这也是H5与PPT最大不同的地方。PPT也可以实现非常复杂的展示和动画，但给不了用户很好的交互和操纵感。这也是手机交互和电脑PC的鼠标交互所不同的地方。这部分的工作主要是依照H5的需求，工作的效率完全取决于程序员的经验和能力。并没有很好的捷径或者模板来优化这部分的工作。或许可以在有空的时候总结一下H5的所有可能的交互方式，并实现相应的代码，这样也会对开发的效率有所帮助。另外，在H5的第三方类库上，使用的不是`jQuery`而是`zepto`，`zepto`的体积更小，使用动画上用css3实现，同时也拥有不少针对移动端的操作。至于`jQuery`与`zepto`有更多不同的地方，可以网上搜搜。
第三个可选的部分，H5最流行的发布平台无疑是微信，尽管类似网易新闻客户端，微博等都有H5的身影，但微信的朋友圈加朋友间的链接，让H5在微信更加流行。同时，微信在公众号的开发接口方面也给以了很大的支持。详情可以了解[微信JS-SDK](http://mp.weixin.qq.com/wiki/7/aaa137b55fb2e0456bf8dd9148dd613f.html)，最常用到的是获取微信用户的信息，自定义分享等等。而存储用户信息到数据库，我使用了我最为熟悉的`PHP CI`框架去实现。这部分工作应该是相对轻松的。

&emsp;&emsp;所以两天的时间开发一个初级版本的H5时间仅仅是够用。而如果一些交互和功能上更加复杂的话，可能还需要另外多半天的时间。现在来总结一下开发的几个小分块与耗时（以一天为6个点）：

* 切图：1
* 标记：1
* scss和html转换：1
* 基础动画：0.5
* 交互：1~1.5
* 第三方app交互：1
* 存储信息：1

&emsp;&emsp;从上面来看，完成一个H5是需要2-3天的时间。如果能够优化切图、标记和scss和html转换这部分的工作，将会大大的提高开发的效率。而可以优化的部分便是标记、scss和html转换这两个部分的工作。标记的需求很简单，就是给出两幅图片，原图与切图。切图是原图上的一个小块，并且像素比例都是一致的。这在计算机视觉的图像识别里面是比较简单的事情，更加高端的当然就是图像的视角变形、缩放都可以标记出相应的位置。所以查阅了相关资料和网上的代码。终于让我找到了相应的解决方法。使用`Opencv`的`SIFT`或者`SURF`算法即可对图像进行匹配。实现的代码是基于网上的一个Python实现的代码：[飘逸的python - 使用图像匹配SIFT算法进行LOGO检测](http://blog.csdn.net/handsomekang/article/details/41448697)。当然其他语言比如C++、Java等也能够实现相应的操作。实现代码如下所示：
```
def find_location(img1,path2):
     img2=cv2.imread(path2,0)

     sift=cv2.SIFT()

     kp1,des1=sift.detectAndCompute(img1,None)
     kp2,des2=sift.detectAndCompute(img2,None)

     h2,w2=img2.shape[:2]

     try:
          FLANN_INDEX_KDTREE=0
          index_params=dict(algorithm=FLANN_INDEX_KDTREE,trees=5)
          search_params=dict(checks=50)
          flann=cv2.FlannBasedMatcher(index_params,search_params)
          matches=flann.knnMatch(des1,des2,k=2)
     except:
          return -1,-1,h2, w2
     
     if(len(matches)<1):
          return -1,-1,h2, w2

     good=[]
     positionX=[]
     positionY=[]
     percent=0.0
     flag=False
     while(not flag and percent<=0.5):
          percent+=0.05
          positionX=[]
          positionY=[]
          for m,n in matches:
               if m.distance <percent*n.distance:
                    good.append(m)
                    x=int(kp1[m.queryIdx].pt[0])-int(kp2[m.trainIdx].pt[0])
                    y=int(kp1[m.queryIdx].pt[1])-int(kp2[m.trainIdx].pt[1])
                    positionX.append(x)
                    positionY.append(y)
          
          if(len(good)>0):
               sorted(positionX)
               sorted(positionY)
               index=int(len(good)/2)
               return positionX[index],positionY[index],h2, w2

     return -1,-1,h2, w2
```
&emsp;&emsp;代码中的`find_location`函数即可返回img2在img1中的x,y位置和img的宽高。这样即可直接在此基础上生成相应的HTML和scss源码。实验过程中发现了一些问题，即是有一些图片很小或者是一张纯色的图片或者是被其他图片覆盖掉的切图，那么`SIFT`可能找不到很好的特征进行匹配。所以，一些小图还是需要人工去进行位置的标记，不过，还是能够把大部分图片匹配到的。

&emsp;&emsp;下一步的开发优化工作应该是对基本的HTML和js建立一个模板文件，可以在每次新建一个工程的时候重复使用。

