#!/usr/bin/node
const counter = process.argv.length;
if (counter < 3) {
  console.log('No argument');
} else if (counter === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
