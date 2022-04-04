#!/usr/bin/node
/*
script that prints the first argument passed to it
*/
const myVar = process.argv.slice(2);
if (myVar[0]) {
  console.log(myVar[0]);
} else {
  console.log('No argument');
}
