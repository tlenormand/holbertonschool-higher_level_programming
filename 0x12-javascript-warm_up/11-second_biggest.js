#!/usr/bin/node
/*
script that searches the second biggest integer in the list of arguments
*/
const listInt = process.argv.slice(2);
let max = parseInt(listInt[0]);
let second = 0;

for (let i = 1; listInt[i]; i++) {
  const nb = parseInt(listInt[i]);
  if (nb > max) {
    second = max;
    max = nb;
  } else if (nb > second && nb !== max) {
    second = nb;
  }
}

console.log(second);
