$(function(){
　　var screenwidth,screenheight,mytop,getPosLeft,getPosTop
　　screenwidth = $(window).width();
　　screenheight = $(window).height();
　　//获取滚动条距顶部的偏移
　　mytop = $(document).scrollTop();
　　//计算弹出层的left
　　getPosLeft = screenwidth/2 - 260;
　　//计算弹出层的top
　　getPosTop = screenheight/2 - 150;
　　//css定位弹出层
　　$("#box").css({"left":getPosLeft,"top":getPosTop});
　　//当浏览器窗口大小改变时...
　　$(window).resize(function(){
　　<span style="white-space:pre">  </span>screenwidth = $(window).width();
　　<span style="white-space:pre">  </span>screenheight = $(window).height();
　　<span style="white-space:pre">  </span>mytop = $(document).scrollTop();
　　<span style="white-space:pre">  </span>getPosLeft = screenwidth/2 - 260;
　　<span style="white-space:pre">  </span>getPosTop = screenheight/2 - 150;
　　<span style="white-space:pre">  </span>$("#box").css({"left":getPosLeft,"top":getPosTop+mytop});
　　});
　　//当拉动滚动条时...
　　$(window).scroll(function(){
　　<span style="white-space:pre">  </span>screenwidth = $(window).width();
　　<span style="white-space:pre">  </span>screenheight = $(window).height();
　　<span style="white-space:pre">  </span>mytop = $(document).scrollTop();
　　<span style="white-space:pre">  </span>getPosLeft = screenwidth/2 - 260;
　　<span style="white-space:pre">  </span>getPosTop = screenheight/2 - 150;
　　<span style="white-space:pre">  </span>$("#box").css({"left":getPosLeft,"top":getPosTop+mytop});
　　});
　　//点击链接弹出窗口
　　$("#popup").click(function(){
　　<span style="white-space:pre">  </span>$("#box").fadeIn("fast");
　　<span style="white-space:pre">  </span>//获取页面文档的高度
　　<span style="white-space:pre">  </span>var docheight = $(document).height();
　　<span style="white-space:pre">  </span>//追加一个层，使背景变灰
　　<span style="white-space:pre">  </span>$("body").append("<div id='greybackground'></div>");
　　<span style="white-space:pre">  </span>$("#greybackground").css({"opacity":"0.5","height":docheight});
　　<span style="white-space:pre">  </span>return false;
　　});
　　//点击关闭按钮
　　$("#closeBtn").click(function() {
　　<span style="white-space:pre">  </span>$("#box").hide();
　　<span style="white-space:pre">  </span>//删除变灰的层
　　<span style="white-space:pre">  </span>$("#greybackground").remove();
　　<span style="white-space:pre">  </span>return false;
　　});
});