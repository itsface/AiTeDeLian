// $(document).ready(function() {
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
let H2;
let write_top1,
	write_left1,
	boxh,
	boxw,
	button_w = 170,
	button_h = 51,
	box_top;
$write = $(".write");
if ($.browser.version != "7.0") //判断是不是IE7 ，IE7下不支持“$(window).width()”
{
	H = $(window).height(); //获得窗口宽度
	W = $(window).width(); //获得窗口高度
	H2 = $(".container_in").height();
	write_top1 = $(".make_comment").offset().top
	write_left1 = $(".make_comment").offset().left
	$(window).resize(function() { //浏览器缩放重新获得窗口宽高
		H = $(window).height();
		W = $(window).width();
		H2 = $(".container_in").height();
		write_top1 = $(".make_comment").offset().top
		write_left1 = $(".make_comment").offset().left
	});

	$(".container").height(H);
	$(".container").width(W);
	// $(".header h1").css({'margin-top':(H-H2)/2});
	$(".index_topic").height(H * 0.414);
	$(".index_topic").css({
		'margin-bottom': 0.041 * H,
		'margin-top': 0.027 * H
	})
	$(".comments").css({
		// 'min-height': 0.284 * H * 0.414,
		'margin-bottom': 0.067 * 0.414 * H,
		'min-height':0.066*W,

	})
	$(".comments .head").css({
		// 'height': 0.645*0.284 * H * 0.414,
		// 'margin-top': 0.27*0.645*0.284 * H * 0.414
		'height':0.0427*W,
		'margin-top':0.012*W
	})
	$(".make_comment").css({
		'height': 0.0266 * W,
		'line-height': 0.0266 * W + 'px'
	})
	$(".make_comment_wrap").css({
		'height': 0.0266 * W,
		'line-height': 0.0266 * W + 'px'
	})
	$(".comments .right").css({
		'margin-top': 0.125 * 0.284 * H * 0.414
	})
	$(".line").css({
		'margin-top': 0.025 * H
	})
	// $(".write").height(H*0.5);

	// if ((W - 0) > 1550) {
	// 	boxw = 1125;
	// 	box_top = 197.667;
	// } else if ((W - 0) > 1250 && (W - 0) < 1550) {
	// 	boxw = 985;

	// 	box_top = 187.667;
	// } else {
	// 	boxw = 956;
	// 	box_top = 177.667;
	// }
	boxw = parseInt($write.css('width'));
	boxh = parseInt($write.css('height'));

	//当年想要按比例缩放
	// $(".write textarea").css({
	// 	'height': 0.453 * 0.52 * H - 22
	// })
	// $(".write .text").css({
	// 	'height': 0.453 * 0.52 * H,
	// 	'margin-top':0.03*0.52*H
	// })
	// $(".write").css({
	// 	'height': 0.52 * H
	// })
	// $(".write .header").css({
	// 	'margin-top': 0.07 * 0.52 * H
	// })
	// $(".write .close").css({
	// 	'top': 0.0266 * 0.52 * H
	// })
	// $(".select_head").css({
	// 	'height': 0.129 * 0.52 * H
	// })
	// $(".write .left_arrow").css({
	// 	'margin-top': 0.046 * 0.52 * H
	// })
	// $(".write .head").css({
	// 	'height': 0.129 * 0.52 * H
	// })

	// $(".write .head img").css({
	// 	'height': 0.129 * 0.52 * H
	// })
	// $(".write .head_tip").css({
	// 	'margin-top':0.028*0.52*H
	// })
	// $(".write .id").css({
	// 	'height':0.076*0.52*H,
	// 	'margin-top':0.048*0.52*H
	// })
	// $(".write .id input").css({
	// 	'height':0.067*0.52*H
	// })
	// $(".write .id_tip").css({
	// 	'margin-top':0.028*0.52*H
	// })
	// $(".write .verify_tip").css({
	// 	'margin-top':0.028*0.52*H
	// })
	// $(".write .verify").css({
	// 	'height':0.064*0.52*H,
	// 	'margin-top':0.02*0.52*H
	// })
	// $(".write .verify input").css({
	// 	'height':0.056*0.52*H
	// })
	// $(".verify_img").css({
	// 	'height':0.071*0.52*H,
	// 	'margin-top':0.021*0.52*H
	// })
	// $(".verify_img img").css({
	// 	'height':0.071*0.52*H,
	// })
	// $(".write .submit").css({
	// 	'height':0.087*0.52*H,
	// 	'margin-top':0.0177*0.52*H,
	// 	'line-height':0.087*0.52*H+'px'
	// })
	// $(".text_tip").css({
	// 	'margin-top':0.028*0.52*H
	// })
	// $(".write .right_arrow").css({
	// 	'margin-top':0.046*0.52*H
	// })



	// boxw = $write.css('width');
	// boxh = 0.52 * H;

	$(window).resize(function() { //浏览器缩放重新获得窗口宽高
		$(".container").height(H);
	$(".container").width(W);
	// $(".header h1").css({'margin-top':(H-H2)/2});
	$(".index_topic").height(H * 0.414);
	$(".index_topic").css({
		'margin-bottom': 0.041 * H,
		'margin-top': 0.027 * H
	})
	$(".comments").css({
		// 'min-height': 0.284 * H * 0.414,
		'margin-bottom': 0.067 * 0.414 * H,
		'min-height':0.066*W,

	})
	$(".comments .head").css({
		// 'height': 0.645*0.284 * H * 0.414,
		// 'margin-top': 0.27*0.645*0.284 * H * 0.414
		'height':0.0427*W,
		'margin-top':0.012*W
	})
	$(".make_comment").css({
		'height': 0.0266 * W,
		'line-height': 0.0266 * W + 'px'
	})
	$(".make_comment_wrap").css({
		'height': 0.0266 * W,
		'line-height': 0.0266 * W + 'px'
	})
	$(".comments .right").css({
		'margin-top': 0.125 * 0.284 * H * 0.414
	})
	$(".line").css({
		'margin-top': 0.025 * H
	})
	// $(".write").height(H*0.5);

	// if ((W - 0) > 1550) {
	// 	boxw = 1125;
	// 	box_top = 197.667;
	// } else if ((W - 0) > 1250 && (W - 0) < 1550) {
	// 	boxw = 985;

	// 	box_top = 187.667;
	// } else {
	// 	boxw = 956;
	// 	box_top = 177.667;
	// }
	boxw = parseInt($(".index_topic").css('width'));
	boxh = parseInt($(".index_topic").css('height'));

		// boxw = $write.css('width');
		// boxh = 0.52 * H;
		// 	$(".write textarea").css({
		// 	'height': 0.453 * 0.52 * H - 22
		// })
		// $(".write .text").css({
		// 	'height': 0.453 * 0.52 * H,
		// 	'margin-top':0.03*0.52*H
		// })
		// $(".write").css({
		// 	'height': 0.52 * H
		// })
		// $(".write .header").css({
		// 	'margin-top': 0.07 * 0.52 * H
		// })
		// $(".write .close").css({
		// 	'top': 0.0266 * 0.52 * H
		// })
		// $(".select_head").css({
		// 	'height': 0.129 * 0.52 * H
		// })
		// $(".write .left_arrow").css({
		// 	'margin-top': 0.046 * 0.52 * H
		// })
		// $(".write .head").css({
		// 	'height': 0.129 * 0.52 * H
		// })

		// $(".write .head img").css({
		// 	'height': 0.129 * 0.52 * H
		// })
		// $(".write .head_tip").css({
		// 	'margin-top':0.028*0.52*H
		// })
		// $(".write .id").css({
		// 	'height':0.076*0.52*H,
		// 	'margin-top':0.048*0.52*H
		// })
		// $(".write .id input").css({
		// 	'height':0.067*0.52*H
		// })
		// $(".write .id_tip").css({
		// 	'margin-top':0.028*0.52*H
		// })
		// $(".write .verify_tip").css({
		// 	'margin-top':0.028*0.52*H
		// })
		// $(".write .verify").css({
		// 	'height':0.064*0.52*H,
		// 	'margin-top':0.02*0.52*H
		// })
		// $(".write .verify input").css({
		// 	'height':0.056*0.52*H
		// })
		// $(".verify_img").css({
		// 	'height':0.071*0.52*H,
		// 	'margin-top':0.021*0.52*H
		// })
		// $(".verify_img img").css({
		// 	'height':0.071*0.52*H,
		// })
		// $(".write .submit").css({
		// 	'height':0.087*0.52*H,
		// 	'margin-top':0.0177*0.52*H,
		// 	'line-height':0.087*0.52*H+'px',
		// })
		// $(".text_tip").css({
		// 	'margin-top':0.028*0.52*H
		// })
		// 	$(".write .right_arrow").css({
		// 	'margin-top':0.046*0.52*H
		// })
		// $(".write").height(H*0.5);

		// if ((W - 0) > 1550) {
		// 	boxw = 1125;
		// 	box_top = 197.667;
		// } else if ((W - 0) > 1250 && (W - 0) < 1550) {
		// 	boxw = 985;
		// 	box_top = 187.667;
		// } else {
		// 	boxw = 956;
		// 	box_top = 177.667;
		// }
		// boxh = $write.css('height');
		
	});

} else {

}

