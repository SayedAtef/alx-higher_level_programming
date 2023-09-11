#!/usr/bin/node
const listOfArg = process.argv.slice(2);
if (listOfArg.length === 0 || listOfArg.length === 1) {
  console.log(0);
} else {
  listOfArg.sort((a, b) => a - b);
  console.log(listOfArg[listOfArg.length - 2]);
}
