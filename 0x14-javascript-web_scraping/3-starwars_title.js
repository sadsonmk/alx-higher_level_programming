#!/usr/bin/node
const request = require('request');

const epsId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${epsId}`;

request(url, (error, response, body) => {
  if (!error) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
