#!/usr/bin/node
/*
script that imports an array and computes a new array
*/
const list = require('./100-data.js').list;
const mapList = [];

list.map((element, idx) => { return mapList.push(element * idx); });

console.log(list);
console.log(mapList);
