#!/usr/local/bin/node
let idx = 0;
exports.logMe = function (item) {
  console.log(`${idx = idx + 1}: ${item}`);
};
