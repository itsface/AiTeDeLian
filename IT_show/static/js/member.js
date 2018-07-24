var H, W;

H = $(window).height(); //获得窗口宽度
W = $(window).width(); //获得窗口高度
$(window).resize(function() { //浏览器缩放重新获得窗口宽高
	H = $(window).height();
	W = $(window).width();
	change_member(W, H);
	var ah = $(".member_block").height();
	var aw = $(".member_block").width();
	var b = $(".bselect").index('.member_block');
	var m = $(".amount input").eq(b).val() - 0;
	turn_h = $(".turn_page").height();
	turn_w = 0.25 * aw;
	var c = $(".ballselect").index('.qiu')
	if (b != -1) {
		$(".turn_page").eq(b).css({
			left: (aw - m * 0.25 * turn_w) / 2 + "px"
		});
	}
	if (c != -1) {
		// $(".qiu").height(0.12 * turn_w);
		// $(".qiu").width(0.12 * turn_w);
		// $(".qiu").css({
		// 	"top": 0.3 * turn_h + "px",
		// 	"left": ($(".page").width() - $(".qiu").width()) / 2 + "px"
		// });
		$(".ballselect").find('img').css({
			'width': 0.15 * turn_w + 'px',
			'height': 'auto',
			"top": 0.27 * turn_h + "px",
			"left": ($(".page").width() - $(".qiu").width()) / 2 - 0.015 * turn_w + "px"

		})
		$(".ballselect").siblings('.page').find('img').css({
			'width': 0.12 * turn_w + 'px',
			'height': 'auto',
			"top": 0.3 * turn_h + "px",
			"left": ($(".page").width() - $(".qiu").width()) / 2 + "px"
		})
	}

});
change_member(W, H);

$(".turn_page").addClass('clearfix3')
var turn_h;
var turn_w;
var flag = 0;
var n, x = 0;

function change_member(W, H) {
	$(".container").height(H);
	$(".star").width(0.8 * W);
	$(".star").css({
		"left": 0.1 * W + "px",
		"top": 0.12 * H + "px"
	})
	$(".member_show").css({
		"margin-top": 0.13 * H + "px"
	})
	$(".main").width(0.5 * W);
	$(".time_star").width($(".main").width());
	$(".main").height($(".time_star").height());
	$(".main").css({
		"top": (H - $(".main").height()) / 2 + 50 + "px",
		"left": (W - $(".main").width()) / 2 + "px"
	})
	var x = $(".main").width();
	var y = $(".main").height();
	$(".quan").css({
		"width": 0.09 * x + "px",
		"height": 0.09 * x + "px"
	})
	$(".quan2011").css({
		"left": 0.001 * x + "px",
		"top": 0.36 * y + "px"
	})
	$(".quan2012").css({
		"left": 0.142 * x + "px",
		"top": 0.08 * y + "px"
	})
	$(".quan2013").css({
		"left": 0.31 * x + "px",
		"top": 0.60 * y + "px"
	})
	$(".quan2014").css({
		"left": 0.455 * x + "px",
		"top": 0.278 * y + "px"
	})
	$(".quan2015").css({
		"left": 0.61 * x + "px",
		"top": 0.01 * y + "px"
	})
	$(".quan2016").css({
		"left": 0.754 * x + "px",
		"top": 0.4 * y + "px"
	})
	$(".quan2017").css({
		"left": 0.91 * x + "px",
		"top": 0.246 * y + "px"
	})
	$(".member_block").height(0.5 * W / 1.86);
	$(".member_block").width(0.5 * W);
	$(".member_block").css({
		"top": (H - $(".member_block").height()) / 2 + 50 + "px",
		"left": (W - $(".member_block").width()) / 2 + "px"
	})
	var ah = $(".member_block").height();
	var aw = $(".member_block").width();
	$(".lunbo").width(0.8 * aw);
	$(".lunbo").height(0.6 * ah);
	$(".lunbo").css({
		"top": (ah - $(".lunbo").height()) / 2 + "px",
		"left": (aw - $(".lunbo").width()) / 2 + "px"
	});
	$(".grade").css({
		"left": (aw - $(".lunbo").width()) / 2 + "px",
		"margin-top": 0.06 * ah + "px"
	});
	$(".turnleft_row").width(0.02 * aw + "px");
	$(".turnright_row").width(0.02 * aw + "px");
	$(".turnleft_row").css({
		"top": (ah - $(".turnleft_row").height()) / 2 + "px",
		"left": 0.02 * aw + "px"
	});
	$(".turnright_row").css({
		"top": (ah - $(".turnright_row").height()) / 2 + "px",
		"right": 0.02 * aw + "px"
	});
	$(".turn_page").height(0.14 * ah);
	// $(".turn_page").width();
	$(".turn_page").css({
		"bottom": 0.02 * ah + "px",
		left: (aw - $(".turn_page").width()) / 2 + "px"
	});
	turn_h = $(".turn_page").height();
	turn_w = 0.25 * aw;
	$(".page").width(0.2 * turn_w);
	$(".page").height(turn_h);
	$(".page").css({
		"margin-right": 0.05 * turn_w + "px"
	});

	$(".member2016_block .turn_page").width(0.3 * aw);
	$(".member2016_block .turn_page .page").css({
		"margin-right": 0.04 * turn_w + "px"
	});
	$(".member2016_block .turn_page .qiu").css({
		"top": 0.3 * turn_h + "px",
		"left": ($(".page").width() - $(".qiu").width()) / 2 + "px"
	});


	var bh = $(".lunbo").height();
	var bw = $(".lunbo").width();
	$(".boy").height(bh);
	$(".boy").width(0.266 * bw);
	$(".boy").css({
		"margin-right": 0.1 * bw + "px"
	});
	$(".portrait").width($(".boy").width());
	$(".portrait").height($(".boy").width());
	$(".cover").width(0.6 * $(".portrait").width());
	$(".cover").height(0.6 * $(".portrait").width());
	$(".cover").css({
		"padding": 0.2 * $(".portrait").width() + "px"
	})
	$(".name").css({
		"line-height": 0.2 * bh + "px"
	})
	$(".department").css({
		"line-height": 0.1 * bh + "px"
	})
}

