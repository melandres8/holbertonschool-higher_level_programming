#!/usr/bin/node
// function that increments and calls a function.
exports.addMeMaybe = function (myNumber, func) {
  func(myNumber + 1);
};
