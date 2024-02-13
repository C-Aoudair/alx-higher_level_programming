#!/usr/bin/node

const myNumber = parseInt(process.argv[2]);

if (myNumber) {
  for (let i = 0; i < myNumber; i++) {
    console.log('C is fun');
  }
} else console.log('Missing number of occurrences');
