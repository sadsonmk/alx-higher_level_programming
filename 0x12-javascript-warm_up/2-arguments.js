#!/usr/bin/node

const args = process.argv;
const size = args.length;

if (size === 2) {
  console.log('No argument');
} else if (size === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
