$(document).ready(function() {
	$(".menu").children().eq(1).addClass("current-menu-item")

    var $thisnav = $('.current-menu-item').offset().left-$('.x').offset().left;
	var $initwidth = $('.current-menu-item').width();
      $('.wee').css({ 'left': $thisnav+10+'px' , 'width': $initwidth });
})
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
// let appr = 0.53 * W;
// var programr = 0.42 * W;
$front = $(".ball .front_end");
$ui = $(".ball .ui")
$program = $(".program");
$app = $(".app");
$baller = $(".baller")
if ($.browser.version != "7.0") //判断是不是IE7 ，IE7下不支持“$(window).width()”
{
	H = $(window).height(); //获得窗口宽度
	W = $(window).width(); //获得窗口高度

	$(window).resize(function() { //浏览器缩放重新获得窗口宽高
		H = $(window).height();
		W = $(window).width();

	});

	$(".container").height(H);
	$(".container").width(W);
	$front.css({
		'height': 0.088 * W,
		'top': 0.215 * W
	})
	$ui.css({
		'height': 0.0906 * W,
		'top': 0.276 * W
	})
	$program.css({
		'height': 0.0906 * W,
		'top': 0.122 * W
	})
	$app.css({
		'height': 0.0906 * W,
		'top': 0.2502 * W
	})

	$("h1").css({
		'top': 0.045 * W
	})
	$(".back").css({
		'height': H
	})
	$(".depart_intro .front_end").css({
		'margin-top': -0.157 * 0.802 * H,
		'height': 0.1822*W
	})
	$(".depart_intro .front_end h3").css({
		'margin-top': 0.175 * 0.324 * H,
		'margin-bottom': 0.132* 0.324 * H
	})
	$(".depart_intro .front_end .close").css({
		'top': 0.030 * 0.324 * H,
		'right': 0.057 * 0.324 * H
	})
	$(".depart_intro .app").css({
		// 'margin-top': -0.157 * 0.802 * H,
		'height': 0.1822*W,
		'bottom': 0.292 * 0.324 * H
	})
	$(".depart_intro .app h3").css({
		'margin-top': 0.175 * 0.324 * H,
		'margin-bottom': 0.132* 0.324 * H
	})
	$(".depart_intro .app .close").css({
		'top': 0.030 * 0.324 * H,
		'right': 0.057 * 0.324 * H
	})
	$(".depart_intro .ui").css({
		'margin-top': -0.157 * 0.802 * H,
		'height': 0.1822*W
	})
	$(".depart_intro .ui h3").css({
		'margin-top': 0.175 * 0.324 * H,
		'margin-bottom': 0.132* 0.324 * H
	})
	$(".depart_intro .ui .close").css({
		'top': 0.030 * 0.324 * H,
		'right': 0.057 * 0.324 * H
	})
	$(".depart_intro .program").css({
		'margin-top': -0.157 * 0.802 * H,
		'height': 0.1822*W
	})
	$(".depart_intro .program h3").css({
		'margin-top': 0.175 * 0.324 * H,
		'margin-bottom': 0.132* 0.324 * H
	})
	$(".depart_intro .program .close").css({
		'top': 0.030 * 0.324 * H,
		'right': 0.057 * 0.324 * H
	})

	// balloval2(0.30, 0.65, programr, programr);
	// if(W>1700 && W<=1920){
	// 	appr = 0.53 * W;
	// 	programr = 0.42*W;
	// 	balloval2(0.30, 0.65, programr, programr);
	// }

	// else if(W<=1700 && W>1500){
	// 	programr = 0.42*W;
	// 	balloval2(0.30, 0.60, programr, programr);
	// }
	// else if(W<=1500 && W>980){
	// 	programr = 0.42*W;
	// 	balloval2(0.30, 0.60, programr, programr);
	// }



	$(window).resize(function() { //浏览器缩放重新获得窗口宽高
		$(".container").height(H);
	$(".container").width(W);
	$front.css({
		'height': 0.088 * W,
		'top': 0.215 * W
	})
	$ui.css({
		'height': 0.0906 * W,
		'top': 0.276 * W
	})
	$program.css({
		'height': 0.0906 * W,
		'top': 0.122 * W
	})
	$app.css({
		'height': 0.0906 * W,
		'top': 0.2502 * W
	})

	$("h1").css({
		'top': 0.045 * W
	})
	$(".back").css({
		'height': H
	})
	$(".depart_intro .front_end").css({
		'margin-top': -0.157 * 0.802 * H,
		'height': 0.1822*W
	})
	$(".depart_intro .front_end h3").css({
		'margin-top': 0.175 * 0.324 * H,
		'margin-bottom': 0.132* 0.324 * H
	})
	$(".depart_intro .front_end .close").css({
		'top': 0.030 * 0.324 * H,
		'right': 0.057 * 0.324 * H
	})
	$(".depart_intro .app").css({
		// 'margin-top': -0.157 * 0.802 * H,
		'height': 0.1822*W,
		'bottom': 0.292 * 0.324 * H
	})
	// $(".depart_intro .app h3").css({
	// 	'margin-top': 0.175 * 0.324 * H,
	// 	'margin-bottom': 0.132* 0.324 * H
	// })
	$(".depart_intro .app .close").css({
		'top': 0.030 * 0.324 * H,
		'right': 0.057 * 0.324 * H
	})
	$(".depart_intro .ui").css({
		'margin-top': -0.157 * 0.802 * H,
		'height': 0.1822*W
	})
	$(".depart_intro .ui h3").css({
		'margin-top': 0.175 * 0.324 * H,
		'margin-bottom': 0.132* 0.324 * H
	})
	$(".depart_intro .ui .close").css({
		'top': 0.030 * 0.324 * H,
		'right': 0.057 * 0.324 * H
	})
	$(".depart_intro .program").css({
		'margin-top': -0.157 * 0.802 * H,
		'height': 0.1822*W
	})
	$(".depart_intro .program h3").css({
		'margin-top': 0.175 * 0.324 * H,
		'margin-bottom': 0.132* 0.324 * H
	})
	$(".depart_intro .program .close").css({
		'top': 0.030 * 0.324 * H,
		'right': 0.057 * 0.324 * H
	})

	})
} else {

}
let t1, t2, t3, t4, t5, t6, t7;
//ui小球运动函数
function balloval3(ballname, ox, oy, shorto, longo) {
	$ball = $(ballname);
	var y = parseInt($ball.css("top"));
	let originx = ox * W;
	let originy = oy * H;
	let short = shorto;
	let long = longo;
	let short2 = short * short;
	let long2 = long * long;
	let all = long2 * short2;
	let b = y;
	// console.log("orginx"+ox*W)
	t5 = setInterval(function() {
		// console.log($ball.css('left'));
		if (parseInt($ball.css('left')) < 0.49 * W) {
			clearInterval(t5);

			t6 = setInterval(function() {
				if (parseInt($ball.css('top')) > 0.58 * H) {
					clearInterval(t6);
					balloval3(ballname, ox, oy, shorto, longo);
				}
				b += 1;
				x = Math.sqrt((all - long2 * (b - originy) * (b - originy)) / short2);

				$ball.css({
					'top': b,
					'left': x + originx
				})
			}, 20)
		}
		b -= 1;
		x = Math.sqrt((all - long2 * (b - originy) * (b - originy)) / short2);

		$ball.css({
			'top': b,
			'left': x + originx
		})


		// console.log(x+short);
	}, 20)
}

