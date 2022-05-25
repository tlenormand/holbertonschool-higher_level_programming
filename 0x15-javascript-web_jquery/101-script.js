#!/usr/bin/node
/*
JavaScript script that adds, removes and clears LI elements
from a list when the user clicks
*/
const $ = window.$;
document.addEventListener('DOMContentLoaded', () => {
  $('#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(function () {
    $('li:last-child').remove();
  });
  $('#clear_list').click(function () {
    $('li').remove();
  });
});
