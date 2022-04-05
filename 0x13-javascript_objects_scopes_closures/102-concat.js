#!/usr/bin/node
/*
script that concats 2 files
*/
const fs = require('fs');

fs.readFile('fileA', 'utf8', (err, fileA) => {
  fs.readFile('fileB', 'utf8', (err, fileB) => {
    fs.writeFileSync('fileC', fileA + fileB);
  });
});
