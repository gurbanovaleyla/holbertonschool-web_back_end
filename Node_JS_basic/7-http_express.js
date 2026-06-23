const express = require('express');
const fs = require('fs');

const app = express();

const dbFile = process.argv[2];

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  let response = 'This is the list of our students\n';

  fs.readFile(dbFile, 'utf-8', (err, data) => {
    if (err) {
      response += 'Cannot load the database';
      res.send(response);
      return;
    }

    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = {};

    for (const line of lines.slice(1)) {
      const [firstname, , , field] = line.split(',');

      if (!students[field]) {
        students[field] = [];
      }
      students[field].push(firstname);
    }

    response += `Number of students: ${lines.length - 1}\n`;

    for (const field in students) {
      response += `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}\n`;
    }

    res.send(response.trim());
  });
});

app.listen(1245);

module.exports = app;