// })

let HEAD_SIZE = 3; //记录头像的个数
let headimg = 1; //默认显示第一个头像
$(".right_arrow").click(function() {
	if (headimg == HEAD_SIZE) {
		headimg -= HEAD_SIZE;
	}
	headimg++;
	headshow();
	console.log(headimg)

})
$(".left_arrow").click(function() {
	if (headimg == 0) {
		headimg += HEAD_SIZE;
	}
	headimg--;
	headshow();
	console.log(headimg)

})

//点击打开弹框，弹出发表评论框
//我先让评论框放到我要留言下面
// $write = $(".write");
// let write_top1 = $(".make_comment").offset().top,
// 	write_left1 = $(".make_comment").offset().left,
// 	boxh,
// 	boxw,
// 	box_top;

// if ((W - 0) > 1550) {
// 	boxw = 1125;
// 	box_top = 197.667;
// } else if ((W - 0) > 1250 && (W - 0) < 1550) {
// 	boxw = 985;
// 	box_top = 187.667;
// } else {
// 	boxw = 956;
// 	box_top = 177.667;
// }
// boxw = $write.css('width');
// boxh = $write.css('height');

// 点击我要留言后的展示效果
// $(".make_comment").click(function() {


// })
$(".make_comment").click(function() {
	boxw = parseInt($(".index_topic").css('width'));
	boxh = parseInt($(".index_topic").css('height'));
	//先把遮罩层放好位置
	// $(".writewrap").css({
	// 	'width': boxw,
	// 	'height': '562px',
	// 	'top': box_top,
	// 	'left': (W - boxw) / 2,
	// 	'z-index': '50',

	// })
	//先把这个框藏在按钮的下面
	$write.css({
		'display': 'block',

		'top': write_top1,
		// 'left': write_left1,
		'z-index': '100',
		'left': '50%',
		'margin-left': -button_w / 2
	});
	//把框移到屏幕中间，并令其成为最高的一层
	$write.animate({
		// 'z-index': '100',
		'top': (H - button_h) / 2,
		// 'left': (W-171)/2,

	}, 100, function() {
		$write.animate({


			'width': boxw,
			'height': 0.52 * H,
			'top': box_top,
			// 'left': (W - boxw) / 2,
			// 'top':'50%',
			// 'left':'50%',
			'margin-left': -boxw / 2,
			// 'margin-top':-0.25*H

		}, 300, function() {
			//接下来就是展开遮罩层的动画了
			// setTimeout(function() {
			// 	$(".writewrap").show();
			// 	$(".writewrap").animate({
			// 		'width': '100%',
			// 		'height': H,
			// 		'top': '0',
			// 		'left': '0'

			// 	}, 300)
			// }, 50)

		})
	})
	//展开该框（其实这里应该采取等比例的作法让展开看起来更贴合事实）

	// $(window).resize(function() {
	// 	$write.css({
	// 		'width': boxw,
	// 		'height': 0.52 * H,
	// 		// 'top': box_top,
	// 		// 'left': (W - boxw) / 2,
	// 		'top': '50%',
	// 		'left': '50%',
	// 		'margin-left': -boxw / 2,
	// 		'margin-top': -0.25 * H
	// 	})

	// })



})

