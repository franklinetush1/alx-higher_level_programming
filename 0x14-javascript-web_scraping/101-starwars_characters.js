#!/usr/bin/node

const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';

async function getCharactersFromMovie(movieId) {
  try {
    const response = await fetchMovieData(apiUrl);
    const movies = JSON.parse(response.body).results;
    const targetMovie = movies.find((movie) => movie.episode_id === movieId);
    if (!targetMovie) {
      console.error(`Movie with ID ${movieId} not found.`);
      return;
    }

    const characterUrls = targetMovie.characters;
    const characterNames = await fetchCharacterNames(characterUrls);
    characterNames.forEach((name) => console.log(name));
  } catch (error) {
    console.error('Error:', error.message);
  }
}

function fetchMovieData(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) reject(error);
      else resolve(response);
    });
  });
}

function fetchCharacterNames(characterUrls) {
  return Promise.all(characterUrls.map(fetchCharacterName));
}

function fetchCharacterName(characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) reject(error);
      else resolve(JSON.parse(body).name);
    });
  });
}

const movieId = parseInt(process.argv[2], 10);
getCharactersFromMovie(movieId);
