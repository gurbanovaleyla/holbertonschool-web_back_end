const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');

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
      const list = students[field].join(', ');
      console.log(`Number of students in ${field}: ${students[field].length}. List: ${list}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