// balloval3(".ball .ui", 0.30, 0.65, 0.27 * W, 0.27 * W);


//前端小球运动函数
function balloval1(ox, oy, shorto, longo) {
	// $ball = $(ballname);.
	var y = parseInt($(".front_end").css("top"));
	let originx = ox * W;
	let originy = oy * H;
	let short = shorto;
	let long = longo;
	let short2 = short * short;
	let long2 = long * long;
	let all = long2 * short2;
	let b = y;
	// console.log("orginx"+ox*W)
	t1 = setInterval(function() {
		// console.log($ball.css('left'));
		if (parseInt($(".ball .front_end").css('top')) > 0.53 * H) {
			clearInterval(t1);

			t2 = setInterval(function() {
				if (parseInt($(".ball .front_end").css('left')) < 0.36 * W) {
					clearInterval(t2);
					balloval1(ox, oy, shorto, longo);
				}
				b -= 1;
				x = Math.sqrt((all - long2 * (b - originy) * (b - originy)) / short2);


				$(".ball .front_end").css({
					'top': b,
					'left': x + originx
				})
			}, 20)
		}
		b += 1;
		x = Math.sqrt((all - long2 * (b - originy) * (b - originy)) / short2);

		$(".ball .front_end").css({
			'top': b,
			'left': x + originx
		})


		// console.log(x+short);
	}, 20)
}

