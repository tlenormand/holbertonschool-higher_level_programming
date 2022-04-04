#!/usr/bin/node
/*
script that searches the second biggest integer in the list of arguments
*/
const listInt = process.argv.slice(2);
let max = listInt[0];
let second = 0;

for (let i = 1; listInt[i]; i++) {
  if (listInt[i] > max) {
    second = max;
    max = listInt[i];
  } else if (listInt[i] > second) {
    second = listInt[i];
  }
}

console.log(second);
