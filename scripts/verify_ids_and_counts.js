const fs = require('fs');
const path = require('path');
const baseDir = path.join(__dirname, '..', 'JSON Data', 'BUET Patern');

const subjects = ['Bangla', 'English'];
const summary = [];

subjects.forEach(s => {
  const dir = path.join(baseDir, s);
  fs.readdirSync(dir).filter(f => f.endsWith('.json')).forEach(f => {
    const data = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
    let idMismatch = 0;
    const ids = [];

    data.forEach((q, idx) => {
      ids.push(q.id);
      if (q.id !== idx + 1) idMismatch++;
    });

    const minId = Math.min(...ids);
    const maxId = Math.max(...ids);
    const hasDuplicates = (new Set(ids).size !== ids.length);

    summary.push({
      subject: s,
      filename: f,
      totalMCQs: data.length,
      minId,
      maxId,
      idMismatch,
      hasDuplicates
    });
  });
});

console.log(JSON.stringify(summary, null, 2));
