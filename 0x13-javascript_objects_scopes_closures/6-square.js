#!/usr/bin/node
const Squares = require('./5-square');

class Square extends Squares {
  charPrint (c) {
    if (c === undefined) {
	    c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let value = '';
      for (let j = 0; j < this.width; j++) {
        value += c;
      }
      console.log(value);
    }
  }
}
module.exports = Square;
