#!/usr/bin/node

const argLength = process.argv.length;

if (argLength === 2 || argLength === 3) {
  console.log('0');
} else {
  let max = parseInt(process.argv[2]);
  let myNumber;
  let number;

  for (let i = 3; i < argLength; i++) {
    number = parseInt(process.argv[i]);
    if (number > max) {
      myNumber = max;
      max = number;
    } else {
      if (myNumber === undefined) {
        myNumber = number;
      } else {
        if (number > myNumber) {
          myNumber = number;
        }
      }
    }
  }

  console.log(myNumber);
}
