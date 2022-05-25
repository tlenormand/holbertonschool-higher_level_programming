#!/usr/bin/node
/*
JavaScript script that toggles the class of the <header> element
when the user clicks on the tag DIV#toggle_header
*/
const $ = window.$;
$('#toggle_header').click(function () {
  $('header').toggleClass('green');
  $('header').toggleClass('red');
});