$(".write .close").click(function() {
	//先收起遮罩层并隐藏
	// alert("666")
	// $(".writewrap").animate({
	// 	'width': boxw,
	// 	'height': 0.5 * H,
	// 	'top': box_top,
	// 	'left': (W - boxw) / 2,
	// 	'z-index': '50',

	// }, 300)

	// $(".writewrap").hide(function() {
	//接下来这个框应该先回到中间
	setTimeout(function() {
		$write.animate({


			'width': button_w,
			'height': button_h,
			'top': (H - button_h) / 2,
			// 'left': (W - 170) / 2,
			'margin-left': -button_w / 2
		})
		//接下来把它移回去



		$write.animate({

			'top': write_top1,
			// 'left': write_left1
			// 'margin-left':-button_w/2

		}, 50, function() {
			$write.css({
				'z-index': '-5',
				'display': 'none'
			})
		});

	}, 10)
	// });
});

function fillscreen() {

}

function headshow() {
	$(".write .head li").eq(headimg - 1).show().siblings().hide();
}



let Iscomment = false,
	Isverify = false,
	Isid = false;

//id输入 ??字数限制呢
$(".write .id").on({
	focus: function() {
		if (!Isid && $(".write .id").val() == '') {
			Isid = true;
		}
	}
})
//留言框判断
$(".write textarea").on({
	focus: function() {
		if (!Iscomment && $(".write textarea").val() == '') {
			Iscomment = true;
		}
	},
	keydown: function() {
		if ($(".write textarea").val().length > 80) {
			alert("字数太多了！");
			$(".write textarea").val($(".write textarea").val().substring(0, 80));

		}
	}
})

