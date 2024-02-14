#!/usr/bin/node

class Square extends require('./5-square') {
  charPrint (c = 'X') {
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.height));
    }
  }
}

module.exports = Square;
