#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  const size = list.length;
  for (let x = 0; x < size; x++) {
    if (searchElement === list[x]) {
      count++;
    }
  }
  return count;
};
