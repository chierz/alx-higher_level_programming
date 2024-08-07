#!/usr/bin/node
/**
  prints number of movies where the character 'Wedge Antilles' is present.
  usage: ./4-starwars_count.js <API URL>
  */

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
