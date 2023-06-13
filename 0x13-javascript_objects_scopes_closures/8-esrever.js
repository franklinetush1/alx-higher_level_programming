#!/usr/bin/node
exports.esrever = function(list) {
  var revList = [];
  for (var i = list.length - 1; i >= 0; i--) {
    revList.push(list[i]);
  }
  return revList;
};
