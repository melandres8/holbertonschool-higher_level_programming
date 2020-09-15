#!/usr/local/bin/node
// script that prints a square
const myNumber = parseInt(process.argv[2]);
let x;

if (myNumber) {
  for (x = 0; x < myNumber; x++) {
    console.log('X'.repeat(myNumber));
  }
} else {
  console.log('Missing size');
}
