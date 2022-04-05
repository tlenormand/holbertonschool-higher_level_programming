#!/usr/bin/node
/*
class Rectangle that defines a rectangle
*/
class Rectangle {
  constructor (w, h) {
    if (parseInt(w) && w > 0 && parseInt(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let y = 0; y < this.height; y++) {
      for (let x = 0; x < this.width; x++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }
}

module.exports = Rectangle;
