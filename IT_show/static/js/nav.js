$(window).on('load resize', function() {
    var $thisnav = $('.current-menu-item').offset().left-$('.x').offset().left;
    $('.menu-item').hover(function() {
      var $left = $(this).offset().left -$('.x').offset().left;
      var $width = $(this).outerWidth();
      var $start = 0;
      $('.wee').css({ 'left': $left+10 , 'width': $width-20 });
    }, function() {
      var $initwidth = $('.current-menu-item').width();
      $('.wee').css({ 'left': $thisnav+10+'px' , 'width': $initwidth });
    });
  });