// balloval1(0.25, 0.75, 0.24 * W, 0.19 * W);
//程序部门的小球
function balloval4(ox, oy, shorto, longo) {
	// $ball = $(ballname);
	let y = parseInt($(".ball .program").css("top"));
	let originx = ox * W;
	let originy = oy * H;
	let short = shorto;
	let long = longo;
	let short2 = short * short;
	let long2 = long * long;
	let all = long2 * short2;
	let b = y;
	// console.log("orginx"+ox*W)
	t7 = setInterval(function() {
		// console.log($(".program").css('left'));
		if (Ismovein == true) {
			clearInterval(t7);
		} else if (parseInt($(".ball .program").css('left')) < 0.66 * W) {
			clearInterval(t7);

			t8 = setInterval(function() {
				if (Ismovein == true) {
					clearInterval(t8);
				}
				if (parseInt($(".program").css('top')) > 0.55 * H) {
					clearInterval(t8);
					balloval4(ox, oy, shorto, longo);
				}
				b += 1;
				x = Math.sqrt((all - long2 * (b - originy) * (b - originy)) / short2);

				$(".ball .program").css({
					'top': b,
					'left': x + originx
				})
			}, 20)
		}
		b -= 1;
		x = Math.sqrt((all - long2 * (b - originy) * (b - originy)) / short2);

		$(".ball .program").css({
			'top': b,
			'left': x + originx
		})


		// console.log(x+short);
	}, 20)
}
// balloval4(0.30, 0.65, 0.42 * W, 0.42 * W);

//安卓部门的小球

function balloval2(ox, oy, shorto, longo) {

	var y = parseInt($(".ball .app").css("top"));
	let originx = ox * W;
	let originy = oy * H;
	let short = shorto;
	let long = longo;
	let short2 = short * short;
	let long2 = long * long;
	let all = long2 * short2;
	let b = y;
	// let move = 0;
	// console.log("orginx"+ox*W)
	t3 = setInterval(function() {
		// console.log($(".app").css('left'));
		if (parseInt($(".ball .app").css('left')) < 0.79 * W) {
			clearInterval(t3);

			t4 = setInterval(function() {
				if (parseInt($(".ball .app").css('top')) > 0.55 * H) {
					clearInterval(t4);
					balloval2(ox, oy, shorto, longo);
				}
				b += 1;
				x = Math.sqrt((all - long2 * (b - originy) * (b - originy)) / short2);

				$(".ball .app").css({
					'top': b,
					'left': x + originx
				})
			}, 20)
		}
		b -= 1;
		x = Math.sqrt((all - long2 * (b - originy) * (b - originy)) / short2);

		$(".ball .app").css({
			'top': b,
			'left': x + originx
		})



	}, 20)
}


// balloval2(0.50, 0.50, 0.33 * W, 0.34 * W);

// initialize();
function initialize() {
	$(".person").animate({
		'opacity': '1'
	}, 200, function() {
		$(".front_end").animate({
			'opacity': '1'
		}, 200, function() {
			$(".ui").animate({
				'opacity': '1'
			}, 200, function() {
				$(".program").animate({
					'opacity': '1'
				}, 200, function() {
					$(".app").animate({
						'opacity': '1'
					})
				})
			})
		})
	})
}


