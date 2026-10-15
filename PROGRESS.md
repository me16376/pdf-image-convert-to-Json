# Workspace Conversion Progress Tracker

**Last Updated:** 2026-10-15  
**Project Root:** `c:\Users\bdCalling\Downloads\Mosabber\pdf-image-convert-to-Json`

---

## 📊 Overall Repository Summary

| Project | Source | Bangla | English | GK | Math | Total Files | Total MCQs | Status |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Project | Source | Bangla | English | GK | Math | Total Files | Total MCQs | Status |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **BUET Pattern** | Images (`p3`–`p750`) | 1,135 (16) | 1,023 (17) | 1,825 (5) | — | **38** | **3,983** | **GK In Progress (1,825 MCQs across 5 topics, Pages 457–700 done)** |
| **Saif Sir NTRCA Suggestion** | PDF (`p1`–`p340`) | 2,231 (111) | 2,034 (98) | 2,211 (99) | 749 (30) | **338** | **7,225** | **100% Completed & Verified** |
| **Ampibian Suggestion** | PDF / Scans | 1,662 (14) | 1,574 (17) | 2,276 (28) | 645 (25) | **84** | **6,157** | **Archived / Complete** |
| **Biddabari-NTRCA** | Question Bank | 2,495 (14) | 1,890 (16) | 3,688 (18) | 1,901 (19) | **67** | **9,974** | **Archived / Complete** |
| **Repository Grand Total** | | **7,523** | **6,521** | **10,000** | **3,295** | **527 files** | **27,339 MCQs** | |

---

## 🎯 BUET Pattern (Non Dept.) - Conversion Progress

- **Source Images:** `Images/BUET Patern/` (`p3.jpg` to `p250.jpg`, Total 246 page images; `p457.jpg` to `p750.jpg`, Total 294 GK images — 0 missing pages)
- **Target Output Directory:** `JSON Data/BUET Patern/`
- **Total Converted to Date:** **38 JSON files, 3,983 MCQs**

### 1. Bangla (বাংলা) — 100% COMPLETED
- **Source Range:** `p3.jpg` to `p134.jpg` (Pages 3 to 134)
- **Status:** **16 Chapters / 16 JSON Files, 1,135 MCQs Extracted & 100% Verified**
- **File Breakdown:**
  1. `উপসর্গ-অনুসর্গ.json` — 17 MCQs
  2. `এক কথায় প্রকাশ.json` — 50 MCQs
  3. `ণত্ব ও ষত্ব বিধান, পরিভাষা.json` — 20 MCQs
  4. `ধ্বনি, বর্ণ ও যুক্তবর্ণ.json` — 41 MCQs
  5. `পদ প্রকরণ, ক্রিয়ার কাল.json` — 40 MCQs
  6. `প্রকৃতি ও প্রত্যয়.json` — 18 MCQs
  7. `প্রয়োগ-অপপ্রয়োগ, লিঙ্গান্তর.json` — 20 MCQs
  8. `বাংলা সাহিত্য.json` — 314 MCQs
  9. `বাগধারা ও প্রবাদ প্রবচন.json` — 72 MCQs
  10. `বানান ও শুদ্ধিকরণ.json` — 75 MCQs
  11. `ভাষা ও ব্যাকরণ.json` — 40 MCQs
  12. `যতি বা ছেদ চিহ্ন, বাক্য ও বাক্য শুদ্ধি.json` — 47 MCQs
  13. `শব্দ ও শব্দার্থ.json` — 131 MCQs
  14. `সংখ্যা, কারক ও বিভক্তি.json` — 39 MCQs
  15. `সন্ধি ও সমাস.json` — 134 MCQs
  16. `সমার্থক ও বিপরীত শব্দ.json` — 77 MCQs

---

### 2. English (ইংরেজি) — 100% COMPLETED
- **Source Range:** `p137.jpg` to `p250.jpg` (Pages 137 to 250)
- **Status:** **17 Chapters / 17 JSON Files, 1,023 MCQs Extracted & 100% Verified**
- **File Breakdown:**
  1. `Parts of Speech.json` — 109 MCQs (Pages 137–155)
  2. `Tense.json` — 26 MCQs (Pages 156–158)
  3. `Right Form of Verb.json` — 89 MCQs (Pages 159–168)
  4. `Corrections.json` — 122 MCQs (Pages 169–182)
  5. `Narration.json` — 11 MCQs (Pages 183–188)
  6. `Synonyms & Antonyms.json` — 159 MCQs (Pages 189–215)
  7. `Article.json` — 21 MCQs (Pages 216–218)
  8. `Degree.json` — 8 MCQs (Pages 218–219)
  9. `Conjunction & Verb.json` — 14 MCQs (Pages 219–220)
  10. `Preposition.json` — 153 MCQs (Pages 220–225)
  11. `Appropriate Sentence and Word.json` — 73 MCQs (Pages 225–228)
  12. `Translation.json` — 42 MCQs (Pages 228–233)
  13. `Word Meaning.json` — 63 MCQs (Pages 233–239)
  14. `Voice.json` — 21 MCQs (Pages 240–243)
  15. `Gender and Number.json` — 10 MCQs (Pages 243–244)
  16. `Idioms & Phrases.json` — 45 MCQs (Pages 244)
  17. `English Literature.json` — 57 MCQs (Pages 244–250)

