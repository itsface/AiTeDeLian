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
	$(".menu").children().eq(4).addClass("current-menu-item")

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
			change_member(W,H);
		});
		change_member(W,H);
	} 
	else {//如果不是ie7，然而我还没写

	}
})
function change_member(W,H){
	$(".container").height(H);
	// $(".mountain").css({"bottom":"0px"})
	$(".main").width(0.7*W);
	$(".time_star").width($(".main").width());
	$(".main").height($(".time_star").height());
	$(".main").css({"top":(H-$(".main").height())/2+50+"px","left":(W-$(".main").width())/2+"px"})
	var x=$(".main").width();
	var y=$(".main").height();
	$(".quan").css({"width":0.09*x+"px","height":0.09*x+"px"})
	$(".quan2011").css({"left":0.001*x+"px","top":0.36*y+"px"})
	$(".quan2012").css({"left":0.142*x+"px","top":0.08*y+"px"})
	$(".quan2013").css({"left":0.31*x+"px","top":0.60*y+"px"})
	$(".quan2014").css({"left":0.455*x+"px","top":0.278*y+"px"})
	$(".quan2015").css({"left":0.61*x+"px","top":0.01*y+"px"})
	$(".quan2016").css({"left":0.754*x+"px","top":0.4*y+"px"})
	$(".quan2017").css({"left":0.91*x+"px","top":0.246*y+"px"})
	$(".member_block").height(0.6*H);
	$(".member_block").width(0.5*W);
	$(".member_block").css({"top":(H-$(".member_block").height())/2+50+"px","left":(W-$(".member_block").width())/2+"px"})
	var ah=$(".member_block").height();
	var aw=$(".member_block").width();
	$(".lunbo").width(0.8*aw);
	$(".lunbo").height(0.6*ah);
	$(".lunbo").css({"top":(ah-$(".lunbo").height())/2+"px","left":(aw-$(".lunbo").width())/2+"px"});
	$(".grade").css({"left":(aw-$(".lunbo").width())/2+"px","margin-top":0.06*ah+"px"});
	$(".turnleft_row").width(0.02*aw+"px");
	$(".turnright_row").width(0.02*aw+"px");
	$(".turnleft_row").css({"top":(ah-$(".turnleft_row").height())/2+"px","left":0.02*aw+"px"});
	$(".turnright_row").css({"top":(ah-$(".turnright_row").height())/2+"px","right":0.02*aw+"px"});
	$(".turn_page").height(0.14*ah);
	$(".turn_page").width(0.25*aw);
	$(".turn_page").css({"bottom":0.02*ah+"px",left:(aw-$(".turn_page").width())/2+"px"});
	var turn_h=$(".turn_page").height();
	var turn_w=$(".turn_page").width();
	$(".page").width(0.2*turn_w);
	$(".page").height(turn_h);
	$(".page").css({"margin-right":0.05*turn_w+"px"});
	$(".qiu").height(0.12*turn_w);
	$(".qiu").width(0.12*turn_w);
	$(".uprow").width(0.1*turn_w);
	$(".downrow").width(0.1*turn_w);
	$(".qiu").css({"top":0.3*turn_h+"px","left":($(".page").width()-$(".qiu").width())/2+"px"});
	$(".uprow").css({"top":0.01*turn_h+"px","left":($(".page").width()-$(".uprow").width())/2+"px"});
	$(".downrow").css({"top":0.827*turn_h+"px","left":($(".page").width()-$(".uprow").width())/2+"px"});
	$(".member2016_block .turn_page").width(0.3*aw);
	$(".member2016_block .turn_page .page").css({"margin-right":0.04*turn_w+"px"});
	$(".member2016_block .turn_page .qiu").css({"top":0.3*turn_h+"px","left":($(".page").width()-$(".qiu").width())/2+"px"});


	var bh=$(".lunbo").height();
	var bw=$(".lunbo").width();
	$(".boy").height(bh);
	$(".boy").width(0.266*bw);
	$(".boy").css({"margin-right":0.1*bw+"px"});
	$(".portrait").width($(".boy").width());
	$(".portrait").height($(".boy").width());
	$(".name").css({"line-height":0.2*bh+"px"})
	$(".department").css({"line-height":0.1*bh+"px"})
}

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
//

$(".quan2011").click(function(){
	$(".member_block").css({"display":"none"});
	$(".member2011_block").css({"opacity":"0","display":"block"});
	$(".member2011_block").animate({opacity:"1"},700)
})
$(".quan2012").click(function(){
	$(".member_block").css({"display":"none"});
	$(".member2012_block").css({"opacity":"0","display":"block"});
	$(".member2012_block").animate({opacity:"1"},700)
})
$(".quan2013").click(function(){
	$(".member_block").css({"display":"none"});
	$(".member2013_block").css({"opacity":"0","display":"block"});
	$(".member2013_block").animate({opacity:"1"},700)
})
$(".quan2014").click(function(){
	$(".member_block").css({"display":"none"});
	$(".member2014_block").css({"opacity":"0","display":"block"});
	$(".member2014_block").animate({opacity:"1"},700)
})
$(".quan2015").click(function(){
	$(".member_block").css({"display":"none"});
	$(".member2015_block").css({"opacity":"0","display":"block"});
	$(".member2015_block").animate({opacity:"1"},700)
})
$(".quan2016").click(function(){
	$(".member_block").css({"display":"none"});
	$(".member2016_block").css({"opacity":"0","display":"block"});
	$(".member2016_block").animate({opacity:"1"},700)
})
$(".quan2017").click(function(){
	$(".member_block").css({"display":"none"});
	$(".member2017_block").css({"opacity":"0","display":"block"});
	$(".member2017_block").animate({opacity:"1"},700)
})
$(".cha").click(function(){
	$(".member_block").animate({opacity:"0"},700,function(){disappear()})
})
function disappear(){
	$(".member_block").css({"display":"none"})
}

