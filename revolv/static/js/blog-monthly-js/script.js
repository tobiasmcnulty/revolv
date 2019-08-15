$(document).ready(function(){
  $('.campaign-list').slick({
  	arrows: false,
  	speed: 300,
  	dots: true,
    infinite: true,
    adaptiveHeight: true,
  	slidesToShow: 3,
  	slidesToScroll: 3,
  	responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 3,
        infinite: true,
        dots: true
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ]
  });
  $('.testimonial-list').slick({
  	arrows: false,
  	speed: 300,
  	dots: true,
    infinite: true,
    adaptiveHeight: true,
  	slidesToShow: 2,
  	slidesToScroll: 2,
  	responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2,
        infinite: true,
        dots: true
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ]
  });
  $('.nonprofit-app-slick').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    asNavFor: '.nonprofit-app-slick-nav'
  });
  $('.nonprofit-app-slick-nav').slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    asNavFor: '.nonprofit-app-slick',
    dots: false,
    focusOnSelect: true,
    responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2,
        infinite: true,
        dots: true
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
  ]
  });
  $('.clean-enrgy-col').tooltipster({
      animation: 'fade',
      side: 'bottom',
      arrow: false,
      trigger: 'click',
      interactive: true,
      contentAsHTML: true,
      theme: 'tooltipster-shadow'
   });
  $(function () {
  'use strict'
    $('[data-toggle="offcanvas"]').on('click', function () {
      $('#navbar-section').toggleClass('active-dark')
    })
  })
  $(window).scroll(function () {
	  if ($(window).scrollTop() > 75) {
	  	$('.navbar').removeClass('top-nav');
	    $('.navbar').addClass('is-sticky');
	  }
	  if ($(window).scrollTop() < 76) {
	    $('.navbar').removeClass('is-sticky');
	    $('.navbar').addClass('top-nav');
	  }
	});
  $(function () {
  'use strict'
	  $('[data-toggle="offcanvas"]').on('click', function () {
	  	$(this).toggleClass('is-active')
	    $('.offcanvas-collapse').toggleClass('open')
	  })
	})

  var TxtRotate = function(el, toRotate, period) {
  this.toRotate = toRotate;
  this.el = el;
  this.loopNum = 0;
  this.period = parseInt(period, 10) || 2000;
  this.txt = '';
  this.tick();
  this.isDeleting = false;
};

TxtRotate.prototype.tick = function() {
  var i = this.loopNum % this.toRotate.length;
  var fullTxt = this.toRotate[i];

  if (this.isDeleting) {
    this.txt = fullTxt.substring(0, this.txt.length - 1);
  } else {
    this.txt = fullTxt.substring(0, this.txt.length + 1);
  }

  this.el.innerHTML = '<span class="wrap">'+this.txt+'</span>';

  var that = this;
  var delta = 300 - Math.random() * 100;

  if (this.isDeleting) { delta /= 2; }

  if (!this.isDeleting && this.txt === fullTxt) {
    delta = this.period;
    this.isDeleting = true;
  } else if (this.isDeleting && this.txt === '') {
    this.isDeleting = false;
    this.loopNum++;
    delta = 500;
  }

  setTimeout(function() {
    that.tick();
  }, delta);
};

  window.onload = function() {
    var elements = document.getElementsByClassName('txt-rotate');
    for (var i=0; i<elements.length; i++) {
      var toRotate = elements[i].getAttribute('data-rotate');
      var period = elements[i].getAttribute('data-period');
      if (toRotate) {
        new TxtRotate(elements[i], JSON.parse(toRotate), period);
      }
    }
    // INJECT CSS
    var css = document.createElement("style");
    css.type = "text/css";
    css.innerHTML = ".txt-rotate > .wrap { border-right: 0.08em solid #fff }";
    document.body.appendChild(css);
  };

  const players = Plyr.setup('.plyr-video', {
    resetOnEnd: true
  });
  window.players = players;
  $('.nonprofit-app-slick').on('beforeChange', function(event, slick, currentSlide, nextSlide){
    var current = $(slick.$slides[currentSlide]);
      players.stop();
  });
});