// $(window).on('load resize', function() {
// 	// var $thisnav = $('.current-menu-item').offset().left;
// 	$('.menu-item').hover(function() {
// 		var $left = $(this).offset().left - $thisnav;
// 		var $width = $(this).outerWidth();
// 		var $start = 0;
// 		$('.wee').css({
// 			'left': $left + 10,
// 			'width': $width - 20
// 		});
// 	}, function() {
// 		var $initwidth = $('.current-menu-item').width();
// 		$('.wee').css({
// 			'left': '10px',
// 			'width': $initwidth
// 		});
// 	});
// }); //滑块
$(document).ready(function() {
	$(".menu").children().eq(5).addClass("nowpage");
	localwee();
	$(".float").animate({
		left: $(".container").width() + "px"
	}, 2500);
});
$(".portrait").hover(function() {
	$(this).children().eq(1).css({
		"display": "block"
	})
}, function() {
	$(this).children().eq(1).css({
		"display": "none"
	})
})


$(".quan").click(function() {

	var a = $(".quan").index(this);
	var aw = $(".member_block").width();
	var m = $(".amount input").eq(a).val() - 0;
	console.log($(".turn_page").eq(a).width())
	$(".member_block").css({
		"display": "none"
	});
	$(".member_block").eq(a).css({
		"opacity": "0",
		"display": "block"
	});
	$(".member_block").eq(a).animate({
		opacity: "1"
	}, 700)
	$(".member_block").eq(a).addClass('bselect');
	$(".bselect .turn_page").addClass('tselect');
	ballchange($(".tselect .page").eq(x))
	$(".turn_page").eq(a).css({
		left: (aw - m * 0.25 * turn_w) / 2 + "px"
	});


})
$(".cha").click(function() {
	$(".member_block").animate({
		opacity: "0"
	}, 700, function() {
		disappear()
		$(".turn_page").removeClass('tselect');
		$(".page").removeClass('ballselect');
		$(".member_block").removeClass('bselect');
	})

	x = 0;
	$()
})


