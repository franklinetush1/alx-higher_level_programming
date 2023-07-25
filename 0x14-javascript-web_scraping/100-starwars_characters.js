#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    characters.forEach((characterUrl) => {
      request(characterUrl, function (error, response, body) {
        if (!error) {
          const characterName = JSON.parse(body).name;
          console.log(characterName);
        }
      });
    });
  }
});
