#!/usr/bin/node

const arr = process.argv.slice(2).map(Number);
function SecondLargest(arr){
    if (arr.length === 0) {
      return 0;
    } else if (arr.length === 1) {
      return 0;
    } else {
      const sorted = arr.sort((a, b) => b - a);
      return sorted[1];
    }
}
