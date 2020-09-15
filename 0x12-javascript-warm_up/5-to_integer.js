#!/usr/local/bin/node
// Convert from string to integer
const myNumber = parseInt(process.argv[2]);

if (myNumber) {
  console.log('My number: ' + myNumber);
} else {
  console.log('Not a number');
}
