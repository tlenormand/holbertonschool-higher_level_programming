#!/usr/bin/node
/*
prints the title of a Star Wars movie
where the episode number matches a given integer
*/

const axios = require('axios');

axios({
  method: 'get',
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2]
})
  .then((response) => {
    console.log(response.data.title);
  }, (error) => {
    console.log('code : ' + error.response.status);
  });
