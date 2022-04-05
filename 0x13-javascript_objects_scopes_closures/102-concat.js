#!/usr/bin/node
/*
script that concats 2 files
*/
const fs = require('fs');

const pathFileA = process.argv[2];
const pathFileB = process.argv[3];
const pathFileC = process.argv[4];

fs.readFile(pathFileA, 'utf8', (err, fileA) => {
  if (err) { return console.log(err); }
  fs.readFile(pathFileB, 'utf8', (err, fileB) => {
    if (err) { return console.log(err); }
    fs.writeFileSync(pathFileC, fileA + fileB);
  });
});
