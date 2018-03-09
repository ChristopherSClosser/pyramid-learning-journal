'use strict';

// hide and show nav when scrolling
$(function(){
  //Keep track of last scroll
  var lastScroll = 0;
  $(window).scroll(function(event){
    //Sets the current scroll position
    var st = $(this).scrollTop();
    //Determines up-or-down scrolling
    if (st > lastScroll){
      //Replace this with your function call for downward-scrolling
      // console.log('scrolling down');
      $('.ckata').hide();
      $('.linked').hide();
      $('header').slideUp('fast');
      // removeClass('nav-down').addClass('nav-up');
    }
    else {
      //Replace this with your function call for upward-scrolling
      // console.log('scrolling up');
      $('header').slideDown('fast');
      // removeClass('nav-up').addClass('nav-down');
      $('.ckata').fadeIn('fast');
      $('.linked').fadeIn('fast');
    }
    //Updates scroll position
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

  // $('.list-projects').on('click', function(){
  //   if ($('ul').is(':hidden')){
  //     $('#project-list').animate({width: 'toggle'},350);
  //   } else {
  //     $('#project-list').slideUp('fast');
  //   }
  // });

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
