#!/usr/bin/node
const fs = require('fs');

const args = process.argv;
const firstSource = fs.readFileSync(args[2]).toString();
const secondSource = fs.readFileSync(args[3]).toString();
fs.writeFileSync(args[4], firstSource + secondSource);
