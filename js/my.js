$(window).on('mousemove', function(e){
    var w = $(window).width();
    var h = $(window).height();
    
    var offsetX = 0.5 - e.pageX / w;
    var offsetY = 0.5 - e.pageY / h;
    
    $(".parallax").each(function(i,el){
        var offset = parseInt($(el).data('offset'));
        
        var translate = "translate3d(" + Math.round(offsetX * offset) + "px, " + Math.round(offsetY * offset) + "px, 0px";
        
        $(el).css({
            'transform':translate
        });
    });
});


$('.component').slick({
    centerMode: true,
    centerPadding: '0px',
    slidesToShow: 3,
  //  autoplay: true,
    responsive: [
    {
      breakpoint: 900,
      settings: {
        centerMode: true,
        slidesToShow: 1
      }
    }]
});