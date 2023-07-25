#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, function (error, response, body) {
  if (!error) {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