let Ismovein = [false, false, false, false];
let Isclick = [false, false, false, false];
let movedown = [false, false, false, false];
//balloval1(0.25, 0.75, 0.24 * W, 0.19 * W);
//balloval2(0.50, 0.50, 0.33 * W, 0.34 * W);
// balloval3(".ball .ui", 0.30, 0.65, 0.27 * W, 0.27 * W);
//balloval4(0.30, 0.65, 0.42 * W, 0.42 * W);


function startt(index) {
	if (index == 0) {
		clearInterval(t1);
		clearInterval(t2);
		balloval1(0.25, 0.75, 0.24 * W, 0.19 * W);
	} else if (index == 1) {
		clearInterval(t3);
		clearInterval(t4);
		balloval2(0.50, 0.50, 0.33 * W, 0.34 * W);
	} else if (index == 2) {
		clearInterval(t5);
		clearInterval(t6);
		balloval3(".ball .ui", 0.30, 0.65, 0.27 * W, 0.27 * W);
	} else if (index == 3) {
		clearInterval(t7);
		clearInterval(t8);
		balloval4(0.30, 0.65, 0.42 * W, 0.42 * W);
	}

}

function cleart(index) {
	if (index == 0) {
		clearInterval(t1);
		clearInterval(t2);

	} else if (index == 1) {
		clearInterval(t3);
		clearInterval(t4);

	} else if (index == 2) {
		clearInterval(t5);
		clearInterval(t6);

	} else if (index == 3) {
		clearInterval(t7);
		clearInterval(t8);

	}
}
//先停止上一次的动画
//鼠标移到星球上
$(".baller").mouseenter(function() {
	let index = $(".baller").index(this)
	$(".logo").eq(index).stop().animate({
		'opacity': '1'
	}, 200)
	$(".black").eq(index).stop().show();

	Ismovein[index] = true;
	// cleart(index);
});

//鼠标离开星球
$(".baller").mouseleave(function() {
	let index = $(".baller").index(this)
	$(".logo").eq(index).stop().animate({
		'opacity': '0'
	}, 200)
	$(".black").eq(index).stop().hide();

	if (Isclick[index] == false) {
		// startt(index);
	}
	Ismovein[index] = false;
});

$(".baller").click(function() {
	console.log("99")
	let index = $(".baller").index(this);
	$(".depart_intro .intro").eq(index).show();
	$(".depart_intro .intro").eq(index).animate({
		'opacity': '1'
	}, 200)
	Isclick[index] = true;
	// cleart(index);

})
//关闭介绍
$(".depart_intro .close").click(function() {
	let index = $(".depart_intro .close").index(this)
	$(".depart_intro .intro").eq(index).animate({
		'opacity': '0'
	}, 200, function() {
		$(".depart_intro .intro").eq(index).hide();
	})

	Isclick[index] = false;
	// startt(index);

});


//img记得控制高度
// ballrun();
// var ball = new Object();
// // function ballrun(){
// 	$ballee = $(".front_end")

// 	ball.y = parseInt($ballee.css('top'));
// 	ball.x = parseInt($ballee.css('left'));
// 	ball.originx = 0.30*W;
// 	ball.originy = 0.65*H;
// 	ball.v = 1;
// 	ball.r= 0.27*W;
// 	ball.w = parseInt($ballee.css('width'));
// 	ball.h = parseInt($ballee.css('height'));

// 	let t1 = setInterval(function(){
// 		// console.log("777")
// 		ball.x -=1;
// 		// ball.x = ball.r*Math.cos(ball.x-ball.originx)+ball.originx;
// 		ball.y = Math.sqrt();
// 		$ballee.css({
// 			'top':ball.y,
// 			'left':ball.x
// 		})
// 	},100)

// }".ui", 0.30, 0.65, 0.27 * W, 0.27 * W