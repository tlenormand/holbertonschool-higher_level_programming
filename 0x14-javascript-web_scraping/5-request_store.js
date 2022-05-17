#!/usr/bin/node
/*
gets the contents of a webpage and stores it in a file
*/

const axios = require('axios');
const fs = require('fs');

axios({
  method: 'get',
  url: process.argv[2]
})
  .then((response) => {
    fs.writeFile(process.argv[3], response.data, 'utf-8', function (err, data) {
      if (err) { return console.log(err); }
    });
  }, (error) => {
    console.log('code : ' + error.response.status);
  });
