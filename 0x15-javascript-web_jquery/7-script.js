#!/usr/bin/node
/*
JavaScript script that fetches the character name
from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
*/
const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('#character').text(data.name);
});
