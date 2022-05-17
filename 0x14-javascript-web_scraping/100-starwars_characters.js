#!/usr/bin/node
/*
gets the contents of a webpage and stores it in a file
*/

const axios = require('axios');

axios({
  method: 'get',
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2]
})
  .then((response) => {
    for (const character of response.data.characters) {
      axios.get(character)
        .then(res => {
          console.log(res.data.name);
        });
    }
  }, (error) => {
    console.log('code : ' + error.response.status);
  });
