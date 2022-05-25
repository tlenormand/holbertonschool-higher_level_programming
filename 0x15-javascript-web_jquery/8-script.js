#!/usr/bin/node
/*
JavaScript script that fetches and lists the title for all movies
by using this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
*/
// const $ = window.$;
const $ = window.$;
$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    for (const movie in data.results) {
      $('#list_movies').append('<li>' + data.results[movie].title + '</li>');
    }
  });
});
