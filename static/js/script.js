/*--- Materialize jQuery ---*/
$(document).ready(function(){
    $(".sidenav").sidenav({edge: "right", draggable: true});
    $(".dropdown-trigger").dropdown();
    $('.parallax').parallax();
    $('.tabs').tabs();
    $("select").formSelect();
    $('.modal').modal();
  });