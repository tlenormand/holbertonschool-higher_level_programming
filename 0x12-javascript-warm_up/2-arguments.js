#!/usr/bin/node
/*
script that prints the first argument passed to it
*/
const myArgs = process.argv.slice(2);
if (myArgs.length === 0) {
  console.log('No argument');
} else if (myArgs.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
