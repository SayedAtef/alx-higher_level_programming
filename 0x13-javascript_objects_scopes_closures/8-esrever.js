#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceR(function (arr, curr) {
    arr.push(curr);
    return arr;
  }, []);
};
