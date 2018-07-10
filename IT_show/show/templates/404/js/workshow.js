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
			change_workshow(W,H);
			fei();
		});
		change_workshow(W,H);
		fei();
	} 
	else {//如果不是ie7，然而我还没写

	}
})
function change_workshow(W,H){
	

	$(".container").height(H);
	$(".ball").width(0.3*H);
	$(".ball").height(0.3*H);
	$(".up_row").width(0.05*H);
	$(".down_row").width(0.05*H);
	$(".ball").css({"left":(W-$(".ball").width())/2+"px","bottom":"30px"},)
	$(".up_row").css({"left":($(".ball").width()-$(".up_row").width())/2+"px","top":0.2*$(".ball").height()+"px"});
	$(".down_row").css({"left":($(".ball").width()-$(".up_row").width())/2+"px","bottom":0.2*$(".ball").height()+"px"});
	$(".web_name").css({"line-height":$(".ball").height()+"px","font-size":0.09*$(".ball").height()+"px"})
	$(".block").width(0.25*W);
	$(".block").height(0.12*W);
	$(".in_img").width($(".block").width());
	$(".in_img").height($(".block").height());
	// $(".top").css({"margin-bottom":(-1)*0.15*H+"px"});
	$(".huiji").css({"left":($(".block").width()-$(".huiji").width())/2+"px","top":($(".block").height()-$(".huiji").height())/2+"px"})
	$(".quan").width(0.5*W);
	$(".fanwei").width(W);
	$(".fanwei").height(0.8*H);
	

	var w=$(".block").width()/2;//块宽度的一半
	var h=$(".block").height()/2;//块高度的一半
	var r=$(".ball").width()/2;//球的半径
	var R=w+30+r;//块转动半径
	var center_w=W/2;//球的中心left值
	var center_h=r+30;//球中心bottom值
	
	$(".block1").css({"bottom":center_h+R-h+"px","left":center_w-w+"px"})
	$(".block2").css({"bottom":center_h-r+"px","left":center_w-R-w+"px"})
	$(".block3").css({"bottom":(-1)*(R+h-center_h)+"px","left":center_w-w+"px"})
	$(".block4").css({"bottom":center_h-r+"px","left":center_w+R-w+"px"})
	$(".quan").css({"left":center_w-$(".quan").width()/2+"px",
					"bottom":(-1)*($(".quan").height()/2-center_h)-0.07*W+"px"})
	$(".fanwei").css({"bottom":$(".left").css("bottom")})
	$(".fugai").height($(".left").css("bottom"))
}

$(document).ready(function() {
  // cool nav menu
  $(".block").hover(function(){
  	$(this).children().eq(0).css({"display":"block"});
  	$(this).children().eq(0).animate({opacity:"1"},500);

  	$(this).children().eq(2).css({"display":"block"});
  	$(this).children().eq(2).animate({opacity:"0.5"},500);

  },function(){
  	$(this).children().eq(0).css({"display":"none"});
  	$(this).children().eq(0).animate({opacity:"0"},500);

  	$(this).children().eq(2).css({"display":"none"});
  	$(this).children().eq(2).animate({opacity:"0"},500);

  })//hover

});
$(window).on('load resize', function() {
    var $thisnav = $('.current-menu-item').offset().left;
    $('.menu-item').hover(function() {
      var $left = $(this).offset().left - $thisnav;
      var $width = $(this).outerWidth();
      var $start = 0;
      $('.wee').css({ 'left': $left+10 , 'width': $width-20 });
    }, function() {
      var $initwidth = $('.current-menu-item').width();
      $('.wee').css({ 'left': '10px' , 'width': $initwidth });
    });
  });//滑块
$(".up").click(function(){
	anti_clockwise();
})
$(".down").click(function(){
	clockwise();
})

function fei(){
	var angle=1;//圈旋转的角度
	var time1=setInterval(function(){
		$(".quan").css({
			'transform':'rotate(-'+angle+'deg)',
			'-webkit-transform':'rotate(-'+angle+'deg)',
			'-moz-transform':'rotate(-'+angle+'deg)',
			'-ms-transform':'rotate(-'+angle+'deg)',
			'-o-transform':'rotate(-'+angle+'deg)',
		})
		angle+=1;
	},50)
}
function anti_clockwise(){
	var a=0;
	W = $(window).width();
	var w=$(".block").width()/2;//块宽度的一半
	var h=$(".block").height()/2;//块高度的一半
	var r=$(".ball").width()/2;//球的半径
	var R=w+30+r;//块转动半径
	var center_w=W/2;//球的中心left值
	var center_h=r+30;//球中心bottom值

	var top_bottom=parseInt($(".top").css("bottom"));
	var top_left=parseInt($(".top").css("left"));
	var left_bottom=parseInt($(".left").css("bottom"));
	var left_left=parseInt($(".left").css("left"));
	var bottom_left=parseInt($(".bottom").css("left"));
	var bottom_bottom=parseInt($(".bottom").css("bottom"));
	var right_left=parseInt($(".right").css("left"));
	var right_bottom=parseInt($(".right").css("bottom"));
// *0.017453293     +1.5707964  +3.1415926/2
	var x
	var y

	var anti=setInterval(function(){
		x=center_w+R*Math.sin(a);
		// console.log(x);
		y=center_h-R*Math.cos(a);
		a+=0.1;
		// $(".top").css({"left":top_left-x+"px"})
		$(".left").css({"left":x-w+"px","bottom":y-h+"px"})

		// console.log(top_left-x);
		// if(a>=1.5707963){
		// 	clearInterval(anti);
		// }
	},100)
}
function clockwise(){

}
