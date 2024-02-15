#!/usr/bin/node

let prtdNum = 0;
exports.logMe = function (item) { console.log(`${prtdNum++}: ${item}`); };
