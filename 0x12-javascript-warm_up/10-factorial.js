#!/usr/bin/node

const args = process.argv;

function factorial (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const value = factorial(args[2]);
console.log(value);
