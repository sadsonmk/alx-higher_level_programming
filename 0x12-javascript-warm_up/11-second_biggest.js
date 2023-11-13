#!/usr/bin/node

const args = process.argv;
args.shift();
args.shift();

const len = args.length;
if (len === 0 || len === 1) {
  console.log(0);
} else {
  const myarr = [];
  for (let a = 0; a < len; a++) {
    myarr.push(parseInt(args[a]));
  }
  myarr.sort();
  console.log(myarr[len - 2]);
}
