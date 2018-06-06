$(".about_us").click(function(){
	$(".name").css("display","none");
	$(".team_intro").css("display","block");
})
$(".return_home").click(function(){
	$(".name").css("display","block");
	$(".team_intro").css("display","none");
})
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
			change_home(W,H);
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
	var temp=0.05*H;
	temp=temp+"px";
	// temp=0.3*H；
	$(".name_main").css("margin-top",temp);
	$(".in_center").height(0.3*H);
	// $(".intro_detail").height(0.7*H);
	$(".about_us h2").css({"margin-top":0.01*H,"margin-bottom":0.01*H})
	$(".block").css({"margin-top":0.035*H})
	$(".short_intro").height(0.299*H);
}

var point_hua=0;
function down(){
	var i;
	for(i=0;i<3;i++){
		$(".block").eq(i).children().eq(0).children().eq(0).attr("src","./img./jj.png")
	}

	if(point_hua==0){
		$(".back_ground").animate({height:$(".head").css("height")},1000);
		$(".head").css({"background-color":"white","opacity":"0"});
		$(".head").animate({opacity:"1"},1000);
		$(".menu-item a").css({"color":"black"});
		$(".back_ground .head .center h2").css({"color":"black"});
		$(".intro_detail").height(0.6*$(window).height());
		// $(".back_ground").not(".name_main").animate({bottom:0.7*$(window).height()},1000);
		$(".short_intro").animate({height:0.999*$(window).height()-parseInt($(".head").css("height"))},1000);
		// $(".intro_detail").css({"height",0.7*H})

		console.log($(".intro_detail").height());
		point_hua=1;
	}
	$(".block p").css({"display":"none"})
	
}
function up(){
	var i;
	for(i=0;i<3;i++){
		$(".block").eq(i).children().eq(0).children().eq(0).attr("src","./img./jj.png")
	}
	if(point_hua==1){
		$(".back_ground").animate({height:0.7*$(window).height()},1000);
		$(".head").css({"background-color":"transparent","opacity":"0"});
		$(".head").animate({opacity:"1"},1000);
		$(".menu-item a").css({"color":"white"});
		$(".back_ground .head .center h2").css({"color":"white"});
		$(".intro_detail").height(0.7*$(window).height());
		// $(".back_ground").not(".name_main").animate({bottom:0.7*$(window).height()},1000);
		$(".short_intro").animate({height:0.299*$(window).height()},1000);
		// $(".intro_detail").css({"height",0.7*H})
		$(".block p").css({"display":"inline"})
		console.log($(".intro_detail").height());
		point_hua=0;
	}
}
$(".block").click(function(){
	down();
	$(this).children().eq(0).children().eq(0).attr("src","./img./cahui.png");
	if($(this).hasClass("imagine")){
		$(".qixiang").css("display","block");
		$(".jingzhun").css("display","none");
		$(".youxiu").css("display","none");
	}
	else if($(this).hasClass("analyze")){
		$(".qixiang").css("display","none");
		$(".jingzhun").css("display","block");
		$(".youxiu").css("display","none");
	}
	else if($(this).hasClass("team")){
		$(".qixiang").css("display","none");
		$(".jingzhun").css("display","none");
		$(".youxiu").css("display","block");
	}
});//如果点击

$(window).bind('mousewheel', function(event, delta) {  
        if(delta==-1&&point_hua==0){
        	down();
        	$(".imagine").children().eq(0).children().eq(0).attr("src","./img./cahui.png");
			$(".qixiang").css("display","block");
			$(".jingzhun").css("display","none");
			$(".youxiu").css("display","none");
        }
        else if(delta==1){
        	up();
        }
}); //滚轮事件
		

// $(document).ready(function() {
  // cool nav menu
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
  });


// });