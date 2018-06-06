$(document).ready(function() {
	var userAgent = navigator.userAgent.toLowerCase();
	// Figure out what browser is being used
	jQuery.browser = {
	version: (userAgent.match(/.+(?:rv|it|ra|ie)[\/: ]([\d.]+)/) || [])[1],
	safari: /webkit/.test(userAgent),
	opera: /opera/.test(userAgent),
	msie: /msie/.test(userAgent) && !/opera/.test(userAgent),
	mozilla: /mozilla/.test(userAgent) && !/(compatible|webkit)/.test(userAgent)
	}; //通过正则去判断当前使用的哪种内核的浏览器
	var H, W;
	if ($.browser.version != "7.0") //判断是不是IE7 ，IE7下不支持“$(window).width()”
	{
		H = $(window).height(); //获得窗口宽度
		W = $(window).width(); //获得窗口高度
		$(window).resize(function() { //浏览器缩放重新获得窗口宽高
			H = $(window).height();
			W = $(window).width();
			change_fourtofour(W,H);
		});
		change_fourtofour(W,H);
	} 
	else {//如果不是ie7，然而我还没写

	}
})
function change_fourtofour(W,H){
	$(".container").height(0.9*H);
	$(".banqiu").width(0.8*W).css("left",0.1*W);
	$(".fourto").css({"bottom":0.1*W,"left":0.425*W,"width":0.15*W});
	$(".huiji").css({"bottom":0.4*H,"left":0.25*W,"width":0.2*H});
	$(".main").css({"height":H-$(".banqiu").height()-30})
}
$(".return").click(function(){

	var huiji_bottom=$(".huiji").css("bottom");
	huiji_bottom=parseInt(huiji_bottom);

	var huiji_left=$(".huiji").css("left");
	huiji_left=parseInt(huiji_left);

	var time=setInterval(function(){
		huiji_bottom+=15;
		huiji_left-=15;
		$(".huiji").css({"bottom":huiji_bottom+"px","left":huiji_left+"px"});
		if(parseInt($(".huiji").css("left"))<0){
				clearInterval(time);
			}
		
	},50)

	function delayer(){
 		window.location = "./home(pre).html";
	}
	jQuery(document).ready(function(){
 	setTimeout(function(){
 		delayer();
 	}, 1000);
 	//这里实现延迟5秒跳转
	});
})