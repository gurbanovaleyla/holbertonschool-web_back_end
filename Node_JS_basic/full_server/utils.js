const fs = require('fs');

function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((l) => l.trim() !== '');
      const students = {};

      for (const line of lines.slice(1)) {
        const [firstname, , , field] = line.split(',');

        if (!students[field]) {
          students[field] = [];
        }
        students[field].push(firstname);
      }

      resolve(students);
    });
  });
}

module.exports = { readDatabase };
