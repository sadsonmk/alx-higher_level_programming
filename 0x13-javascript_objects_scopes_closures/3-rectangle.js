#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return undefined;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let value = '';
      for (let j = 0; j < this.width; j++) {
        value += 'X';
      }
      console.log(value);
    }
  }
}
module.exports = Rectangle;
