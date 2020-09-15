#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.
const args = process.argv;
let myArray;

if (args.length < 3 || args.length === 3) {
  console.log(0);
} else {
  myArray = args.splice(2);
  myArray.sort(function (a, b) {
    return b - a;
  });
  console.log(myArray[1]);
}
