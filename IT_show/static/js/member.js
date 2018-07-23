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
			change_member(W, H);
		});
		change_member(W, H);
	} else { //如果不是ie7，然而我还没写

	}
})
$(".turn_page").addClass('clearfix3')
var turn_h;
var turn_w;
var flag = 0;
var n, x = 0;
var page = new Array();
var str = ['', '', '', '', '', '', ''];
inilize();

function change_member(W, H) {
	$(".container").height(H);
	$(".star").width(0.8 * W);
	$(".star").css({
		"left": 0.1 * W + "px",
		"top": 0.12 * H + "px"
	})
	$(".member_show").css({
		"margin-top": 0.05 * H + "px"
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
	$(".member_block").height(0.6 * H);
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
	turn_w = 0.25*aw;
	$(".page").width(0.2 * turn_w);
	$(".page").height(turn_h);
	$(".page").css({
		"margin-right": 0.05 * turn_w + "px"
	});
	$(".qiu").height(0.12 * turn_w);
	$(".qiu").width(0.12 * turn_w);
	$(".uprow").width(0.1 * turn_w);
	$(".downrow").width(0.1 * turn_w);
	$(".qiu").css({
		"top": 0.3 * turn_h + "px",
		"left": ($(".page").width() - $(".qiu").width()) / 2 + "px"
	});
	$(".uprow").css({
		"top": 0.01 * turn_h + "px",
		"left": ($(".page").width() - $(".uprow").width()) / 2 + "px"
	});
	$(".downrow").css({
		"top": 0.827 * turn_h + "px",
		"left": ($(".page").width() - $(".uprow").width()) / 2 + "px"
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

$(window).on('load resize', function() {
	var $thisnav = $('.current-menu-item').offset().left;
	$('.menu-item').hover(function() {
		var $left = $(this).offset().left - $thisnav;
		var $width = $(this).outerWidth();
		var $start = 0;
		$('.wee').css({
			'left': $left + 10,
			'width': $width - 20
		});
	}, function() {
		var $initwidth = $('.current-menu-item').width();
		$('.wee').css({
			'left': '10px',
			'width': $initwidth
		});
	});
}); //滑块
$(document).ready(function() {
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


$(".quan").click(function(){
	for (var i=1;i<=7;i++){
		var showHandle = ".show"+i.toString();
		if ($(this).hasClass("quan"+(i+2010).toString())){
			$(".member_block").css({
				"display": "none"
			});
			$(".member"+(i+2010).toString()+"_block").css({
				"opacity": "0",
				"display": "block"
			});
			$(".member"+(i+2010).toString()+"_block").animate({
				opacity: "1"
			}, 700)
		}
	}
}
)

$(".cha").click(function() {
	$(".member_block").animate({
		opacity: "0"
	}, 700, function() {
		disappear()
	})
	$(".turn_page").removeClass('tselect');
	$(".page").removeClass('ballselect');
	x =0;
})


	y = 0; //x 记录当前页的,y记录被点击页
var point2012 = 1,
	point2013 = 1,
	point2014 = 1,
	point2015 = 1,
	point2016 = 1,
	point2017 = 1;

var point=new Array();
for (var i = 0; i < 7; i++) {
	point[i]=1;
}
function disappear() {
	$(".member_block").css({
		"display": "none"
	})
	$(".long").css({
		"left": "0px"
	});
	flag = 0;
	point2012 = 1;
	point2013 = 1;
	point2014 = 1;
	point2015 = 1;
	point2016 = 1;
	point2017 = 1;
	$(".page1 .uprow").css({
		"display": "block"
	});
	$(".page1 .downrow").css({
		"display": "block"
	});
	$(".page2 .uprow").css({
		"display": "none"
	});
	$(".page2 .downrow").css({
		"display": "none"
	});
	$(".page3 .uprow").css({
		"display": "none"
	});
	$(".page3 .downrow").css({
		"display": "none"
	});
	$(".page4 .uprow").css({
		"display": "none"
	});
	$(".page4 .downrow").css({
		"display": "none"
	});
	$(".page2 .uprow").css({
		"display": "none"
	});
	$(".page2 .downrow").css({
		"display": "none"
	});
}
$(".turnright").click(function() {
	for (var t = 0; t < 7; t++) {
		var memberBlockStr="member"+(t+2011).toString()+"_block"
		if ($(this).parent().hasClass(memberBlockStr) && point[t] < page[t] && flag == 0){
			var left = parseInt($(this).parent().children().eq(4).children().eq(0).css("left"));
			flag = 1;
			$(this).parent().children().eq(4).children().eq(0).animate({
				left: left - $(".lunbo").width() - 0.1 * $(".lunbo").width() + "px"
			}, 1000, function() {
				flag = 0;
			})
			point[t] += 1;
			var i = 0;
			for (i = 0; i < 3; i++) {
				$(this).parent().children().eq(5).children().eq(i).children().eq(1).css({
					"display": "none"
				});
				$(this).parent().children().eq(5).children().eq(i).children().eq(2).css({
					"display": "none"
				});
			}
			$(this).parent().children().eq(5).children().eq(point[t] - 1).children().eq(1).css({
				"display": "block"
			});
			$(this).parent().children().eq(5).children().eq(point[t] - 1).children().eq(2).css({
				"display": "block"
			});
			break;
		}
	}
})

$(".turnleft").click(function() {
	for (var t = 0; t < 7; t++) {
		var memberBlockStr="member"+(t+2011).toString()+"_block"
		if ($(this).parent().hasClass(memberBlockStr) && point[t] >1 && flag == 0){
			var left = parseInt($(this).parent().children().eq(4).children().eq(0).css("left"));
			flag = 1;
			$(this).parent().children().eq(4).children().eq(0).animate({
				left: left + $(".lunbo").width() + 0.1 * $(".lunbo").width() + "px"
			}, 1000, function() {
				flag = 0;
			})
			point[t] -= 1;
			var i = 0;
			for (i = 0; i < 3; i++) {
				$(this).parent().children().eq(5).children().eq(i).children().eq(1).css({
					"display": "none"
				});
				$(this).parent().children().eq(5).children().eq(i).children().eq(2).css({
					"display": "none"
				});
			}
			$(this).parent().children().eq(5).children().eq(point[t] - 1).children().eq(1).css({
				"display": "block"
			});
			$(this).parent().children().eq(5).children().eq(point[t] - 1).children().eq(2).css({
				"display": "block"
			});
		}
	}
	break;
})



function inilize()

{

	for (var i = 0; i < 7; i++) {

		page[i] = $(".amount input").eq(i).val() - 0;

		for (var j = 1, m =page[i]+1; j < m; j++) {
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


}





function ballchange(_this){
	// if($(_this).parent().hasClass('tselect') =='false')
	// {
	// 	x=0;
	// }
	$sel = $(_this).parent();

	$(_this).addClass("ballselect")
	$(_this).siblings('.page').removeClass("ballselect");
	$(_this).parent().addClass('tselect');
	$(".turn_page").not($sel).removeClass("tselect");
	$(".ballselect").find('img').css({
		'width': 0.15 * turn_w + 'px',
		'height': 'auto',
		"top": 0.27 * turn_h + "px",
		"left": ($(".page").width() - $(".qiu").width()) / 2 - 0.015* turn_w + "px"

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
		$(".tselect").siblings('.lunbo').children().eq(0).animate({
			left: left - (y - x) * ($(".lunbo").width() + 0.1 * $(".lunbo").width()) + "px"
		}, 1000, function() {
			flag = 0;
		})
	x = y;

}
$(".page").click(function(event) {

	ballchange(this)
});	

function toleft()
{
	

}

