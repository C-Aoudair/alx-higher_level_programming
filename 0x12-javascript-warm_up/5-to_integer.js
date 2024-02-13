#!/usr/bin/node

const myNumber = Number(process.argv[2]);

if (myNumber) {
  console.log(myNumber);
} else console.log('Not a number');
