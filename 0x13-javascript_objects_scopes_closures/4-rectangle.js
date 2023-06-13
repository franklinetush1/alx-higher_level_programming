#!/usr/bin/node
class Rectangle{
  constructor(w,h){
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print(){
    for (let x = 0; x < this.height; x++) {
        console.log('X'.repeat(this.width)); 
    } 
  }

  rotate () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
