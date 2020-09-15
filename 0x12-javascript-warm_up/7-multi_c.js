#!/usr/bin/node
// script that prints x times “C is fun”
const myNumber = parseInt(process.argv[2]);
let i = 0;

if (process.argv.length < 3 || typeof myNumber !== 'number') {
  console.log('Missing number of occurrences');
} else {
  while (i < myNumber) {
    console.log('C is fun');
    i++;
  }
}
