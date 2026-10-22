import json

dbms_mcqs = [
  {
    "id": 1,
    "question": "DBMS-এর পূর্ণরূপ কী?",
    "options": [
      "Data Backup Management System",
      "Database Management Software",
      "Distributed Base Management System",
      "Database Management System"
    ],
    "answer": "ঘ"
  },
  {
    "id": 2,
    "question": "RDBMS-এ ডেটা সংরক্ষণের মূল কাঠামো কী?",
    "options": [
      "Document",
      "Graph",
      "Table",
      "Key-Value Pair"
    ],
    "answer": "গ"
  },
  {
    "id": 3,
    "question": "ডেটাবেসে একটি 'Row' কী নামে পরিচিত?",
    "options": [
      "Attribute",
      "Column",
      "Field",
      "Record"
    ],
    "answer": "ঘ"
  },
  {
    "id": 4,
    "question": "নিম্নের কোনটি NoSQL DBMS-এর প্রধান বৈশিষ্ট্য?",
    "options": [
      "Strict স্কিমা",
      "ডেটা টেবিল ও সম্পর্কের ব্যবহার",
      "Horizontal Scaling-কে সমর্থন",
      "SQL-এর বাধ্যতামূলক ব্যবহার"
    ],
    "answer": "গ"
  },
  {
    "id": 5,
    "question": "Hierarchical DBMS ডেটাকে কোন কাঠামোতে সংরক্ষণ করে?",
    "options": [
      "Network",
      "Tree",
      "Star",
      "Relational"
    ],
    "answer": "খ"
  },
  {
    "id": 6,
    "question": "ER ডায়াগ্রামে Entity বোঝাতে কোন প্রতীক ব্যবহৃত হয়?",
    "options": [
      "Diamond",
      "Ellipse",
      "Rectangle",
      "Double Rectangle"
    ],
    "answer": "গ"
  },
  {
    "id": 7,
    "question": "Weak Entity বোঝাতে কোন প্রতীক ব্যবহৃত হয়?",
    "options": [
      "Rectangle",
      "Diamond",
      "Double Rectangle",
      "Double Ellipse"
    ],
    "answer": "গ"
  },
  {
    "id": 8,
    "question": "একটি Entity-র বৈশিষ্ট্যকে কী বলা হয়?",
    "options": [
      "Relationship",
      "Attribute",
      "Record",
      "Key"
    ],
    "answer": "খ"
  },
  {
    "id": 9,
    "question": "যে Attribute-এর একাধিক মান থাকতে পারে (যেমন: একাধিক মোবাইল নম্বর), তাকে কী বলা হয়?",
    "options": [
      "Simple Attribute",
      "Composite Attribute",
      "Multi-Valued Attribute",
      "Derived Attribute"
    ],
    "answer": "গ"
  },
  {
    "id": 10,
    "question": "জন্ম তারিখ থেকে বয়স নির্ণয় করা গেলে, বয়স কোন ধরনের Attribute?",
    "options": [
      "Simple",
      "Derived",
      "Multi-Valued",
      "Composite"
    ],
    "answer": "খ"
  },
  {
    "id": 11,
    "question": "একাধিক Student একটি Course-এ Enrol করলে, এটি কোন ধরনের Relationship?",
    "options": [
      "One to One",
      "One to Many",
      "Many to One",
      "Many to Many"
    ],
    "answer": "ঘ"
  },
  {
    "id": 12,
    "question": "একটি রেকর্ডের অদ্বিতীয় বা ইউনিক সনাক্তকরণের জন্য ব্যবহৃত ফিল্ডকে কী বলে?",
    "options": [
      "Foreign Key",
      "Super Key",
      "Primary Key",
      "Alternate Key"
    ],
    "answer": "গ"
  },
  {
    "id": 13,
    "question": "একটি টেবিলের সমস্ত সম্ভাব্য ইউনিক কী-কে (যা Primary Key হতে পারত) কী বলে?",
    "options": [
      "Super Key",
      "Candidate Key",
      "Composite Key",
      "Foreign Key"
    ],
    "answer": "খ"
  },
  {
    "id": 14,
    "question": "Primary Key ছাড়া অন্যান্য Candidate Key গুলোকে কী বলা হয়?",
    "options": [
      "Super Key",
      "Alternate Key",
      "Composite Key",
      "Artificial Key"
    ],
    "answer": "খ"
  },
  {
    "id": 15,
    "question": "দুটি টেবিলের মধ্যে সম্পর্ক তৈরি করতে একটি টেবিলের Primary Key যখন অন্য টেবিলে ব্যবহৃত হয়, তখন সেটিকে কী বলে?",
    "options": [
      "Alternate Key",
      "Foreign Key",
      "Super Key",
      "Composite Key"
    ],
    "answer": "খ"
  },
  {
    "id": 16,
    "question": "ডেটাবেজ ডিজাইনে, যে কী স্বয়ংক্রিয়ভাবে তৈরি হয় এবং ডেটা টেবিলের কোনো প্রাকৃতিক Attribute নয়, তাকে কী বলে?",
    "options": [
      "Primary Key",
      "Foreign Key",
      "Artificial Key",
      "Composite Key"
    ],
    "answer": "গ"
  },
  {
    "id": 17,
    "question": "Normalization-এর প্রধান উদ্দেশ্য কী?",
    "options": [
      "ডেটা অ্যাক্সেসের গতি কমানো",
      "ডেটা রিডানডেন্সি (পুনরাবৃত্তি) দূর করা",
      "টেবিলের সংখ্যা বৃদ্ধি করা",
      "কোয়েরি প্রসেসিং জটিল করা"
    ],
    "answer": "খ"
  },
  {
    "id": 18,
    "question": "কোনো টেবিলে মাল্টি-ভ্যালুড অ্যাট্রিবিউট না থাকলে সেটিকে কোন Normal Form-এ বলা হয়?",
    "options": [
      "2NF",
      "1NF",
      "3NF",
      "BCNF"
    ],
    "answer": "খ"
  },
  {
    "id": 19,
    "question": "একটি টেবিল 1NF-এ আছে এবং এর সমস্ত নন-কী অ্যাট্রিবিউট প্রাইমারি কী-এর উপর সম্পূর্ণ নির্ভরশীল—এটি কোন Normal Form-এর শর্ত?",
    "options": [
      "2NF",
      "3NF",
      "1NF",
      "BCNF"
    ],
    "answer": "ক"
  },
  {
    "id": 20,
    "question": "কোন Normal Form এ Transitive Dependency (নন-কী অ্যাট্রিবিউটের ওপর নন-কী অ্যাট্রিবিউটের নির্ভরশীলতা) দূর করে?",
    "options": [
      "1NF",
      "2NF",
      "3NF",
      "BCNF"
    ],
    "answer": "গ"
  },
  {
    "id": 21,
    "question": "3NF-এর চেয়েও কঠোর এবং সমস্ত ফাংশনাল ডিপেন্ডেন্সি একটি সুপার কী-এর উপর নির্ভরশীল—এটি কোন Normal Form?",
    "options": [
      "2NF",
      "BCNF",
      "1NF",
      "3NF"
    ],
    "answer": "খ"
  },
  {
    "id": 22,
    "question": "SQL-এর পূর্ণরূপ কী?",
    "options": [
      "Systematic Query Language",
      "Simple Query Logic",
      "Structured Query Language",
      "Standard Query Logic"
    ],
    "answer": "গ"
  },
  {
    "id": 23,
    "question": "SQL-এ ডেটাবেসের কাঠামো পরিবর্তন করতে কোন কমান্ড ব্যবহৃত হয়?",
    "options": [
      "SELECT",
      "INSERT",
      "ALTER",
      "UPDATE"
    ],
    "answer": "গ"
  },
  {
    "id": 24,
    "question": "একটি টেবিল থেকে সমস্ত ডেটা এবং এর জন্য আলোকেট মেমরি মুছে ফেলার জন্য কোন DDL কমান্ড ব্যবহৃত হয়?",
    "options": [
      "DELETE",
      "DROP",
      "TRUNCATE",
      "REMOVE"
    ],
    "answer": "গ"
  },
  {
    "id": 25,
    "question": "একটি টেবিলে নতুন রেকর্ড যোগ করার জন্য কোন DML কমান্ড ব্যবহৃত হয়?",
    "options": [
      "INSERT",
      "ADD",
      "CREATE",
      "UPDATE"
    ],
    "answer": "ক"
  },
  {
    "id": 26,
    "question": "ডেটাবেস থেকে তথ্য 'Query' করার জন্য কোন কমান্ড ব্যবহৃত হয়?",
    "options": [
      "INSERT",
      "UPDATE",
      "SELECT",
      "CREATE"
    ],
    "answer": "গ"
  },
  {
    "id": 27,
    "question": "কোনো ব্যবহারকারীকে ডেটাবেসের অ্যাক্সেস অধিকার দেওয়ার জন্য কোন DCL কমান্ড ব্যবহৃত হয়?",
    "options": [
      "GRANT",
      "ALLOW",
      "REVOKE",
      "PERMIT"
    ],
    "answer": "ক"
  },
  {
    "id": 28,
    "question": "ট্রানজেকশন সফলভাবে সম্পন্ন করে পরিবর্তনগুলিকে স্থায়ীভাবে সেভ করার জন্য কোন TCL কমান্ড ব্যবহৃত হয়?",
    "options": [
      "BEGIN",
      "COMMIT",
      "SAVEPOINT",
      "ROLLBACK"
    ],
    "answer": "খ"
  },
  {
    "id": 29,
    "question": "কোনো ত্রুটি ঘটলে ট্রানজেকশনের সমস্ত কাজ বাতিল করে পূর্ববর্তী অবস্থায় ফিরে যাওয়ার জন্য কোন TCL কমান্ড ব্যবহৃত হয়?",
    "options": [
      "COMMIT",
      "ROLLBACK",
      "SAVEPOINT",
      "END"
    ],
    "answer": "খ"
  },
  {
    "id": 30,
    "question": "নিচের কোন কমান্ডটি DML-এর অন্তর্ভুক্ত?",
    "options": [
      "CREATE",
      "ALTER",
      "UPDATE",
      "REVOKE"
    ],
    "answer": "গ"
  },
  {
    "id": 31,
    "question": "3-Tier Architecture-এ সাধারণ ব্যবহারকারীরা কোন স্তরে কাজ করেন?",
    "options": [
      "ডেটাবেস টায়ার",
      "অ্যাপ্লিকেশন টায়ার",
      "প্রেজেন্টেশন টায়ার",
      "ফিজিক্যাল টায়ার"
    ],
    "answer": "গ"
  },
  {
    "id": 32,
    "question": "ডেটাবেস কাঠামোর লজিক্যাল উপস্থাপনাকে কী বলা হয়?",
    "options": [
      "Instance",
      "Schema",
      "View",
      "Repository"
    ],
    "answer": "খ"
  },
  {
    "id": 33,
    "question": "3-Tier Architecture-এ অ্যাপ্লিকেশন সার্ভার এবং ডেটাবেসে অ্যাক্সেস করা প্রোগ্রামগুলো কোন স্তরে থাকে?",
    "options": [
      "ডেটাবেস টায়ার",
      "প্রেজেন্টেশন টায়ার",
      "অ্যাপ্লিকেশন টায়ার",
      "ইউজার টায়ার"
    ],
    "answer": "গ"
  },
  {
    "id": 34,
    "question": "DBMS-এর তুলনায় ফাইল সিস্টেমে একটি প্রধান দুর্বলতা কী?",
    "options": [
      "কম জটিলতা",
      "ডেটা পুনরাবৃত্তি",
      "কম ব্যয়",
      "কম নিরাপত্তা"
    ],
    "answer": "খ"
  },
  {
    "id": 35,
    "question": "DBMS-এ ডেটা অ্যাক্সেসের গতি বৃদ্ধি করতে কোনটি ব্যবহৃত হতে পারে?",
    "options": [
      "View",
      "Schema",
      "Index",
      "Stored Procedure"
    ],
    "answer": "গ"
  },
  {
    "id": 36,
    "question": "একটি ট্রানজেকশন প্রাথমিক অবস্থায় আছে এবং এখনও সম্পন্ন হয়নি—এটি কোন State?",
    "options": [
      "Committed",
      "Active",
      "Partially Committed",
      "Failed"
    ],
    "answer": "খ"
  },
  {
    "id": 37,
    "question": "ট্রানজেকশনের সমস্ত অপারেশন সম্পন্ন হয়েছে, কিন্তু এখনও ডেটা স্থায়ীভাবে সংরক্ষিত হয়নি—এটি কোন State?",
    "options": [
      "Active",
      "Partially Committed",
      "Aborted",
      "Committed"
    ],
    "answer": "খ"
  },
  {
    "id": 38,
    "question": "ACID Properties-এর 'A' দ্বারা কী বোঝানো হয়?",
    "options": [
      "Availability",
      "Authenticity",
      "Atomicity",
      "Accessibility"
    ],
    "answer": "গ"
  },
  {
    "id": 39,
    "question": "ACID Properties-এর 'I' দ্বারা কী বোঝানো হয়?",
    "options": [
      "Interaction",
      "Isolation",
      "Integrity",
      "Indexing"
    ],
    "answer": "খ"
  },
  {
    "id": 40,
    "question": "একটি ট্রানজেকশন সফল হলে ডেটাবেসের অবস্থাটি যেন অপরিবর্তিত থাকে—ACID-এর কোন ধর্ম এটি নিশ্চিত করে?",
    "options": [
      "Atomicity",
      "Isolation",
      "Consistency",
      "Durability"
    ],
    "answer": "গ"
  },
  {
    "id": 41,
    "question": "মানুষের পঠনযোগ্য ডেটাকে কী বলা হয়?",
    "options": [
      "Ciphertext",
      "Private Key",
      "Plain Text",
      "Public Key"
    ],
    "answer": "গ"
  },
  {
    "id": 42,
    "question": "এনক্রিপশন অ্যালগরিদম এবং একটি কী ব্যবহার করে প্লেইন টেক্সটকে অপঠনযোগ্য ফরম্যাটে রূপান্তর করার প্রক্রিয়াকে কী বলে?",
    "options": [
      "Decryption",
      "Hashing",
      "Data Encryption",
      "Key Generation"
    ],
    "answer": "গ"
  },
  {
    "id": 43,
    "question": "Symmetric Encryption পদ্ধতিতে এনক্রিপশন এবং ডিক্রিপশনের জন্য কোনটি ব্যবহৃত হয়?",
    "options": [
      "দুটি ভিন্ন কী",
      "দুটি Public Key",
      "একই কী",
      "কোনো কী নয়"
    ],
    "answer": "গ"
  },
  {
    "id": 44,
    "question": "Asymmetric Encryption পদ্ধতিতে কোনটি ব্যবহৃত হয়?",
    "options": [
      "Private Key",
      "Public Key ও Private Key",
      "একটি Common Key",
      "শুধু Private Key"
    ],
    "answer": "খ"
  },
  {
    "id": 45,
    "question": "নিম্নের কোনটি একটি বহুল ব্যবহৃত সিমেট্রিক এনক্রিপশন প্রযুক্তি?",
    "options": [
      "AES",
      "RSA",
      "SHA",
      "DES"
    ],
    "answer": "ক"
  },
  {
    "id": 46,
    "question": "নিম্নের কোনটি একটি বহুল ব্যবহৃত অ্যাসিমেট্রিক এনক্রিপশন প্রযুক্তি?",
    "options": [
      "AES",
      "RSA",
      "SHA",
      "Blowfish"
    ],
    "answer": "খ"
  },
  {
    "id": 47,
    "question": "পাসওয়ার্ড এবং অন্যান্য সংবেদনশীল তথ্যকে আনরিডেবল ফরম্যাটে সংরক্ষণ করতে সাধারণত কোন প্রযুক্তি ব্যবহৃত হয়?",
    "options": [
      "Encryption",
      "Decryption",
      "Hashing",
      "Symmetric Key"
    ],
    "answer": "গ"
  },
  {
    "id": 48,
    "question": "Double Ellipse (দ্বিগুণ উপবৃত্ত) E-R ডায়াগ্রামে কী বোঝাতে ব্যবহৃত হয়?",
    "options": [
      "Primary Key",
      "Derived Attribute",
      "Multi-Valued Attribute",
      "Composite Attribute"
    ],
    "answer": "গ"
  },
  {
    "id": 49,
    "question": "DBMS-এ JOIN অপারেশনটি কী জন্য ব্যবহৃত হয়?",
    "options": [
      "টেবিল তৈরি করা",
      "ডেটা মুছে ফেলা",
      "একাধিক টেবিল থেকে ডেটা একত্রিত করা",
      "নতুন রেকর্ড যোগ করা"
    ],
    "answer": "গ"
  },
  {
    "id": 50,
    "question": "একটি ডেটাবেস টেবিলে Column কী নামে পরিচিত?",
    "options": [
      "Record",
      "Tuple",
      "Attribute",
      "Entity"
    ],
    "answer": "গ"
  }
]

with open('JSON Data/BPSC ICT Wizard/6. DBMS.json', 'w', encoding='utf-8') as f:
    json.dump(dbms_mcqs, f, ensure_ascii=False, indent=2)

print('Saved 6. DBMS.json with', len(dbms_mcqs), 'MCQs')
