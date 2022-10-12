#!/usr/bin/node
const args = process.argv.slice(2);
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
	theFunction();
  }
}
module.exports = { callMeMoby };
