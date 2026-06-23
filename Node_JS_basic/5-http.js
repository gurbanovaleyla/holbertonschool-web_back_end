const http = require('http');
const fs = require('fs');

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
    return;
  }

  if (req.url === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });

    const dbFile = process.argv[2];

    fs.readFile(dbFile, 'utf-8', (err, data) => {
      let response = 'This is the list of our students\n';

      if (err) {
        response += 'Cannot load the database';
        res.end(response);
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

      for (const field of Object.keys(students)) {
        response += `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}\n`;
      }

      res.end(response.trim());
    });

    return;
  }

  res.writeHead(404, { 'Content-Type': 'text/plain' });
  res.end('Not found');
});

app.listen(1245);

module.exports = app;
