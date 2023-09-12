#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((c, curr) => curr === searchElement ? c + 1 : c, 0);
};
