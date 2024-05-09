
$(document).ready(function(){

    //Owl carousel script
    $('.testimonials .owl-carousel').owlCarousel({
      margin:20,
      loop:true,
      autoplay:true,
      autoplayTimeout:1500,
    //   autoplayHoverPause:true,
      responsive:{
      0:{
      items:1,
      nav:true
      },
      450:{
      items:2,
      nav:true
      },
      650:{
      items:3,
      nav:true
      }
      }
    });
    });