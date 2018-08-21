var point_hua=0;
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
			if(point_hua==0){
				change_home(W,H);
			}
			else if(point_hua==1){
				down();
          		$(".imagine").children().eq(0).children().eq(0).attr("src","/static/img/cahui.png");
				$(".qixiang").css("display","block");
				$(".jingzhun").css("display","none");
				$(".youxiu").css("display","none");
			}
		});
		change_home(W,H);

		var yellow_now=$(".planet_yellow").css("top");
		yellow_now=yellow_now.substring(0,yellow_now.length-2)-0;
		var point_yellow=0,flag_yellow=0;

		var huan_left=$(".planet_huan").css("left");
		var huan_top=$(".planet_huan").css("top");
		huan_left=huan_left.substring(0,huan_left.length-2)-0;
		huan_top=huan_top.substring(0,huan_top.length-2)-0;
		var point_huan=0,flag_huan=0;

		var blue_now=$(".planet_blue").css("left");
		blue_now=blue_now.substring(0,blue_now.length-2)-0;
		var point_blue=0,flag_blue=0;

		var qiu1_now=$(".qiu1").css("top");
		qiu1_now=qiu1_now.substring(0,qiu1_now.length-2)-0;
		var point_qiu1=0,flag_qiu1=0;

		var qiu2_now=$(".qiu2").css("right");
		qiu2_now=qiu2_now.substring(0,qiu2_now.length-2)-0;
		var point_qiu2=0,flag_qiu2=0;

		
		var time=setInterval(function(){
			if(point_yellow==0){
				flag_yellow++;
				yellow_now+=1;
				if(flag_yellow==100){
					point_yellow=1;
					flag_yellow=0;
				}
			}
			else if(point_yellow==1){
				flag_yellow++;
				yellow_now-=1;
				if(flag_yellow==100){
					point_yellow=0;
					flag_yellow=0;
				}
			}
			$(".planet_yellow").css({"top":yellow_now+"px"});

			if(point_huan==0){
				flag_huan++;
				huan_left-=1;
				huan_top-=1;
				if(flag_huan==50){
					point_huan=1;
					flag_huan=0;
				}
			}
			else if(point_huan==1){
				flag_huan++;
				huan_left+=1;
				huan_top+=1;
				if(flag_huan==50){
					point_huan=0;
					flag_huan=0;
				}
			}
			$(".planet_huan").css({"top":huan_top+"px"});
			$(".planet_huan").css({"left":huan_left+"px"});

			if(point_blue==0){
				flag_blue++;
				blue_now+=1;
				if(flag_blue==150){
					point_blue=1;
					flag_blue=0;
				}
			}
			else if(point_blue==1){
				flag_blue++;
				blue_now-=1;
				if(flag_blue==150){
					point_blue=0;
					flag_blue=0;
				}
			}
			$(".planet_blue").css({"left":blue_now+"px"});

			if(point_qiu1==0){
				flag_qiu1++;
				qiu1_now-=1;
				if(flag_qiu1==150){
					point_qiu1=1;
					flag_qiu1=0;
				}
			}
			else if(point_qiu1==1){
				flag_qiu1++;
				qiu1_now+=1;
				if(flag_qiu1==150){
					point_qiu1=0;
					flag_qiu1=0;
				}
			}
			$(".qiu1").css({"top":qiu1_now+"px"});

			if(point_qiu2==0){
				flag_qiu2++;
				qiu2_now-=1;
				if(flag_qiu2==100){
					point_qiu2=1;
					flag_qiu2=0;
				}
			}
			else if(point_qiu2==1){
				flag_qiu2++;
				qiu2_now+=1;
				if(flag_qiu2==100){
					point_qiu2=0;
					flag_qiu2=0;
				}
			}
			$(".qiu2").css({"right":qiu2_now+"px"});

		},100)
	} 
	else {//如果不是ie7，然而我还没写

	}
})



function change_home(W,H){
	$(".back_ground").height(0.7*H);
	var temp=0.17*H;
	temp=temp+"px";
	// temp=0.3*H；
	$(".name_main").css("margin-top",temp);
	$(".in_center").height(0.3*H);
	// $(".intro_detail").height(0.7*H);
	$(".about_us h2").css({"margin-top":0.02*H,"margin-bottom":0.01*H})
	$(".block").css({"margin-top":0.04*H})
	$(".short_intro").height(0.299*H);
}

