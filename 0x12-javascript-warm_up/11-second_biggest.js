#!/usr/bin/node

const arr = process.argv.slice(2).map(Number);

if (arr.length === 0) {
  console.log(0);
} else if (arr.length === 1) {
  console.log(0);
} else {
  const sorted = arr.sort((a, b) => b - a);
  console.log(sorted[1]);
}
