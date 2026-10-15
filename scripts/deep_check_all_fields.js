const fs = require('fs');
const path = require('path');

const baseDir = path.join(__dirname, '..', 'JSON Data', 'BUET Patern');

const report = [];

function checkFile(subject, filename) {
  const filePath = path.join(baseDir, subject, filename);
  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  const isBanan = (filename === 'বানান ও শুদ্ধিকরণ.json');

  data.forEach((q, idx) => {
    // 1. Missing or empty required fields
    if (!q.id) {
      report.push({ file: filename, qId: idx, issue: 'Missing or zero id' });
    }
    if (!q.question || typeof q.question !== 'string' || q.question.trim().length === 0) {
      report.push({ file: filename, qId: q.id, issue: 'Empty or non-string question' });
    }
    if (!q.answer || typeof q.answer !== 'string' || q.answer.trim().length === 0) {
      report.push({ file: filename, qId: q.id, issue: 'Empty or non-string answer' });
    }

    // 2. Options array check
    if (!Array.isArray(q.options)) {
      report.push({ file: filename, qId: q.id, issue: 'Options is not an array' });
    } else {
      q.options.forEach((opt, oidx) => {
        if (typeof opt !== 'string' || opt.trim().length === 0) {
          report.push({ file: filename, qId: q.id, issue: `Option[${oidx}] is empty` });
        }
      });
    }

    // 3. Trailing or double spaces
    const checkSpaces = (field, text) => {
      if (!text || typeof text !== 'string') return;
      if (text.includes('  ')) {
        report.push({ file: filename, qId: q.id, issue: `Double spaces in ${field}`, text: text.substring(0, 60) });
      }
      if (/^\s+|\s+$/.test(text)) {
        report.push({ file: filename, qId: q.id, issue: `Leading/trailing unstripped space in ${field}` });
      }
    };

    checkSpaces('question', q.question);
    checkSpaces('answer', q.answer);
    if (q.explanation) checkSpaces('explanation', q.explanation);
    if (!isBanan && Array.isArray(q.options)) {
      q.options.forEach((o, oidx) => checkSpaces(`options[${oidx}]`, o));
    }

    // 4. Bengali character integrity
    const checkBengaliIntegrity = (field, text) => {
      if (!text || typeof text !== 'string') return;
      // Corrupt unicode
      if (/[\uFFFD\uFEFF]/.test(text)) {
        report.push({ file: filename, qId: q.id, issue: `Corrupt unicode char in ${field}` });
      }
      // Non-Bengali Indic (Devanagari, Tamil, etc)
      const foreign = text.match(/[\u0900-\u0963\u0966-\u097F\u0A00-\u0D7F]/);
      if (foreign) {
        report.push({ file: filename, qId: q.id, issue: `Foreign Indic script char "${foreign[0]}" in ${field}` });
      }
      // Duplicate vowel signs
      const dup = text.match(/([ািীুূৃেৈোৌ])\1+/);
      if (dup) {
        report.push({ file: filename, qId: q.id, issue: `Duplicate vowel sign "${dup[0]}" in ${field}` });
      }
      // Stray isolated vowel signs without preceding consonant
      const strayKar = text.match(/(^|[^\u0985-\u09FA])([ািীুূৃেৈোৌ])/);
      if (strayKar && !text.includes('(' + strayKar[2] + ')') && !text.includes('“' + strayKar[2] + '”')) {
        // Only if not single letter in quotes/brackets
        report.push({ file: filename, qId: q.id, issue: `Stray kar without consonant in ${field}: "${strayKar[0]}"` });
      }
    };

    checkBengaliIntegrity('question', q.question);
    checkBengaliIntegrity('answer', q.answer);
    if (q.explanation) checkBengaliIntegrity('explanation', q.explanation);
    if (!isBanan && Array.isArray(q.options)) {
      q.options.forEach((o, oidx) => checkBengaliIntegrity(`options[${oidx}]`, o));
    }

    // 5. English integrity
    const checkEnglishIntegrity = (field, text) => {
      if (!text || typeof text !== 'string') return;
      // Word directly touching multiple dots or ellipsis
      const dotTouch = text.match(/[a-zA-Z]+(\.{2,}|…+)[a-zA-Z]+/);
      if (dotTouch) {
        report.push({ file: filename, qId: q.id, issue: `Word touching dots in ${field}: "${dotTouch[0]}"` });
      }
      // Repeated consonant > 2 (except intentional or roman numeral iii)
      const triple = text.match(/\b([a-zA-Z])\1\1+\b/);
      if (triple && !/^(?:iii|eee)$/i.test(triple[0])) {
        report.push({ file: filename, qId: q.id, issue: `Triple repeated letter "${triple[0]}" in ${field}` });
      }
    };

    checkEnglishIntegrity('question', q.question);
    checkEnglishIntegrity('answer', q.answer);
    if (q.explanation) checkEnglishIntegrity('explanation', q.explanation);
    if (!isBanan && Array.isArray(q.options)) {
      q.options.forEach((o, oidx) => checkEnglishIntegrity(`options[${oidx}]`, o));
    }
  });
}

const subjects = ['Bangla', 'English'];
subjects.forEach(s => {
  const dir = path.join(baseDir, s);
  fs.readdirSync(dir).filter(f => f.endsWith('.json')).forEach(f => {
    checkFile(s, f);
  });
});

console.log(`Deep check finished. Total issues flagged: ${report.length}`);
fs.writeFileSync('scripts/deep_check_all_fields_report.json', JSON.stringify(report, null, 2), 'utf8');

report.forEach(r => {
  console.log(`[${r.file}] Q#${r.qId}: ${r.issue} ${r.text ? `("${r.text}")` : ''}`);
});
