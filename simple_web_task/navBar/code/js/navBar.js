(function($){
	//默认参数
	var defaults={
		linkData:[
			{text:'微云',href:'http://www.baidu.com'}			
		]
	};
	$.fn.extend({
		'navBar':function(options){
			var opts=$.extend({},defaults,options);
			console.log(options);
			return this.each(function(){
				var that=$(this); //记录当前的this
				that.addClass('navBar'); 
				var linkData=opts.linkData; 
				var dataLen=linkData.length; //导航栏栏目个数
				var linkWidths=[]; //所有栏目的宽度
				var lastHideIndex=-1; //上次收缩的最大index，-1表示不收缩
				var moreWidth=0; //更多按钮的宽度
				var allPadding=0; //padding_left+padding_right+margin_left+margin_right

				//根据需要收缩的index绑定bar，收缩的栏目放进ul中
				var bindBarHtml=function(dataIndex){
					var barHtml='<div class="bar">';

					var listHtml='<div class="content-menu" style="display:none;"><ul>';
								
					if(dataIndex>=0){
						barHtml+='<a class="more" href="#" style="z-index:'+(dataLen+1)+';"><span>«</span></a>';
					}
					for(var x in linkData){
						if(x>dataIndex){
							barHtml+='<a href="'+linkData[x].href+'" style="z-index:'+(dataLen-x)+';"><span>'+linkData[x].text+'</span></a>';
						}else{
							listHtml+='<li><a href="'+linkData[x].href+'" ><i class="ico-folder"></i><span>'+linkData[x].text+'</span></a></li>';
						}
							
					}
					barHtml+='</ul></div>';
					listHtml+='</div>';
					that.html(barHtml);
					if(dataIndex>=0){
						that.append(listHtml);
						that.find('.more').unbind('click');
						that.find('.more').on('click',function(){
							that.find('.content-menu').toggle();
						});
					}
				}
				var resize=function(){
					bindBarHtml(-1);
					var barWidth=that.width(); //计算当前bar的宽度

					if(lastHideIndex!=-1){ //如果lastHideIndex!=-1，证明bar中有more这个栏目，可用barWidth需要减去moreWidth
						barWidth-=moreWidth;
					}
					
					//console.log("barWidth:"+barWidth);
					//第一次计算所有栏目的宽度
					if(linkWidths.length==0){
						//计算more的宽度
						that.find('.bar').append('<a class="more" href="#" style="z-index:'+(dataLen+1)+';"><span>«</span></a>');						
						var padding_left=that.find('.more').css('padding-left');
						padding_left=parseInt(padding_left.substr(0,padding_left.length-2));
						var padding_right=that.find('.more').css('padding-right');
						padding_right=parseInt(padding_right.substr(0,padding_right.length-2));
						var margin_left=that.find('.more').css('margin-left');
						margin_left=parseInt(margin_left.substr(0,margin_left.length-2));
						var margin_right=that.find('.more').css('margin-right');
						margin_right=parseInt(margin_right.substr(0,margin_right.length-2));

						allPadding=padding_left+padding_right+margin_left+margin_right;
						moreWidth=that.find('.more').width()+allPadding;
						that.find('.more').remove();

						//计算所有栏目宽度
						that.find('.bar a').each(function(index){
							linkWidths[index]=$(this).width()+allPadding;
						});
					}
					
					//检测需要排布的index
					var currentWidth=0;
					var hideIndex=-1;
					for(var i=dataLen-1;i>=0;i--){
						currentWidth+=linkWidths[i];
						if(currentWidth>=barWidth-1){
							hideIndex=i;						
							break;
						}
					}
					lastHideIndex=hideIndex;
					//console.log('hideIndex:'+hideIndex);
					if(hideIndex>=0){
						//重新排布
						bindBarHtml(hideIndex);
					}
				}

				//初始化
				resize();

				//动态改变
				$(window).resize(function(){
					resize();
				});
			});
		}
	});	
})(jQuery);