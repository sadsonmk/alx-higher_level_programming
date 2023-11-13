#!/usr/bin/node

const args = process.argv;
args.shift();
args.shift();

const mySet = new Set(args);
const myArr = [];
for (const elem of mySet) {
  myArr.push(elem);
}
myArr.sort();

const len = myArr.length;
if (len === 0 || len === 1) {
  console.log(0);
} else {
  console.log(myArr[len - 2]);
}
