module.exports = class Rectangle{
  constructor(w,h){
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print(){
    for (let x = 0; x < this.height; x++) {
      let rect = '';
      for (let width = 0; width < this.width; width++) {
        rect += 'X';
      }
      console.log(rect);
    }
  }
};
