#!/usr/bin/node
// script that prints two arguments passed to it, in the following format: “ is ”
const arg1 = process.argv[2];
const arg2 = process.argv[3];
const argLen = process.argv.length;
if (argLen < 3) {
  console.log(arg1 + ' is ' + arg2);
} else if (arg1 && !arg2) {
  console.log(arg1 + ' is ' + arg2);
} else {
  console.log(arg1 + ' is ' + arg2);
}