var mi=0;
function down(){
	var i;
	for(i=0;i<3;i++){
		$(".block").eq(i).children().eq(0).children().eq(0).attr("src","/static/img/huang.png")
	}//改变三个圈

	if(point_hua==0){
		$(".back_ground").animate({height:$(".head").css("height")},1000);
		$(".head").css({"background-color":"white","opacity":"0"});
		$(".head").animate({opacity:"1"},1000);
		$(".menu-item a").css({"color":"black"});
		$(".nav .logoandlink h2").css({"color":"black"});
		$(".intro_detail").height(0.6*$(window).height());
		// $(".back_ground").not(".name_main").animate({bottom:0.7*$(window).height()},1000);
		$(".short_intro").animate({height:0.999*$(window).height()-parseInt($(".head").css("height"))},1000,function(){mi=1});
		// $(".intro_detail").css({"height",0.7*H})
		point_hua=1;
	}
	$(".block p").css({"display":"none"})
	console.log("down");
}//向下的函数
function up(){
	var i;
	for(i=0;i<3;i++){
		$(".block").eq(i).children().eq(0).children().eq(0).attr("src","/static/img/huang.png")
	}//改变三个圈
	if(point_hua==1){
		$(".back_ground").animate({height:0.7*$(window).height()},1000);
		$(".head").css({"background-color":"transparent","opacity":"0"});
		$(".head").animate({opacity:"1"},1000);
		$(".menu-item a").css({"color":"white"});
		$(".nav .logoandlink h2").css({"color":"white"});
		$(".intro_detail").height(0.7*$(window).height());
		// $(".back_ground").not(".name_main").animate({bottom:0.7*$(window).height()},1000);
		$(".short_intro").animate({height:0.299*$(window).height()},1000,function(){mi=0;});
		// $(".intro_detail").css({"height",0.7*H})
		$(".block p").css({"display":"inline"})
		point_hua=0;
		$(".qixiang").animate({bottom:"20px",opacity:"0.6"},500);
		$(".jingzhun").animate({bottom:"20px",opacity:"0.6"},500);
		$(".youxiu").animate({bottom:"20px",opacity:"0.6"},500);
	}
	console.log("up");
}//向上的函数
$(".block").click(function(){
	down();
	$(this).children().eq(0).children().eq(0).attr("src","/static/img/cahui.png");
	if($(this).hasClass("imagine")){
		$(".qixiang").css("display","block");
		$(".jingzhun").css("display","none");
		$(".youxiu").css("display","none");
		$(".qixiang").animate({bottom:"0px",opacity:"0.85"},500);
		$(".jingzhun").animate({bottom:"20px",opacity:"0.6"},500);
		$(".youxiu").animate({bottom:"20px",opacity:"0.6"},500);
	}
	else if($(this).hasClass("analyze")){
		$(".qixiang").css("display","none");
		$(".jingzhun").css("display","block");
		$(".youxiu").css("display","none");
		$(".qixiang").animate({bottom:"20px",opacity:"0.6"},500);
		$(".jingzhun").animate({bottom:"0px",opacity:"0.85"},500);
		$(".youxiu").animate({bottom:"20px",opacity:"0.6"},500);
	}
	else if($(this).hasClass("team")){
		$(".qixiang").css("display","none");
		$(".jingzhun").css("display","none");
		$(".youxiu").css("display","block");
		$(".qixiang").animate({bottom:"20px",opacity:"0.6"},500);
		$(".jingzhun").animate({bottom:"20px",opacity:"0.6"},500);
		$(".youxiu").animate({bottom:"0px",opacity:"0.85"},500);
	}
});//如果点击，改变三个圈的样式

$(window).bind('mousewheel', function(event, delta) {  
        if(delta==-1&&point_hua==0&&mi==0){
        	down();
        	console.log("-1");
          	$(".imagine").children().eq(0).children().eq(0).attr("src","/static/img/cahui.png");
			$(".qixiang").css("display","block");
			$(".jingzhun").css("display","none");
			$(".youxiu").css("display","none");
			$(".qixiang").animate({bottom:"0px",opacity:"0.85"},500);
        }//向下滚动
        else if(delta==1&&point_hua==1&&mi==1){
        	up();
        	console.log("1");
        }//向上滚动
}); //滚轮事件
		

