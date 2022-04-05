#!/usr/bin/node
/*
function that prints the number of arguments
already printed and the new argument value
*/
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count += 1;
};

let count = 0;
