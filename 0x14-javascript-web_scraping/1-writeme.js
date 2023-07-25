#!/usr/bin/node
const fs = require('fs');

const filename = process.argv[2];
const contentToWrite = process.argv[3];

fs.writeFile(filename, contentToWrite, (error) => {
  if (error) {
    console.error(error);
  } 
});
