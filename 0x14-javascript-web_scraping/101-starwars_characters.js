#!/usr/bin/node

const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';

function getCharacterNames (movieId) {
  const url = `${apiUrl}${movieId}/`;
  request(url, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const characters = JSON.parse(body).characters;
      printCharacterNames(characters, 0);
    } else {
      console.error(`Error fetching data for movie with ID ${movieId}`);
    }
  });
}

function printCharacterNames (characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const characterName = JSON.parse(body).name;
      console.log(characterName);
      printCharacterNames(characters, index + 1);
    } else {
      console.error(`Error fetching character data: ${error}`);
    }
  });
}

const movieId = process.argv[2];
getCharacterNames(movieId);
