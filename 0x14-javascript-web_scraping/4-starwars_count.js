#!/usr/bin/node
/*
prints the number of movies
where the character “Wedge Antilles” is present (id 18)
*/

const axios = require('axios');

axios({
  method: 'get',
  url: process.argv[2]
})
  .then((response) => {
    let count = 0;
    let prop;
    let character;
    for (prop in response.data.results) {
      for (character in response.data.results[prop].characters) {
        if (response.data.results[prop].characters[character] === 'https://swapi-api.hbtn.io/api/people/18/') { count += 1; }
      }
    }
    console.log(count);
  }, (error) => {
    console.log('code : ' + error.response.status);
  });
