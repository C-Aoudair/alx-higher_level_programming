#!/usr/bin/node

exports.esrever = function (list) {
  return (list.reduceRight((accumulator, currentVal) => {
    return (accumulator.concat(currentVal));
  }, []));
};
