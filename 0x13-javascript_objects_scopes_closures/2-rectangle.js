#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return {}; // Return empty object if either width or height is less than or equal to 0
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
