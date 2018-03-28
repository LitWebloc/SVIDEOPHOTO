//Паралакс с преследованием мыши
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

//Слайдер

$('.component').slick({
    centerMode: true,
    centerPadding: '0px',
    slidesToShow: 3,
    autoplay: true,
    responsive: [
    {
      breakpoint: 900,
      settings: {
        centerMode: true,
        slidesToShow: 1,
        autoplaySpeed: 1500
      }
    }]
});

//Прелоудер
$(document).ready(function(){
    $(setTimeout(function() {
        $('#prelouder').css("opacity","0");
    if($('#prelouder').css("opacity","0")){
        $(setTimeout(function() {
            $('#prelouder').addClass("none")
        },1000))
    }
    },2000))
    
})