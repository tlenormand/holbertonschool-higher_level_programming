#!/usr/bin/node
/*
JavaScript script that updates the text color of the <header> element to red
when the user clicks on the tag DIV#red_header
*/
const $ = window.$;
$('#red_header').click(function () {
  $('header').css({
    color: '#FF0000'
  });
});