//验证码输入部分
$(".verify input").on({
	focus: function() {
		if (!Isverify && $(".verify input").val() == '') {
			Isverify = true;
		}
	}
})



//提交留言表单
$(".write .submit").click(function() {

	if (!Iscomment) {
		alert("留言不能为空！");
	} else if (!Isverify) {
		alert("请输入验证码！");
	} else {
		var msg = $(".write textarea").val(),
			msg = htmlEncodeJQ(msg);
		var com = {
			url: 'http://118.25.179.209/api/comment/get',
			method: 'POST',
			data: {
				content: msg
			},
			dataType: 'Default: Intelligent Guess',
			async: true

		}
	}
})



//滚动条插件


$(window).on("load", function() {
	$(".index_topic").mCustomScrollbar();



});

$(".index_topic").mCustomScrollbar({

	callbacks: {
		whileScrolling: function() {
			if (parseInt($(".mCSB_dragger").css("bottom")) < "4") {
				// addcomment();
			}

		}
	}
})


//更换验证码事件
function changeverify() {


}

//频繁调用函数，特别用于调整大小时
$(window).resize(function() {})



//promise
function promisesetajax(obj) {
	return new Promise((resolve, reject) => {
		var request = new XMLHttpRequest();
		request.open(obj.method, obj.url, obj.async);
		if (obj.method == 'GET') {
			request.send();
		} else if (obj.method == 'POST') {
			request.send(obj.data);
		}

		request.onreadystatechange = function() {
			if (request.readyState === 4) {
				if (request.status === 200) {
					var dat = JSON.parse(request.responseText);
					resolve(dat);

				} else {
					reject(new Error(request.status))
				}
			}

		}

	})
}



