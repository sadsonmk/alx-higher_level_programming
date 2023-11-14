#!/usr/bin/node
const Squares = require('./5-square');

class Square extends Squares {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.size; i++) {
      let value = '';
      for (let j = 0; j < this.size; j++) {
        value += c;
      }
      console.log(value);
    }
  }
}
module.exports = Square;
