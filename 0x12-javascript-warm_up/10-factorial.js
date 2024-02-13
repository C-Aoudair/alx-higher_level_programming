#!/usr/bin/node

function fact (myNumber) {
  if (myNumber) {
    return (myNumber * fact(myNumber - 1));
  } else return (1);
}

console.log(fact(parseInt(process.argv[2])));
