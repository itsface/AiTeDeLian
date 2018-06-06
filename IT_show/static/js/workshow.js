var webNum = 5, nowBlock = 1,H, W, circling, upsc, sidesc, sizechange;
var upoffset;//left和right相对轨迹点向上的位移
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
    addc();
	upsc=1.1;
    sidesc=0.8;
	circling = false;
	sizechange = true;
	$(".menu").children().eq(2).addClass("current-menu-item")

    var $thisnav = $('.current-menu-item').offset().left-$('.x').offset().left;
	var $initwidth = $('.current-menu-item').width();
      $('.wee').css({ 'left': $thisnav+10+'px' , 'width': $initwidth });

	if ($.browser.version != "7.0") //判断是不是IE7 ，IE7下不支持“$(window).width()”
	{
		H = $(window).height(); //获得窗口宽度
		W = $(window).width(); //获得窗口高度

		$(window).resize(function() { //浏览器缩放重新获得窗口宽高
			H = $(window).height();
			W = $(window).width();
			change_workshow();
		});
		change_workshow();
		fei();
	} 
	else {//如果不是ie7，然而我还没写

	}
})

function next(x,k=1) {
    return (x + k - 1 + webNum) % webNum  + 1;
}

function _(x) {
    return x.toString();
}

function change_workshow(){
	sizechange = true;

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
	$(".huiji").css({"left":($(".block").width()-$(".huiji").width())/2+"px","top":($(".block").height()-$(".huiji").height())/2+"px"})
	$(".quan").width(0.5*W);
	$(".fanwei").width(W);
	$(".fanwei").height(0.8*H);
	

	let w=0.125*W;//块宽度的一半
	let h=0.06*W;//块高度的一半
	var r=$(".ball").width()/2;//球的半径
	var R=W/4;//块转动半径
	var center_w=W/2;//旋转中心left值
	var center_h=r+30-0.07*W;//旋转中心bottom值
    upoffset = H/5;//left和right相对轨迹点向上的位移
    addc()
    extendsc();
	$(".top").css({"bottom":center_h+R-$(".top").height()/2+"px","left":center_w-$(".top").width()/2+"px"});
	$(".left").css({"bottom":center_h-$(".left").height()/2+upoffset+"px","left":center_w-R-$(".left").width()/2+"px"});
	$(".right").css({"bottom":center_h-$(".right").height()/2+upoffset+"px","left":center_w+R-$(".right").width()/2+"px"});

	adapt()
	$(".quan").css({"left":center_w-R+"px",
					"bottom":center_h-R+"px"});
	$(".fanwei").css({"bottom":$(".left").css("bottom")});
	$(".fugaitwo").css({"height":upoffset+"px","bottom":center_h-$(".left").height()/2+"px","left":W/2+W/10, "width": '40%'});
	$(".fugai").css({"height":upoffset+"px","bottom":center_h-$(".left").height()/2+"px","left":0, "width": '40%'});
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
$(".up").click(function(){
	clockwise(1);
})
$(".down").click(function(){
	clockwise(-1);
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

function addc(k=0) {
    let next1Block = next(nowBlock);
    let next2Block = next(next1Block);
    $(".block"+_(nowBlock)).addClass("left");
    $(".block"+_(next1Block)).addClass("top");
    $(".block"+_(next2Block)).addClass("right");

    $(".in_img"+_(nowBlock)).addClass("leftimg");
    $(".in_img"+_(next1Block)).addClass("topimg");
    $(".in_img"+_(next2Block)).addClass("rightimg");

  	$(".block"+_(nowBlock)).children().eq(0).addClass("leftfj");
    $(".block"+_(next1Block)).children().eq(0).addClass("topfj");
    $(".block"+_(next2Block)).children().eq(0).addClass("rightfj")
    if (k!=0){
        $(".block"+_(k)).addClass("bottom");
        $(".in_img"+_(k)).addClass("bottomimg");
        $(".block"+_(k)).children().eq(0).addClass("bottomfj")
        $(".bottom").css({'display':'block'});
    }
}

function extendsc(sc=0) {
    x = [".top",".right",".left",".bottom"];
    y = [-1,1,1,-1];
    z = [upsc,sidesc,sidesc,upsc]
    x.forEach(function (str,index) {
        $(str).width(0.25*W*((upsc-sidesc)*sc*y[index]+z[index]));
        $(str).height(0.1247*W*((upsc-sidesc)*sc*y[index]+z[index]));
    })
}

function adapt(f=true) {
    x=[".left",".right",".top",".bottom"];
    x.forEach(function (str) {
        $(str+"img").width($(str).width());
        $(str+"img").height($(str).height());
        if (f)
        $(str+"fj").css({"left":($(str).width()-$(str+"fj").width())/2+"px","top":($(str).height()-$(str+"fj").height())/2+"px","display":"none"})
    })
}

function clockwise(fx){
	// $(".top").css({"margin-bottom":(-1)*0.15*$(window).height()+"px"})
    if (circling) return;
    circling = true;

    $(".left").removeClass("left");
    $(".right").removeClass("right");
    $(".top").removeClass("top");
    $(".bottom").removeClass("bottom");

    $(".leftfj").removeClass("leftfj");
    $(".rightfj").removeClass("rightfj");
    $(".topfj").removeClass("topfj");
    $(".bottomfj").removeClass("bottomfj");

    $(".leftimg").removeClass("leftimg");
    $(".rightimg").removeClass("rightimg");
    $(".topimg").removeClass("topimg");
    $(".bottomimg").removeClass("bottomimg");

    if (fx===1){
        addc(next(nowBlock,3))
    }
    if (fx===-1){
        addc(next(nowBlock,-1));
    }
	var a=0;
// *0.017453293       +3.1415926/2  
	var left_x,left_y;
	var bottom_x,bottom_y;
	var right_x,right_y;
	var top_x,top_y;
    let w;//块宽度的一半
    let h;//块高度的一半
    var r;//球的半径
    var R;//块转动半径
    var center_w;//旋转中心left值
    var center_h;//旋转中心bottom值
    var pi=3.1415926;
    sizechange = true;
	var anti=setInterval(function(){
	    if (sizechange) {
            w = 0.125 * W;//块宽度的一半
            h = 0.06 * W;//块高度的一半
            r = $(".ball").width() / 2;//球的半径
            R = W / 4;//块转动半径
            center_w = W / 2;//旋转中心left值
            center_h = r + 30 - 0.07 * W;//旋转中心bottom值
            sizechange = false;
	    }
		left_x=center_w+R*Math.sin(a-pi/2);
		left_y=center_h-R*Math.cos(a-pi/2);

		bottom_x=center_w+R*Math.sin(a);
		bottom_y=center_h-R*Math.cos(a);

		right_x=center_w+R*Math.sin(a+pi/2);
		right_y=center_h-R*Math.cos(a+pi/2);

		top_x=center_w+R*Math.sin(a+pi);
		top_y=center_h-R*Math.cos(a+pi);
		a+=0.010*fx;
		var sc = a*fx/(pi/2);

		// console.log((-1)*0.15*$(window).height());
		// $(".top").css({"left":top_left-left_x+"pleft_x"})
        extendsc(sc);
		$(".left").css({"left":left_x-$(".left").width()/2+"px","bottom":left_y-$(".left").height()/2+upoffset*(1-sc)+"px"});
		$(".bottom").css({"left":bottom_x-$(".bottom").width()/2+"px","bottom":bottom_y-$(".bottom").height()/2+upoffset*sc+"px"});
		$(".right").css({"left":right_x-$(".right").width()/2+"px","bottom":right_y-$(".right").height()/2+upoffset*(1-sc)+"px"});
		$(".top").css({"left":top_x-$(".top").width()/2+"px","bottom":top_y-$(".top").height()/2+upoffset*sc+"px"});
        adapt(false);
        if(a*fx>=1.574){
			clearInterval(anti);
			if (fx===1){
			    $(".left").css({'display':'none'});
            }
            if (fx===-1){
			    $(".right").css({'display':'none'});
            }

            adapt(true);
            $(".left").removeClass("left");
            $(".right").removeClass("right");
            $(".top").removeClass("top");
            $(".bottom").removeClass("bottom");

            $(".leftfj").removeClass("leftfj");
            $(".rightfj").removeClass("rightfj");
            $(".topfj").removeClass("topfj");
            $(".bottomfj").removeClass("bottomfj");

            $(".leftimg").removeClass("leftimg");
            $(".rightimg").removeClass("rightimg");
            $(".topimg").removeClass("topimg");
            $(".bottomimg").removeClass("bottomimg");
            nowBlock=next(nowBlock,fx);
            circling = false;
		}
	},1)
}
