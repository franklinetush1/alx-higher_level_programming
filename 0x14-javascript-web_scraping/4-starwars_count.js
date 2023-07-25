#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (!error) {
    const responseData = JSON.parse(body);
    const movies = responseData.results;
    let count = 0;

    for (const movie of movies) {
      const characters = movie.characters;
      const AntillesPresent = characters.some((characterUrl) => characterUrl.endsWith('/18/'));

      if (AntillesPresent) {
        count++;
      }
    }

    console.log(count);
  } else {
    console.log(error);
  }
});
