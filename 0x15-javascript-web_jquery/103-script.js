#!/usr/bin/node
/*
JavaScript script that fetches and prints how to say “Hello”
depending on the language
*/
import fetch from 'node-fetch';

const $ = window.$;

document.addEventListener('DOMContentLoaded', () => {
  $('#language_code').keyup(function (event) {
    if (event.keyCode === 13) {
      $('#btn_translate').click();
    }
  });

  $('#btn_translate').click(function () {
    fetch('https://www.fourtonfish.com/hellosalut/?lang=' + $('#language_code').val())
      .then(function (response) {
        return response.json();
      })
      .then(function (jsonData) {
        $('#hello').text(jsonData.hello);
      });
  });
});
