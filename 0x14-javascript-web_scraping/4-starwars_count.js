#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const charId = 18;
const charUrl = `https://swapi-api.alx-tools.com/api/people/${charId}/`;

request(url, (error, response, body) => {
  if (!error) {
    const data = JSON.parse(body);
    const dataObjs = data.results;

    const len = dataObjs.length;
    let total = 0;
    for (let i = 0; i < len; i++) {
      const lenObj = dataObjs[i].characters.length;
      for (let j = 0; j < lenObj; j++) {
        if (dataObjs[i].characters[j] === charUrl) {
          total += 1;
        }
      }
    }
    console.log(total);
  }
});
