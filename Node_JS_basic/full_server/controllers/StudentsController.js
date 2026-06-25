const { readDatabase } = require('../utils');

class StudentsController {
  static async getAllStudents(req, res) {
    const dbFile = process.argv[2];

    try {
      const data = await readDatabase(dbFile);

      let response = 'This is the list of our students\n';

      const keys = Object.keys(data).sort((a, b) =>
        a.toLowerCase().localeCompare(b.toLowerCase())
      );

      for (const field of keys) {
        response += `Number of students in ${field}: ${data[field].length}. List: ${data[field].join(', ')}\n`;
      }

      res.status(200).send(response.trim());
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const dbFile = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const data = await readDatabase(dbFile);

      const students = data[major] || [];

      res.status(200).send(`List: ${students.join(', ')}`);
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }
}

module.exports = StudentsController;
