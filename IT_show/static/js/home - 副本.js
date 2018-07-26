var pagestatus,nowchoose;

$(document).ready(function() {
	$(".menu").children().eq(1).addClass("nowpage");
	localwee();
	pagestatus=0;
	nowchoose=1;
	
	$(".nav h2").css({"color":"#FFFFFF"});
	$(".nav a").css({"color":"#FFFFFF"});
})

$(window).on('load resize', function() {
	if (!isFlashing[".bgdown"]){
		if (pagestatus==1){
			$(".bgdown").css({"left": 0, "top": 0, "width": sw, "height": sh})
			$(".choose_aboutus").css({"left": sw*0.265, "top": sh*0.15, "width": sw*0.47, "height": 220})
		}
		if (pagestatus==0){
			$(".bgdown").css({"left": 0, "top": sh*0.635, "width": sw, "height": sh})
			$(".choose_aboutus").css({"left": sw*0.265, "top": sh*0.02, "width": sw*0.47, "height": 220})
		}
	}
});

function chooseImgchange(mode){
	for (var i=1;i<=3;i++)
	{
		var handle_choose = ".cho" + i.toString();
		var handle_intro = ".intro" + i.toString();
		if (nowchoose==i&&mode==0){
			$(handle_choose).children().eq(0).attr("src",$("#bluechoose").val());
			$(handle_intro).show();
		} else {
			$(handle_choose).children().eq(0).attr("src",$("#yellowchoose").val());
			if (mode==0)
				$(handle_intro).hide();
		}
	}
}

function pagedown(){
	if (pagestatus!=1&&(!isFlashing[".bgdown"])){
		slideFlash(".bgdown",0,0,sw,sh);
		slideFlash(".choose_aboutus",sw*0.265,sh*0.15,sw*0.47,220);
		$(".choose p").hide();
		pagestatus=1;
		chooseImgchange(0);
		$(".nav h2").css({"color":"black"});	
		$(".nav a").css({"color":"black"});
	}
}

function pageup(){
	if (pagestatus!=0&&(!isFlashing[".bgdown"])){
		
		slideFlash(".bgdown",0,sh*0.635,sw,sh);
		slideFlash(".choose_aboutus",sw*0.265,sh*0.02,sw*0.47,220);
		$(".choose p").show();
		pagestatus=0;
		chooseImgchange(1);
		$(".nav h2").css({"color":"#FFFFFF"});
		$(".nav a").css({"color":"white"});
	}
}

$(".choose").click(function(){
	for (var i=1;i<=3;i++)
	{
		if ($(this).hasClass("cho" + i.toString()))
			nowchoose = i;
	}
	chooseImgchange(0);
	pagedown();
});//如果点击

$(window).bind('mousewheel', function(event, delta) {  
	if(delta==-1){
		pagedown();
	}
	else if(delta==1){
		pageup();
	}
});