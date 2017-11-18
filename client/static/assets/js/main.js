$(document).ready(function(){
  var nav= $('.navbar-fixed-top');
  var distancia = $('.navbar-fixed-top').offset();
  if (distancia.top >= 0) {
    nav.removeClass('efecto').addClass('normal');
  }
  $(window).scroll(function(){
    var scroll= $(window).scrollTop();

    if(scroll >= 600){
      nav.removeClass('normal').addClass('efecto');
    } else{
      nav.removeClass('efecto').addClass('normal');
    }
  });
});

(function($) {
  "use strict";
  // Add "loaded" class when a section has been loaded
  $(window).scroll(function() {
    var scrollTop = $(window).scrollTop();
    $(".section").each(function() {
      var elementTop = $(this).offset().top - $('#header').outerHeight();
      if(scrollTop >= elementTop) {
        $(this).addClass('loaded');
      }
    });
  });

  //map

  function initialize() {
    var mapCanvas = document.getElementById('map-canvas');
    var latLng = new google.maps.LatLng(42.6159,-70.6620)
    var mapOptions = {
      center: latLng,
      // center: new google.maps.LatLng(42.606374,-70.662544),
      zoom: 9,
      mapTypeId: google.maps.MapTypeId.ROADMAP,
      scrollwheel: false
    };
    var map = new google.maps.Map(mapCanvas, mapOptions)

    var marker = new google.maps.Marker({
      position: latLng,
      map: map,
      title: 'Ocean Alliance'
    });
  }
  google.maps.event.addDomListener(window, 'load', initialize);

//   options = $.extend({
//     scrollwheel: false,
//     navigationControl: false,
//     mapTypeControl: false,
//     scaleControl: false,
//     draggable: false,
//     mapTypeId: google.maps.MapTypeId.ROADMAP
// }, options);

  // One Page Navigation Setup
  $('.one-page-nav #navigation').singlePageNav({
    offset: $('.one-page-nav').outerHeight(),
    filter: ':not(.external)',
    speed: 750,
    currentClass: 'active',

    beforeStart: function() {
    },
    onComplete: function() {
    }
  });

  // Sticky Navbar Affix
  $('.one-page-nav').affix({
    offset: {
      top: $('#topbar').outerHeight(),
    }
  });

  // Smooth Hash Link Scroll
  $('.smooth-scroll').click(function() {
    if (location.pathname.replace(/^\//,'') === this.pathname.replace(/^\//,'') && location.hostname === this.hostname) {

      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top
        }, 1000);
        return false;
      }
    }
  });

  $('.nav a').on('click', function(){
    if($('.navbar-toggle').css('display') !=='none'){
      $(".navbar-toggle").click();
    }
  });

  var $container = $('.portfolio-isotope');
  $container.imagesLoaded(function(){
    $container.isotope({
      itemSelector : '.portfolio-item',
      resizable: true,
      resizesContainer: true
    });
  });

  $('section#challenge a').on('click', function(){
    $('#project-modal img').attr('src', $(this).attr('data-image-url'));
    if ($(this).attr('data') == "texto1") {
        $('#project-modal h3.project-title').html('Reto 1');
        $('#project-modal p.prueba').html('Esto es el texto del reto 1.');
    }
    if ($(this).attr('data') == "texto2") {
         $('#project-modal p.prueba').html('Esto es el texto del reto 2');
         $('#project-modal h3.project-title').html('Reto 2');
    }
    if ($(this).attr('data') == "texto3") {
         $('#project-modal p.prueba').html('Esto es el texto del reto 3');
         $('#project-modal h3.project-title').html('Reto 3');
    }
    // if(){
    //   $('#project-modal p.prueba').html('Así se puede hacer un texto dinámico chinga!');
    // }
  });

  // filter items when filter link is clicked
  $('#filters a').click(function(){
    var selector = $(this).attr('data-filter');
    $container.isotope({ filter: selector });
    return false;
  });

  $('#contactform').submit(function() {
    var action = $(this).attr('action');
    var values = $(this).serialize();

    $.post(action, values, function(data) {
      $('.results').hide().html(data).slideDown('slow');
      $('#contactform').find('.form-control').val('');
    });
    return false;
  });

  $('.iphone-carousel').on('slid.bs.carousel', function () {
    var carouselData = $(this).data('bs.carousel');
    var currentIndex = carouselData.getActiveIndex();
    $('.section-iphone-features .feature-block').removeClass('active');
    $(".section-iphone-features").find("[data-slide-to='" + currentIndex + "']").addClass('active');
  });
})(jQuery);