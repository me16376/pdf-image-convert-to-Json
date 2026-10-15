const fs = require('fs');
const path = require('path');

const baseDir = path.join(__dirname, '..', 'JSON Data', 'BUET Patern');

const devanagariNonPunct = /[\u0900-\u0963\u0966-\u097F]/;
const foreignScript = /[\u0D80-\u0DFF\u0A80-\u0AFF\u0B00-\u0B7F\u0B80-\u0BFF\u0C00-\u0C7F\u0C80-\u0CFF\u0D00-\u0D7F]/;
const corruptUnicode = /[\uFFFD\uFEFF]/;
const doubleKar = /([ািীুূৃেৈৌ])\1+/;
const brokenHalant = /[\u0980-\u09FF]\s+্|্\s+[\u0980-\u09FF]/;
const detachedKar = /\s+[া-ৌ]/;
const doubleHasant = /্{2,}/;
// words split by hyphen: e.g. letter- space- letter
const splitHyphenWord = /([\u0980-\u09FFa-zA-Z]{2,})-\s+([\u0980-\u09FFa-zA-Z]{2,})/;
// English words attached directly to dots e.g. word.....word
const attachedDots = /[a-zA-Z]+[\.]{2,}[a-zA-Z]+|[a-zA-Z]+[…]+[a-zA-Z]+/;

function inspectFile(subject, filename) {
  const filePath = path.join(baseDir, subject, filename);
  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  const isBananShuddhi = (filename === 'বানান ও শুদ্ধিকরণ.json');

  const findings = [];

  data.forEach((q, index) => {
    const fieldsToCheck = [
      { name: 'question', text: q.question },
      { name: 'answer', text: q.answer },
      { name: 'explanation', text: q.explanation || '' }
    ];

    if (!isBananShuddhi && Array.isArray(q.options)) {
      q.options.forEach((opt, oidx) => {
        fieldsToCheck.push({ name: `options[${oidx}]`, text: opt });
      });
    }

    fieldsToCheck.forEach(f => {
      const txt = f.text;
      if (!txt || typeof txt !== 'string') return;

      if (devanagariNonPunct.test(txt)) {
        findings.push({ qId: q.id, field: f.name, issue: 'Devanagari character', snippet: txt.match(devanagariNonPunct)[0] });
      }
      if (foreignScript.test(txt)) {
        findings.push({ qId: q.id, field: f.name, issue: 'Foreign script', snippet: txt.match(foreignScript)[0] });
      }
      if (corruptUnicode.test(txt)) {
        findings.push({ qId: q.id, field: f.name, issue: 'Corrupt unicode char', snippet: 'FFFD/FEFF' });
      }
      if (doubleKar.test(txt)) {
        findings.push({ qId: q.id, field: f.name, issue: 'Duplicate kar (vowel sign)', snippet: txt.match(doubleKar)[0] });
      }
      if (doubleHasant.test(txt)) {
        findings.push({ qId: q.id, field: f.name, issue: 'Double hasant', snippet: '্্' });
      }
      if (attachedDots.test(txt)) {
        findings.push({ qId: q.id, field: f.name, issue: 'Word attached to dots/blank without space', snippet: txt.match(attachedDots)[0] });
      }
    });
  });

  return { subject, filename, mcqCount: data.length, findings };
}

const subjects = ['Bangla', 'English'];
const allResults = [];

subjects.forEach(subj => {
  const dir = path.join(baseDir, subj);
  const files = fs.readdirSync(dir).filter(f => f.endsWith('.json'));
  files.forEach(f => {
    allResults.push(inspectFile(subj, f));
  });
});

console.log(JSON.stringify(allResults, null, 2));