### 3. General Knowledge (সাধারণ জ্ঞান) — IN PROGRESS
- **Source Range:** `p457.jpg` to `p750.jpg` (294 page images upright in `Images/BUET Patern/`, all 19 missing pages added)
- **Structure:** Page-by-page Python generation in `scripts/buet_gk_pages/` compiled into 5 Topic JSONs under `JSON Data/BUET Patern/GK/`.
- **Identified Topic Partitions:**
  1. `বাংলাদেশ বিষয়াবলি` (Pages 457–566) — **100% COMPLETED (799 MCQs, all 19 missing pages included)**
  2. `আন্তর্জাতিক বিষয়াবলি` (Pages 566–643) — **100% COMPLETED (604 MCQs)**
  3. `সাধারণ বিজ্ঞান` (Pages 643–677) — **100% COMPLETED (273 MCQs)**
  4. `কম্পিউটার ও তথ্য প্রযুক্তি` (Pages 678–696) — **100% COMPLETED (134 MCQs)**
  5. `পাওয়ার সেক্টর ও গ্যাস সেক্টর` (Pages 697–750) — **IN PROGRESS (15 MCQs up to Page 700; Next: Page 701, Q16)**
- **Completed So Far:** **244 pages mapped, 244 page scripts created (`page_457.py` to `page_700.py`), 1,825 MCQs compiled across 5 topic JSONs**

---

### 4. Math (গণিত)
- **Status:** Pending (Awaiting images/source material from user).

---

## 📚 Saif Sir NTRCA Suggestion - Conversion Progress

**Source PDF:** `PDF/Saif Sir NTRCA Suggestion/saif-sir-ntrca-suggestion.pdf`  
**Target Root:** `JSON Data/Saif Sir NTRCA Suggestion/`  
**Status:** **100% COMPLETED ACROSS ALL 4 SUBJECTS (338 JSON Files, 7,225 MCQs)**

### 1. Bangla (বাংলা) — 100% COMPLETED
- **Completed:** Model Test-01 through Model Test-111 (`Model Test-01.json` to `Model Test-111.json`)
- **Total MCQs:** **2,231 MCQs** (111 JSON files)

### 2. General Knowledge (জিকে) — 100% COMPLETED
- **Completed:** Model Test-01 through Model Test-99 (`Model Test-01.json` to `Model Test-99.json`)
- **Total MCQs:** **2,211 MCQs** (99 JSON files, Pages 80–162)

### 3. English (ইংরেজি) — 100% COMPLETED
- **Completed:** Model Test-01 through Model Test-97 + Model Test-46A
- **Total MCQs:** **2,034 MCQs** (98 JSON files, Pages 163–256)

### 4. Math (গণিত) — 100% COMPLETED
- **Completed:** Model Test-01 through Model Test-27 (including `03A`, `20A`, `23A`)
- **Total MCQs:** **749 MCQs** (30 JSON files, Pages 257–340)

---

## 🔍 Comprehensive Word-by-Word Quality Audit
- **Scope:** Every single JSON file across all subjects in Saif Sir NTRCA Suggestion and BUET Pattern.
- **Checks Performed:**
  - Foreign script / unicode corruption detection (Sinhala `ය`, Devanagari `संभाव্য`, `शब्द`).
  - Broken conjuncts and missing root letters (e.g. `√মুচ + ্ত` -> `√মৃচ + ক্ত`).
  - Typographic errors (stacked vowels `োা`, double kars `ৌৌ`, `াা`, `েে`, double hasanta `্্`).
  - Space/hyphen word splits (e.g. `দক্ষিণ- পূর্ব` -> `দক্ষিণ-পূর্ব`, `ই- কমার্স` -> `ই-কমার্স`).
  - Missing fill-in-the-blank tokens in English.
  - Option keys sanity and cross-validation against original image/PDF scans.
- **Result:** All files verified clean, syntactically valid JSON with full Bengali and English utf-8 encoding.

---

## ⚠️ Strict Rules & Commitments
- **NEVER run `git push` automatically or autonomously.**
- Only push to git when the user explicitly instructs you to push.