y = 0; //x 记录当前页的,y记录被点击页


function disappear() {
	$(".member_block").css({
		"display": "none"
	})
	$(".long").css({
		"left": "0px"
	});
	$(".ballselect").find('img').css({
		'width': 0.12 * turn_w + 'px',
		'height': 'auto',
		"top": 0.3 * turn_h + "px",
		"left": ($(".page").width() - $(".qiu").width()) / 2 + "px"
	})
	flag = 0;
}
var page = new Array();
var str = ['', '', '', '', '', '', ''];

function inilize()

{

	for (var i = 0; i < 7; i++) {

		page[i] = $(".amount input").eq(i).val() - 0;

		for (var j = 1, m = page[i] + 1; j < m; j++) {
			//ES6

			// str[i] +=
			// 	`<div class="page` + j + ` page">
			//                       <img src="./static/img/page` + j + `.png" class="qiu` + j + ` qiu">
			//               </div>

			// `

			str[i] += "<div class=\"page" + j + " page\">\n\t                        <img src=\"/static/img/page" + j + ".png\" class=\"qiu" + j + " qiu\">\n\t                </div>\n\t                \n\t\t\t";

		}
		$(".turn_page").eq(i).append(str[i]);
	}
	$(".page").width(0.2 * turn_w);
	$(".page").height(turn_h);
	$(".page").css({
		"margin-right": 0.05 * turn_w + "px"
	});
	// ballchange($(".tselect .page").eq(0))


}

inilize();



function ballchange(_this) {
	if (flag == 0) {


		$sel = $(_this).parent();

		$(_this).addClass("ballselect")
		$(_this).siblings('.page').removeClass("ballselect");
		// $(_this).parent().addClass('tselect');
		$(".turn_page").not($sel).removeClass("tselect");
		$(".ballselect").find('img').css({
			'width': 0.15 * turn_w + 'px',
			'height': 'auto',
			"top": 0.27 * turn_h + "px",
			"left": ($(".page").width() - $(".qiu").width()) / 2 - 0.015 * turn_w + "px"

		})
		$(".ballselect").siblings('.page').find('img').css({
			'width': 0.12 * turn_w + 'px',
			'height': 'auto',
			"top": 0.3 * turn_h + "px",
			"left": ($(".page").width() - $(".qiu").width()) / 2 + "px"
		})
		y = $(".tselect .page").index(_this);
		var left = parseInt($(".tselect").siblings('.lunbo').children().eq(0).css("left"));

		flag = 1;
		// $(".tselect .page,.bselect .turnleft,.bselect .turnright").attr('disabled', 'true');
		// setTimeout(function() {
		// 	$(".tselect .page,.bselect .turnleft,.bselect .turnright").removeAttr('disabled')
		// }, 1500);
		$(".tselect").siblings('.lunbo').children().eq(0).animate({
			left: left - (y - x) * ($(".lunbo").width() + 0.1 * $(".lunbo").width()) + "px"
		}, 1000, function() {
			flag = 0;
		})
		x = y;
	}

}
$(window).resize(function() {

	$(".tselect").siblings('.lunbo').children().eq(0).css({
		left: - x * ($(".lunbo").width() + 0.1 * $(".lunbo").width()) + "px"
	})
	console.log($(".lunbo").width() )
})

$(".page").click(function(event) {

	ballchange(this)
});

function toleft(_this) {
	if (flag == 0) {


		if (x > 0) {
			y--;
			ballchange($(_this).siblings('.turn_page').children().eq(y))
			x = y;
		}


	}

}

function toright(_this) {
	if (flag == 0) {
		var b = $(".bselect").index('.member_block');
		var c = $(".amount input").eq(b).val() - 0;
		if (x < c - 1) {
			y++;
			ballchange($(_this).siblings('.turn_page').children().eq(y))
			x = y;
			console.log(x)
		}
	}

}
$(".turnleft").click(function() {
	toleft(this)
});
$(".turnright").click(function(event) {
	toright(this)
});