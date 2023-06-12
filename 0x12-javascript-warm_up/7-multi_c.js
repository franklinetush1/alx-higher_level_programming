#!/usr/bin/node
let times = parseInt(process.argv[2]);
if (isNaN(times)) {
  console.log('Missing number of occurrences');
} else {
  for (times; times > 0; times--) {
    console.log('C is fun');
  }
}
