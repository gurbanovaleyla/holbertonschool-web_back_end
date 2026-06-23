const fs = require('fs').promises;

function countStudents(path) {
  return fs.readFile(path, 'utf8')
    .then((data) => {
      const lines = data.split('\n').filter((line) => line.trim() !== '');

      const students = {};
      let total = 0;

      for (const line of lines) {
        const [firstname, , field] = line.split(',');

        if (!students[field]) {
          students[field] = [];
        }

        students[field].push(firstname);
        total += 1;
      }

      console.log(`Number of students: ${total}`);

      for (const field of Object.keys(students)) {
        console.log(
          `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}`
        );
      }
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
