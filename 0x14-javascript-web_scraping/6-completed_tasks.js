#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    let completedTodosByUser = {};
    todos.forEach((todo) => {
      if (todo.completed && completedTodosByUser[todo.userId] === undefined) {
        completedTodosByUser[todo.userId] = 1;
      } else if (todo.completed) {
        completedTodosByUser[todo.userId] += 1;
      }
    });
    console.log(completedTodosByUser);
  }
});
