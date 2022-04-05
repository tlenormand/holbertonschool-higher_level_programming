#!/usr/bin/node
/*
script that concats 2 files
*/
const fs = require('fs');

fs.readFile('fileA', 'utf8', (err, fileA) => {
  if (err) {
    return console.log(err);
  }
  fs.readFile('fileB', 'utf8', (err, fileB) => {
    if (err) {
      return console.log(err);
    }
    fs.writeFileSync('fileC', fileA + fileB);
  });
});
