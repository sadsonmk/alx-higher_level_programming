#!/usr/bin/node

const args = process.argv;
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log(NaN);
  } else {
    console.log(a + b);
  }
}
add(parseInt(args[2]), parseInt(args[3]));
