#!/usr/bin/node

const argLenght = process.argv.length;

if (argLenght === 2) console.log('No argument');
else if (argLenght === 3) console.log('Argument found');
else console.log('Arguments found');
