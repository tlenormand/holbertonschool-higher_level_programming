#!/usr/bin/node
/*
function that returns the reversed version of a list
*/
exports.esrever = function (list) {
  const output = [];

  while (list.length) {
    output.push(list.pop());
  }

  return output;
};
