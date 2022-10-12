#!/usr/bin/node
// A script that prints a square
args = process.argv.slice(2);
if (isNaN(parseInt(args[0]))) {
  console.log('Missing size');
} else {
  const row = 'X'.repeat(parseInt(args[0]));
  for (let i = 0; i < args[0]; i++) {
    console.log(row);
  }
}
