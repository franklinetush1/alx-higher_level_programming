#!/usr/bin/node
const squareSize = parseInt(process.argv[2]);
if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < squareSize; x++) {
    let length = '';
    for (let width = 0; width < squareSize; width++) {
      length += 'X';
    }
    console.log(length);
  }
}
