#!/usr/bin/node
/*
gets the contents of a webpage and stores it in a file
*/

const axios = require('axios');

axios({
  method: 'get',
  url: process.argv[2]
})
  .then((response) => {
    const dictTask = {};
    let val;
    const data = response.data;
    for ([, val] of Object.entries(data)) {
      if (val.completed === true) {
        if (dictTask[val.userId] === undefined) {
          dictTask[val.userId] = 0;
        }
        dictTask[val.userId] += 1;
      }
    }
    console.log(dictTask);
  }, (error) => {
    console.log('code : ' + error.response.status);
  });
