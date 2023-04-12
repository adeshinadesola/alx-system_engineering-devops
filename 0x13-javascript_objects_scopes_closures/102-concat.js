#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  console.log('Usage: ./102-concat.js fileA fileB destFile');
  process.exit(1);
}

const fileA = process.argv[2];
const fileB = process.argv[3];
const destFile = process.argv[4];

const contentA = fs.readFileSync(fileA, 'utf8');
const contentB = fs.readFileSync(fileB, 'utf8');

fs.writeFileSync(destFile, contentA + contentB);

console.log(`The content of ${fileA} and ${fileB} has been concatenated and written to ${destFile}`);
