#!/usr/bin/node
/*
script that prints a square
*/
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (let y = 0; y < parseInt(process.argv[2]); y++) {
    for (let x = 0; x < parseInt(process.argv[2]); x++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
}
