#!/usr/bin/node
/*
script that imports a dictionary of occurrences by user id
and computes a dictionary of user ids by occurrence
*/
const dict = require('./101-data.js').dict;
const newDict = {};

for (const [key, value] of Object.entries(dict)) {
  if (!newDict[value]) { newDict[value] = []; }
  newDict[value].push(key);
}

console.log(newDict);
