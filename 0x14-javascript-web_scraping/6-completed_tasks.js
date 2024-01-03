#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error) {
    const value = JSON.parse(body);
    const counter = value.reduce((counted, obj) => {
      const { userId, completed } = obj;
      if (completed) {
        counted[userId] = counted[userId] || {};
        counted[userId].count = (counted[userId].count || 0) + 1;
      }
      return counted;
    }, {});
    const newObj = {};
    for (const user in counter) {
      const total = counter[user].count;
      newObj[user] = total;
    }
    console.log(newObj);
  }
});
