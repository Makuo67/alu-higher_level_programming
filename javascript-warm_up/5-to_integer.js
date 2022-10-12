#!/usr/bin/node
// A script that prints My number: <first argument converted in integer> if the first argument can be converted to an intege

const args = process.argv.slice(2);
if (isNaN(parseInt(args[0]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(args[0]));
}