$(document).ready(function (){
	$(".menu").children().eq(1).addClass("nowpage");
	localwee();
	var liuxing_top=$(".liuxing").css("top");
	liuxing_top=parseInt(liuxing_top);
	var liuxing_left=$(".liuxing").css("left");
	liuxing_left=parseInt(liuxing_left);
	var touming=$(".liuxing").css("opacity");
	touming=parseInt(touming);
	
	var flag=0;
	var xiu=setInterval(function(){
		liuxing_top+=5;
		liuxing_left-=5;
		if(touming>=1){
			flag=1;
		}
		if(flag==0){
			touming+=0.1;
		}
		else if(flag==1){
			touming-=0.05;
		}
		$(".liuxing").css({"left":liuxing_left+"px","top":liuxing_top+"px","opacity":touming})
		if(touming<=0){
			clearInterval(xiu);
		}
	},50)
});//刘星

var allInterval=[],isFlashing=[],sw,sh; // screenwidth and screenheight;

function localwee(){
	var timeout = setTimeout(function(){
		window.clearInterval(allInterval[".wee"]);
		isFlashing[".wee"]=false;
		var left = $('.nowpage').position().left + 10;
		var width = $('.nowpage').width();
		//console.log(width);
		//console.log(left);
		$('.wee').css({ 'left': left , 'width': width });
	},100);
}

$(window).on('load', function() {
    sw = $('.container').width();
	sh = $('.container').height();
});

$(window).on('resize', function() {
    sw = $('.container').width();
	sh = $('.container').height();
	// window.clearInterval(allInterval['.wee']);
	localwee();
});

function slideFlash(handle,aimLeft,aimTop,aimWidth,aimHeight){  // top left 都是相对父元素的 fps是帧率
	fps=50;
	var startLeft=$(handle).position().left;
	var startTop=$(handle).position().top;
	var startWidth=$(handle).width();
	var startHeight=$(handle).height();
	var startsw=sw,startsh=sh;
	window.clearInterval(allInterval[handle]);
	isFlashing[handle]=true;
	allInterval[handle]=window.setInterval(flash,750/fps);
	var i=0;
	function flash() {
		i++;
		var nowLeft = (aimLeft - startLeft) * Math.cos(Math.PI / 2 * i / fps - Math.PI / 2) + startLeft;
		var nowTop = (aimTop - startTop) * Math.cos(Math.PI / 2 * i / fps - Math.PI / 2) + startTop;
		var nowWidth = (aimWidth - startWidth) * Math.cos(Math.PI / 2 * i / fps - Math.PI / 2) + startWidth;
		var nowHeight = (aimHeight - startHeight) * Math.cos(Math.PI / 2 * i / fps - Math.PI / 2) + startHeight;
		// if (i<20) console.log(i, (aimLeft - startLeft) * Math.cos(Math.PI / 2 * i / fps - Math.PI / 2));
		$(handle).css({'left': nowLeft*sw/startsw , 'top': nowTop*sh/startsh , 'width': nowWidth*sw/startsw , 'height': nowHeight*sh/startsh });
		if (i===fps){
			isFlashing[handle]=false;
			window.clearInterval(allInterval[handle]);
		}
    }
}

$('.menu-item').hover(function() {
	var aimLeft = $(this).position().left + 10;
	var aimWidth = $(this).width();

	var aimTop=$('.wee').offset().top;
	var aimHeight=2;
	slideFlash('.wee',aimLeft,aimTop,aimWidth,aimHeight);
}, function() {
	var aimLeft = $('.nowpage').position().left + 10;
	var aimWidth = $('.nowpage').width();
	var aimTop=$('.wee').offset().top;
	var aimHeight=2;
	slideFlash('.wee',aimLeft,aimTop,aimWidth,aimHeight);
});

// // $(document).ready(function() {
//   // cool nav menu
//   $(window).on('load resize', function() {
//     var $thisnav = $('.current-menu-item').offset().left;
//     $('.menu-item').hover(function() {
//       var $left = $(this).offset().left - $thisnav;
//       var $width = $(this).outerWidth();
//       var $start = 0;
//       $('.wee').css({ 'left': $left+10 , 'width': $width-20 });
//     }, function() {
//       var $initwidth = $('.current-menu-item').width();
//       $('.wee').css({ 'left': '10px' , 'width': $initwidth });
//     });
//   });


// // });