//添加评论的方式
function addcomment() {

	var obj = {
		url: 'http://118.25.179.209/api/comment/get',
		method: 'GET',
		data: {

		},
		dataType: 'Default: Intelligent Guess',
		async: true

	}


	promisesetajax(obj).then(function(data) {
			let str = "";
			if (data.comment == '[]') {

			} else {
				for (let i = 0, m = data.comment.length; i < m; i++) {

					str += `<div class="comments clearfix">
	         			 	<div class="head"><img src="${data.comment[i].head}" alt="" /></div>
	          				<div class="right clearfix">
				            <div class="clearfix" style="margin-bottom: -5px;"> 
				              	<div class="id"></div>
				             	 <div class="time">${data.comment[i].createTime}</div>
				            </div>
				            <p>${data.comment[i].content}</p>
				          	</div>
			        	</div>
        `
				}
			}

			$("#mCSB_1_container").append(str);



		},
		function(error) {
			alert("发生错误：" + error);
		})

	// $.ajax({
	// 	type: "GET",
	// 	url: "http://118.25.179.209/api/comment/get",
	// 	dataType: "json",
	// 	success: function(data) {

	// 		let str = "";
	// 		for (let i = 0, m = data.comment.length; i < m; i++) {

	// 			str += `<div class="comments clearfix">
	//          			 	<div class="head"><img src="${data.comment[i].head}" alt="" /></div>
	//           				<div class="right clearfix">
	// 			            <div class="clearfix" style="margin-bottom: -5px;"> 
	// 			              	<div class="id"></div>
	// 			             	 <div class="time">${data.comment[i].createTime}</div>
	// 			            </div>
	// 			            <p>${data.comment[i].content}</p>
	// 			          	</div>
	// 		        	</div>
	//        `
	// 		}
	// 		$("#mCSB_1_container").append(str);

	// 	},
	// 	error: function(jqXHR) {
	// 		alert("发生错误：" + jqXHR.status);
	// 	},
	// });
}

//评论初始化函数
// addcomment();



// $.ajax({ 
//     type: "POST", 	
// 	url: "http://localhost/aite/js/jj.txt",
// 	data: {
// 		num: $("#mCSB_1").children().length
// 	},
// 	dataType: "json",
// 	//发送成功可以返回的东西
// 	success: function(data){
// 		alert("666")
// 	},
// 	error: function(jqXHR){     
// 	   alert("发生错误：" + jqXHR.status);  
// 	},     
// });


// 	var obj = {
// 		url: 'http://localhost/aite/js/jj.txt',
// 		method: 'GET',
// 		data: {
// 			// num: $("#mCSB_1").children().length
// 		},
// 		dataType: 'Default: Intelligent Guess',
// 		async: true

// 	}

// 	function promisesetajax(obj) {
// 		return new Promise((resolve, reject) => {
// 			var request = new XMLHttpRequest();
// 			request.open(obj.method, obj.url, obj.async);
// 			request.send(obj.data);
// 			request.onreadystatechange = function() {
// 				if (request.readyState === 4) {
// 					if (request.status === 200) {
// 						var dat = JSON.parse(request.responseText);
// 						resolve(dat);

// 					} else {
// 						reject(new Error(request.status))
// 					}
// 				}

// 			}

// 		})
// 	}


// 	promisesetajax(obj).then(function(data) {
// 			let str = "";
// 			for (let i = 0; i < data.length; i++) {

// 				str += `<div>${data[i].content}</div>`;

// 			}
// 			// $("#mCSB_1_container")[0].innerHtml = str;
// 			console.log(str)
// 			document.getElementById("mCSB_1_container").innerHtml = str;
// 			let ss= document.getElementById("bb");
// 			ss.innerHtml = "6666";

// 		},
// 		function(error) {
// 			alert("发生错误：" + error);
// 		})

// }
// document.addEventListener("DOMNodeInserted", function(e) {
// 	console.log("insert", e.target);
// });

// })