#!/usr/bin/node
// script that computes and prints a factorial
const myNumber = parseInt(process.argv[2]);

function Factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * Factorial(n - 1);
  }
}

console.log(Factorial(myNumber));
