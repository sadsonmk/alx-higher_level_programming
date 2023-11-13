#!/usr/bin/node

const args = process.argv;
let value = parseInt(args[2]);

if (isNaN(value)) {
  console.log('Missing number of occurrences');
} else {
  while (value > 0) {
    console.log('C is fun');
    value -= 1;
  }
}
