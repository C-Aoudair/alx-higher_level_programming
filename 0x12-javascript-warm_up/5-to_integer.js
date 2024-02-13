#!/usr/bin/node

const myNumber = (Math.floor(process.argv[2]));

if (myNumber) {
  console.log(`My number: ${myNumber}`);
} else console.log('Not a number');
