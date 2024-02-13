#!/usr/bin/node

let size = parseInt(process.argv[2]);

if (size) {
  let height = '';
  for (let i = 0; i < size; i++) {
    height += 'X';
  }
  while (size) {
    console.log(height);
    size--;
  }
} else console.log('Missing size');
