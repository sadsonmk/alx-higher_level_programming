#!/usr/bin/node

const args = process.argv;
args.shift();
args.shift();

args.sort();

const len = args.length;
if (len === 0 || len === 1) {
  console.log(0);
} else {
  console.log(args[len - 2]);
}
