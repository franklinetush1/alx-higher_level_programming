#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let x = 0; x < this.height; x++) {
        console.log(c.repeat(this.width)); 
      }
    }
  }
};
