#!/usr/bin/node
const sf = require('fs');
sf.fstat.readfile(process.argv[2], 'utf-8', function (error, content) {
  console.log(error || content);
});
