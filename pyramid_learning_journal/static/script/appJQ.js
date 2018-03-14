'use strict';

// hide and show nav when scrolling
$(function(){
  // Keep track of last scroll
  var lastScroll = 0;
  $(window).scroll(function(event){
    // Sets the current scroll position
    var st = $(this).scrollTop();
    // Determines up-or-down scrolling
    if (st > lastScroll){
      // Use this for downward-scrolling
      // console.log('scrolling down');
      $('.ckata').hide();
      $('.linked').hide();
      $('header').slideUp('fast');
      // removeClass('nav-down').addClass('nav-up');
    }
    else {
      // Use this for upward-scrolling
      // console.log('scrolling up');
      $('header').slideDown('fast');
      // removeClass('nav-up').addClass('nav-down');
      $('.ckata').fadeIn('fast');
      $('.linked').fadeIn('fast');
    }
    // Updates scroll position
    lastScroll = st;
  });
});

//function for mobile menu on page ready
$(function(){
  // $('section').hide();

  $('.burger').on('click', function(){
    if ($('nav').is(':hidden')){
      $('#main-nav').slideDown('fast');
    } else {
      $('#main-nav').slideUp('fast');
    }
  });

  $('#home, #github, #gallery, #me').on('click', function(){
    if (window.innerWidth <= 500){
      $('#main-nav').slideUp('fast');
    }
  });

  $('.dropdown').on('click', function(){
    if ($('.dropdown-content').is(':hidden')){
      $('.dropdown-content').slideDown('fast');
    } else {
      $('.dropdown-content').slideUp('fast');
    }
  });

  // $('#project-list li').on('click', function(e){
  //   e.preventDefault();
  //   $('.github').fadeOut();
  //   $('.gallery').fadeOut();
  //   $('.me').fadeOut();
  //
  //   if ($(this).text() === 'Show all'){
  //     $('section').fadeIn();
  //     $('content').fadeIn();
  //   }else{
  //     $('content').hide();
  //     let $select = ($(this).text());
  //     projectView.projectFilter($select);
  //     $('section').fadeIn();
  //   }
  //
  //   $('#project-list').slideUp('fast');
  //
  //   if (window.innerWidth <= 500){
  //     $('#main-nav').slideUp('fast');
  //   }
  // });
});
