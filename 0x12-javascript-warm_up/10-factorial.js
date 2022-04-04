#!/usr/bin/node
/*
script that computes and prints a factorial
*/
function factorial (num) {
  if (num > 0) {
    return num * factorial(num - 1);
  }
  return 1;
}

console.log(factorial(parseInt(process.argv[2])));
