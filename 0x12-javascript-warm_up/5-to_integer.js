#!/usr/bin/node
const value= parseInt(process.argv[2]);
const type = (typeof(value));
if(type == 'number')
{
    console.log('My number: ' + value);
}
else
{
    console.log('Not a number');
}
