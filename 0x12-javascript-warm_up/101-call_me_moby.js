#!/usr/bin/node
// function that executes x times a function.
exports.callMeMoby = function (myNumber, func) {
  for (let i = 0; i < myNumber; i++) {
    func();
  }
};
