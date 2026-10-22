# -*- coding: utf-8 -*-
"""
Generate JSON for 'BCS Computer পার্ট.pdf'
Extracts only MCQ questions (question, options, answer).
"""
import os
import sys
import json

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

questions = [
    {
        "id": 1,
        "question": "ফায়ারওয়ালের প্রাথমিক কাজ কী?",
        "options": [
            "সমস্ত আগত ট্রাফিক ফিল্টার করা",
            "সমস্ত বহির্গত ট্রাফিক ব্লক করা",
            "আগত এবং বহির্গত নেটওয়ার্ক ট্রাফিক নিরীক্ষা এবং নিয়ন্ত্রণ করা।",
            "সমস্ত নেটওয়ার্ক ট্রাফিক এনক্রিপ্ট করা।"
        ],
        "answer": "C"
    },
    {
        "id": 2,
        "question": "ইন্টারনেটের মাধ্যমে তথ্য আদান-প্রদানের জন্য সর্বাধিক ব্যবহৃত প্রোটোকল কী?",
        "options": [
            "HTTP",
            "FTP",
            "DNS",
            "TCP/IP"
        ],
        "answer": "D"
    },
    {
        "id": 3,
        "question": "নিচের কোনটি ক্লাউড কম্পিউটিং এর বৈশিষ্ট্য নয়?",
        "options": [
            "On-demand self service",
            "Broad network access",
            "Limited customization",
            "Physical ownership of servers"
        ],
        "answer": "D"
    },
    {
        "id": 4,
        "question": "একটি কম্পিউটার নেটওয়ার্কে একটি LAN-এর একাধিক ডিভাইসকে একটি WAN এর সাথে সংযুক্ত করে এমন ডিভাইস কোনটি?",
        "options": [
            "রাউটার",
            "ওয়েব সার্ভার",
            "ব্রীজ",
            "হাব"
        ],
        "answer": "A"
    },
    {
        "id": 5,
        "question": "প্রতারণামূলকভাবে সংবেদনশীল তথ্য যেমন পাসওয়ার্ড ও ক্রেডিট কার্ড নম্বর অর্জন করার জন্য ইন্টারনেট ব্যবহার করার অনুশীলনকে কী বলা হয়?",
        "options": [
            "Phishing",
            "Spamming",
            "Ransom ware",
            "Sniffing"
        ],
        "answer": "A"
    },
    {
        "id": 6,
        "question": "চিকিৎসা ক্ষেত্রে কম্পিউটার এর কাজ কোনটি?",
        "options": [
            "তথ্য সংরক্ষণ",
            "ইমেজ বিশ্লেষণ",
            "রোগী পর্যবেক্ষণ",
            "উপরের সবগুলো"
        ],
        "answer": "D"
    },
    {
        "id": 7,
        "question": "নিচের কোনটি সার্বজনীন ডিজিটাল লজিক গেইট?",
        "options": [
            "XOR",
            "AND",
            "NOR",
            "OR"
        ],
        "answer": "C"
    },
    {
        "id": 8,
        "question": "GPU-এর পূর্ণরূপ কী?",
        "options": [
            "Graph Processing Unit",
            "Graphic Processing Unit",
            "Graphics Processing Unit",
            "Geographical Processing Unit"
        ],
        "answer": "C"
    },
    {
        "id": 9,
        "question": "নিচের কোনটি ALU-এর আউটপুট রাখার জন্য ব্যবহৃত হয়?",
        "options": [
            "Register",
            "ROM",
            "Flags",
            "Output Unit"
        ],
        "answer": "A"
    },
    {
        "id": 10,
        "question": "DBMS-এর পূর্ণরূপ কী?",
        "options": [
            "Data Backup Management Service",
            "Database Management System",
            "Data of Binary Management System",
            "Database Management System"
        ],
        "answer": "C"
    },
    {
        "id": 11,
        "question": "2 কিলোবাইট মেমোরি address করার জন্য কতটি address লাইন দরকার?",
        "options": [
            "12",
            "10",
            "11",
            "14"
        ],
        "answer": "C"
    },
    {
        "id": 12,
        "question": "এমবেডেড সিস্টেমে সাধারণত কোন ধরনের মেমোরি ব্যবহৃত হয়?",
        "options": [
            "RAM",
            "হার্ডডিস্ক ড্রাইভ",
            "ফ্লাশ মেমোরি",
            "অপটিক্যাল ডিস্ক ড্রাইভ"
        ],
        "answer": "C"
    },
    {
        "id": 13,
        "question": "নিচের কোনটি Spyware এর উদাহরণ?",
        "options": [
            "Key loggers",
            "Avast",
            "Norton",
            "Kasparasky"
        ],
        "answer": "A"
    },
    {
        "id": 14,
        "question": "IPv4-এ নিচের কোনটি Google DNS Server এর IP Address?",
        "options": [
            "8.8.7.6",
            "8.7.8.6",
            "8.8.8.6",
            "8.8.8.8"
        ],
        "answer": "D"
    },
    {
        "id": 15,
        "question": "(2FA)₁₆ এই হেক্সাডেসিমেল সংখ্যাটিকে অক্টালে রূপান্তর করুন :",
        "options": [
            "(762)",
            "(1372)",
            "(228)",
            "(1482)"
        ],
        "answer": "B"
    },
    {
        "id": 16,
        "question": "অ্যামাজন এর ক্লাউড প্ল্যাটফর্ম কোনটি?",
        "options": [
            "Azure",
            "AWS",
            "Cloudera",
            "উপরের সবগুলো"
        ],
        "answer": "B"
    },
    {
        "id": 17,
        "question": "নিচের কোন সাইবার আক্রমণ সংঘটিত হলে গ্রাহক নিজ Computer system ব্যবহার করতে পারেন না এবং Computer System কে ব্যবহার উপযোগী করতে অর্থ দাবি করা হয়?",
        "options": [
            "Phising",
            "Denial of Service",
            "Ransomware",
            "Man-in-the Middle"
        ],
        "answer": "C"
    },
    {
        "id": 18,
        "question": "SCSI এর পূর্ণরূপ কী?",
        "options": [
            "Small Computer System Interface",
            "Small Computer Software Interface",
            "Small Computer Storage Interface",
            "Small Computer Standard Interface"
        ],
        "answer": "A"
    },
    {
        "id": 19,
        "question": "নিচের কোন ডিভাইসটি ইনপুট ও আউটপুট ডিভাইস হিসেবে কাজ করে?",
        "options": [
            "Scanner",
            "Mouse",
            "Touch Screen",
            "Projector"
        ],
        "answer": "C"
    },
    {
        "id": 20,
        "question": "নিচের কোন Octal সংখ্যাটি Decimal সংখ্যা ৫৫ এর সমতুল্য?",
        "options": [
            "৫৫",
            "৭৭",
            "৬৭",
            "৮৭"
        ],
        "answer": "C"
    },
    {
        "id": 21,
        "question": "নিচের কোনটি System software নয়?",
        "options": [
            "Linux",
            "Andrid",
            "Mozilla Firefox",
            "Apple iOS"
        ],
        "answer": "C"
    },
    {
        "id": 22,
        "question": "নিচের কোন protocol টি ইন্টারনেটে তথ্য আদান প্রদানে নিরাপত্তা নিশ্চিত করে থাকে?",
        "options": [
            "FTP",
            "HTTPS",
            "TCP",
            "DNS"
        ],
        "answer": "B"
    },
    {
        "id": 23,
        "question": "Piconet কী?",
        "options": [
            "Wifi Network",
            "Wide Area Netware",
            "Bluetooth Network",
            "5G Network"
        ],
        "answer": "C"
    },
    {
        "id": 24,
        "question": "এক মেশিন থেকে অন্য মেশিনে ইমেইল মেসেজ স্থানান্তর করতে কোন TCP/IP প্রোটোকল ব্যবহার হয়?",
        "options": [
            "FTP",
            "RPC",
            "SNMP",
            "SMTP"
        ],
        "answer": "D"
    },
    {
        "id": 25,
        "question": "যে কম্পিউটার প্রোগ্রাম নিজে নিজেই অন্য কম্পিউটারে ইন্টারনেটের মাধ্যমে কপি করা হয় তাকে ........বলে।",
        "options": [
            "Program Virus",
            "Worms",
            "Trojan Horse",
            "Boot Virus"
        ],
        "answer": "B"
    },
    {
        "id": 26,
        "question": "নিচের কোন প্রতিষ্ঠানটি 4G Standard প্রস্তুতকরণে সম্পৃক্ত?",
        "options": [
            "ISO",
            "ITU",
            "3GPP",
            "ETSI"
        ],
        "answer": "C"
    },
    {
        "id": 27,
        "question": "নিচের কোনটি Open Source Software ?",
        "options": [
            "Google Chrome",
            "Microsoft Windows",
            "Zoom",
            "Adobe Photoshop"
        ],
        "answer": "A"
    },
    {
        "id": 28,
        "question": "নিচের কোনটি Structured Query Language নয়?",
        "options": [
            "Java",
            "MySQL",
            "Oracle",
            "উপরের সবগুলো"
        ],
        "answer": "A"
    },
    {
        "id": 29,
        "question": "ইন্টারনেট যোগাযোগ ব্যবস্থায় Hostname- কে IP Address-এ অনুবাদ করে-",
        "options": [
            "FTP",
            "Firewall",
            "DNS Server",
            "Gateway"
        ],
        "answer": "C"
    },
    {
        "id": 30,
        "question": "নিচের কোন মডেলটি Clould Computing সেবা প্রদানকারীগণ ব্যবহার করে না?",
        "options": [
            "Caas",
            "laas",
            "Paas",
            "SaaS"
        ],
        "answer": "A"
    },
    {
        "id": 31,
        "question": "নিচের কোনটি anti- virus সফটওয়্যার নয়?",
        "options": [
            "Oracle",
            "McAfee",
            "Norton",
            "Kaspersky"
        ],
        "answer": "A"
    },
    {
        "id": 32,
        "question": "RFID বলতে বোঝায়-",
        "options": [
            "Randm Frequesncy Identification",
            "Random Frequesncy Information",
            "Radio Frequency Information",
            "Radio Frequency Identification"
        ],
        "answer": "D"
    },
    {
        "id": 33,
        "question": "কোন চিহ্নটি- ই মেইল ঠিকানায় অবশ্যই থাকবে?",
        "options": [
            "$",
            "#",
            "&",
            "@"
        ],
        "answer": "D"
    },
    {
        "id": 34,
        "question": "১০১১১০ বাইনারি নাম্বারের সমতুল্য ডেসিমাল নাম্বার কোনটি?",
        "options": [
            "৪৬",
            "১৬",
            "২৪",
            "৫৪"
        ],
        "answer": "A"
    },
    {
        "id": 35,
        "question": "DNS সার্ভারের কাজ হচ্ছে Domain name কে IP address এ পরিবর্তন করা-",
        "options": [
            "Email, DNS কে IP address এ পরিবর্তন করা-",
            "MAC Address, IP",
            "Domain name, IP",
            "Email, IP"
        ],
        "answer": "C"
    },
    {
        "id": 36,
        "question": "নিচের কোনটি output device নয়?",
        "options": [
            "Monitor",
            "Microphone",
            "printer",
            "speaker"
        ],
        "answer": "B"
    },
    {
        "id": 37,
        "question": "নিচের কোনটি একটি প্রতিষ্ঠানের ওয়েব ঠিকানাকে নির্দেশ করে?",
        "options": [
            "http",
            "www",
            "URL",
            "HTML"
        ],
        "answer": "C"
    },
    {
        "id": 38,
        "question": "নিচের কোন প্রযুক্তি 'Pay as You Go' সার্ভিস মডেল অনুসরণ করে?",
        "options": [
            "Internet of things (IoT)",
            "Cloud Computing",
            "Client -Server Systems",
            "Big Data Analytics"
        ],
        "answer": "B"
    },
    {
        "id": 39,
        "question": "যে সাইবার আক্রমণ সংঘটিত হলে গ্রাহকের বৈধ অনুরোধসমূহ কোন একটি Web server সম্পূর্ণ করতে ব্যর্থ হয় সেটি কী নামে পরিচিত?",
        "options": [
            "Phishing",
            "Man-in-the Middle",
            "Denial of Service",
            "উপরের কোনটিই নয়"
        ],
        "answer": "C"
    },
    {
        "id": 40,
        "question": "নিচের Job Scheduling Policy সমূহের কোনটি Starvation থেকে মুক্ত?",
        "options": [
            "Priority Scheduling",
            "Shortest Job First",
            "Yungest Job First",
            "Round -robin"
        ],
        "answer": "D"
    },
    {
        "id": 41,
        "question": "নিচের কোন প্রযুক্তি Face Recognition System এর সহায়ক ভূমিকা পালন করে?",
        "options": [
            "Applied Artificial Intelligence (AI)",
            "Applied Internet of things (IoT)",
            "Virtual Reality",
            "উপরের কোনটিই নয়"
        ],
        "answer": "A"
    },
    {
        "id": 42,
        "question": "নিচের কোন মেমোরিটিতে Access Time সবচেয়ে কম?",
        "options": [
            "Registers",
            "SSD",
            "RAM",
            "Cache Memory"
        ],
        "answer": "A"
    },
    {
        "id": 43,
        "question": "নিচের কোন ডিভাইসটি ডিজিটাল সিগন্যাল অন্যালগ সিগন্যালে পরিবর্তনে ব্যবহৃত হয়?",
        "options": [
            "Router",
            "Switch",
            "Modem",
            "HUB"
        ],
        "answer": "C"
    },
    {
        "id": 44,
        "question": "Keyboard এবং CPU এর মধ্যে কোন পদ্ধতিতে data transmission হয়?",
        "options": [
            "Simplex",
            "Duplex",
            "Half Duplex",
            "Triplex"
        ],
        "answer": "A"
    },
    {
        "id": 45,
        "question": "Blockchain এর প্রতিটি block কী তথ্য বহন করে?",
        "options": [
            "A hash pointer to the previous block",
            "Timestamp",
            "List of transactions",
            "উপরের সবগুলো"
        ],
        "answer": "D"
    },
    {
        "id": 46,
        "question": "নিচের কোনটি Bluetooth এর IEEE standard?",
        "options": [
            "IEEE 802.15",
            "IEEE 802.1",
            "IEEE 802.3",
            "IEEE 802.11"
        ],
        "answer": "A"
    },
    {
        "id": 47,
        "question": "নিচের কোনটি Multi- tasking operating system নয়?",
        "options": [
            "Windows",
            "Linux",
            "Windows NT",
            "DOS"
        ],
        "answer": "D"
    },
    {
        "id": 48,
        "question": "নিচের কোনটি Open Source DBMS ?",
        "options": [
            "MySQL",
            "Microsoft SQL Server",
            "Microsoft Access",
            "Oracle"
        ],
        "answer": "A"
    },
    {
        "id": 49,
        "question": "যে ইলেক্ট্রনিক লজিক গেইটের আউটপুট লজিক 1 শুধুমাত্র যখন সকল ইনপুট লজিক 1 তার নাম",
        "options": [
            "AND গেইট",
            "OR গেইট",
            "NAND গেইট",
            "কোনটিই নয়"
        ],
        "answer": "A"
    },
    {
        "id": 50,
        "question": "নিচের কোনটির যোগাযোগের দূরত্ব সবচেয়ে কম কত?",
        "options": [
            "Wi-Fi",
            "Cellular network",
            "Wi-Max",
            "Bluetooth"
        ],
        "answer": "D"
    },
    {
        "id": 51,
        "question": "নিচের কোনটি ১০০ এর ১ কমপ্লিমেন্ট?",
        "options": [
            "111",
            "101",
            "011",
            "011"
        ],
        "answer": "C"
    },
    {
        "id": 52,
        "question": "RFID বলতে বুঝায়-",
        "options": [
            "Random Frequency Identification",
            "Random Frequency Information",
            "Radio Frequency Information",
            "Radio Frequency Identification"
        ],
        "answer": "D"
    },
    {
        "id": 53,
        "question": "Apache এক ধরনের",
        "options": [
            "Database Management System (DBMS)",
            "Web Server",
            "Web Browser",
            "Protocol"
        ],
        "answer": "B"
    },
    {
        "id": 54,
        "question": "নিচের কোনটি সঠিক নয়?",
        "options": [
            "\\overline{A+B} = \\bar{A} + \\bar{B}",
            "\\overline{AB} = \\bar{A} + \\bar{B}",
            "\\overline{A+B} = \\bar{A} \\cdot \\bar{B}",
            "\\overline{AB} = \\bar{A} \\cdot \\bar{B}"
        ],
        "answer": "B"
    },
    {
        "id": 55,
        "question": "ক্লাউড কম্পিউটিং এর সার্ভিস মডেল কোনটি?",
        "options": [
            "অবকাঠামোগত",
            "প্ল্যাটফর্মভিত্তিক",
            "সফটওয়্যার",
            "সবগুলো"
        ],
        "answer": "D"
    },
    {
        "id": 56,
        "question": "কোন নেটওয়ার্ক টপোলজিতে হাব (hub) ব্যবহার করা হয়?",
        "options": [
            "বাস টপোলজি",
            "রিং টপোলজি",
            "স্টার টপোলজি",
            "ট্রি টপোলজি"
        ],
        "answer": "C"
    },
    {
        "id": 57,
        "question": "একটি কম্পিউটার Boot করতে পারে না যদি তাতে না থাকে-",
        "options": [
            "compiler",
            "loader",
            "operating system",
            "bootstrap"
        ],
        "answer": "C"
    },
    {
        "id": 58,
        "question": "নিচের কোনটি Anti-virus সফটওয়্যার নয়?",
        "options": [
            "Oracle",
            "McAfee",
            "Norton",
            "Kaspersky"
        ],
        "answer": "A"
    },
    {
        "id": 59,
        "question": "যে কম্পিউটার ভাষায় সবকিছু শুধুমাত্র বাইনারি কোডে লেখা হয় তাকে বলে-",
        "options": [
            "Machine language",
            "C",
            "Java",
            "Python"
        ],
        "answer": "A"
    },
    {
        "id": 60,
        "question": "API মানে-",
        "options": [
            "Advanced Processing Information",
            "Application Processing Information",
            "Application Programming Interface",
            "Application Processing Interface"
        ],
        "answer": "C"
    },
    {
        "id": 61,
        "question": "মাইক্রোসফট IIS হচ্ছে একটি-",
        "options": [
            "ইমেইল সার্ভার",
            "ওয়েব সার্ভার",
            "ডাটাবেইস সার্ভার",
            "ফাইল সার্ভার"
        ],
        "answer": "B"
    },
    {
        "id": 62,
        "question": "ব্লুটুথ কত দূরত্ব পর্যন্ত কাজ করে?",
        "options": [
            "১০-৩০ মিটার",
            "১০-৫০ মিটার",
            "১০-১০০ মিটার",
            "১০-৩০০ মিটার"
        ],
        "answer": "C"
    },
    {
        "id": 63,
        "question": "একটি সিস্টেম যেখানে আইটেমগুলো এক প্রান্তে সংযোজিত হয় কিন্তু অন্য প্রান্ত থেকে সরানো হয় তার নাম-",
        "options": [
            "Array",
            "Linked list",
            "Stack",
            "Queue"
        ],
        "answer": "D"
    },
    {
        "id": 64,
        "question": "H. 323 Protocol সাধারণত কি কাজে ব্যবহৃত হয়?",
        "options": [
            "File transfer",
            "VoIP",
            "Data Security",
            "File download"
        ],
        "answer": "B"
    },
    {
        "id": 65,
        "question": "মুদ্রিত লেখা সরাসরি ইনপুট নেয়ার জন্য নীচের কোনটি ব্যবহৃত হয়?",
        "options": [
            "OMR",
            "OCR",
            "MICR",
            "Scanner"
        ],
        "answer": "B"
    },
    {
        "id": 66,
        "question": "একটি রিলেশনাল ডাটাবেস মডেলে নীচের কোনটি দ্বারা Relation প্রকাশ করা হয়?",
        "options": [
            "Tuples",
            "Attributes",
            "Tables",
            "Rows"
        ],
        "answer": "C"
    },
    {
        "id": 67,
        "question": "Bluetooth কিসের উদাহরণ?",
        "options": [
            "Personal Area Network",
            "Local Area Network",
            "Virtual Private Network",
            "কোনটি নয়"
        ],
        "answer": "A"
    },
    {
        "id": 68,
        "question": "মোবাইল ফোনে কোন Mode এর যোগাযোগ হয়?",
        "options": [
            "Simplex",
            "Half-duplex",
            "Full -duplex",
            "কোনটি নয়"
        ],
        "answer": "C"
    },
    {
        "id": 69,
        "question": "Firewall কি protection দেয়ার জন্য ব্যবহৃত হয়?",
        "options": [
            "Fire attacks",
            "Unauthorized access",
            "Virus attacks",
            "Data driven attack"
        ],
        "answer": "B"
    },
    {
        "id": 70,
        "question": "TV remote এর Carrier frequency -র range কত?",
        "options": [
            "100 MHZ",
            "1 GHZ",
            "2 GHZ",
            "Infra-red range এর"
        ],
        "answer": "D"
    },
    {
        "id": 71,
        "question": "নীচের কোনটি Octal number নয়?",
        "options": [
            "19",
            "77",
            "15",
            "101"
        ],
        "answer": "A"
    },
    {
        "id": 72,
        "question": "Time-shared OS- এর জন্য কোন sheduling policy সবচেয়ে ভাল?",
        "options": [
            "First come first serve",
            "Round-robin",
            "Shortest job first",
            "Last come first serve"
        ],
        "answer": "B"
    },
    {
        "id": 73,
        "question": "নীচের কোনটি ৫২₍₁₆₎ এর বাইনারী রূপ?",
        "options": [
            "0101 0010₍₂₎",
            "0111 0011₍₂₎",
            "0000 1100₍₂₎",
            "1111 0000₍₂₎"
        ],
        "answer": "A"
    },
    {
        "id": 74,
        "question": "প্রথম Web browser কোনটি?",
        "options": [
            "Netscape Navigator",
            "World Wide Web",
            "Internet Ecplorer",
            "Safari"
        ],
        "answer": "B"
    },
    {
        "id": 75,
        "question": "Social Networking Site এ যোগাযোগে কোন media ব্যবহৃত হয়?",
        "options": [
            "image/video",
            "Audio",
            "Text",
            "উপরের সবগুলো"
        ],
        "answer": "D"
    },
    {
        "id": 76,
        "question": "CPU কোন address generate করে?",
        "options": [
            "Physical address",
            "Logical Address",
            "Both physical and logical addresses",
            "উপরের কোনটি নয়"
        ],
        "answer": "B"
    },
    {
        "id": 77,
        "question": "নীচের কোন প্রোগ্রামটি একটি সম্পূর্ণ কম্পিউটার প্রোগ্রামকে একবারে অনুবাদ ও সম্পাদন করে?",
        "options": [
            "Interpreter",
            "Emulator",
            "Compiler",
            "Simulator"
        ],
        "answer": "C"
    },
    {
        "id": 78,
        "question": "নীচের কোনটি একই সাথে ইনপুট ও আউটপুট হিসেবে কাজ করে?",
        "options": [
            "Mouse",
            "Microphone",
            "Touch Screen",
            "Printer"
        ],
        "answer": "C"
    },
    {
        "id": 79,
        "question": "কম্পিউটার থেকে কম্পিউটারে তথ্য আদান-প্রদানের প্রযুক্তিকে বলা হয়",
        "options": [
            "ইন্টারকম",
            "ইন্টারনেট",
            "ই-মেইল",
            "ইন্টারসীড"
        ],
        "answer": "B"
    },
    {
        "id": 80,
        "question": "ই-মেইল গ্রহণ করার অধিক ব্যবহৃত প্রোটকল কোনটি?",
        "options": [
            "POP3",
            "POP9",
            "HTML",
            "SMTP"
        ],
        "answer": "A"
    },
    {
        "id": 81,
        "question": "কোনটি সঠিক নয়?",
        "options": [
            "A + 0 = A",
            "A . 1 = A",
            "A + Ā = 1",
            "A . Ā = 1"
        ],
        "answer": "D"
    },
    {
        "id": 82,
        "question": "এক word কত বিট বিশিষ্ট হয়?",
        "options": [
            "8",
            "16",
            "4",
            "2"
        ],
        "answer": "B"
    },
    {
        "id": 83,
        "question": "কোন ধরনের bus ব্যবহৃত হয় না?",
        "options": [
            "address bus",
            "input-reader bus",
            "data bus",
            "control bus"
        ],
        "answer": "B"
    },
    {
        "id": 84,
        "question": "ROM ভিত্তিক প্রোগ্রামের নাম কি?",
        "options": [
            "malware",
            "firmware",
            "virus",
            "lip-lop"
        ],
        "answer": "B"
    },
    {
        "id": 85,
        "question": "একটি লজিক গেট-এর আউটপুট 1 হয় যখন এর সব ইনপুট ০ থাকে। এই গেটটি--",
        "options": [
            "AND",
            "OR",
            "XOR",
            "NAND"
        ],
        "answer": "D"
    },
    {
        "id": 86,
        "question": "কোনটি মাইক্রোসফটের প্রথম প্রোগ্রাম?",
        "options": [
            "Windows XP",
            "Windows 98",
            "MS DOS",
            "Windows 7"
        ],
        "answer": "C"
    },
    {
        "id": 87,
        "question": "ডিস্ক ডিফ্রাগমেন্টেশান ব্যবহৃত হয়",
        "options": [
            "ভাইরাস ধ্বংসের জন্য",
            "খারাপ সেক্টরসমূহ পরীক্ষা করতে",
            "ডিস্কের ফাইলগুলোকে পুনর্বিন্যস্ত করতে",
            "ডিস্ক ফরমেট করতে"
        ],
        "answer": "C"
    },
    {
        "id": 88,
        "question": "কোন সাইটটি কেনা-বেচার জন্য নয়?",
        "options": [
            "ekhanei.com",
            "olx.com",
            "google.com",
            "amazon.com"
        ],
        "answer": "C"
    },
    {
        "id": 89,
        "question": "কম্পিউটার নেটওয়ার্ক OSI মডেলের স্তর কয়টি?",
        "options": [
            "৭",
            "৫",
            "৯",
            "৮"
        ],
        "answer": "A"
    },
    {
        "id": 90,
        "question": "কোন প্রোটোকলটি ইন্টারনেট সংযোগের ক্ষেত্রে সর্বাধিক ব্যবহৃত হয়?",
        "options": [
            "TCP/IP",
            "Novel Netware",
            "Net BEUI",
            "Linux"
        ],
        "answer": "A"
    },
    {
        "id": 91,
        "question": "কোন চিহ্নটি ই-মেইল ঠিকানায় অবশ্যই থাকবে?",
        "options": [
            "$",
            "#",
            "&",
            "@"
        ],
        "answer": "D"
    },
    {
        "id": 92,
        "question": "নিচের কোনটি সামঞ্জস্যপূর্ণ নয়?",
        "options": [
            "ফেসবুক",
            "টুইটার",
            "লিংকড ইন",
            "উইকিপিডিয়া"
        ],
        "answer": "D"
    },
    {
        "id": 93,
        "question": "10101111 এর 1's complement কোনটি?",
        "options": [
            "1111 1111",
            "0000 0000",
            "0101 0000",
            "1100 0011"
        ],
        "answer": "C"
    },
    {
        "id": 94,
        "question": "কোন মাধ্যমে আলোর পালস ব্যবহৃত হয়?",
        "options": [
            "তামার তার",
            "কো-এক্সিয়াল ক্যাবল",
            "অপটিক্যাল ফাইবার",
            "ওয়ারলেস মিডিয়া"
        ],
        "answer": "C"
    },
    {
        "id": 95,
        "question": "কম্পিউটার সিপিইউ (CPU)-এর কোন অংশ গাণিতিক সিদ্ধান্ত গ্রহণের কাজ করে?",
        "options": [
            "এ. এল. ইউ (ALU)",
            "কন্ট্রোল ইউনিট (control unit)",
            "রেজিস্টার সেট (Register set)",
            "কোনটিই নয়"
        ],
        "answer": "A"
    },
    {
        "id": 96,
        "question": "\"একটি ২(দুই) ইনপুট লজিক সেটের আউটপুট ০ হবে, যদি এর ইনপুটগুলো সমান হয়\" --এর উক্তিটি কোন সেটের জন্য সত্য?",
        "options": [
            "AND",
            "NOR",
            "Ex-OR",
            "OR"
        ],
        "answer": "C"
    },
    {
        "id": 97,
        "question": "কোনটি অপারেটিং সিস্টেম নয়?",
        "options": [
            "C",
            "DOS",
            "CP/M",
            "XENIX"
        ],
        "answer": "A"
    },
    {
        "id": 98,
        "question": "ক্লাউড সার্ভার নিচের কোনটিতে সবচেয়ে ভালো বর্ণনা করা সম্ভব?",
        "options": [
            "নেটওয়ার্কের মাধ্যমে যুক্ত একাধিক কম্পিউটার সার্ভার",
            "একটি বিশাল ক্ষমতা সম্পন্ন কম্পিউটার সার্ভার",
            "ব্যবহারকারীর চাহিদা অনুযায়ী কম্পিউটিং সেবা দেয়া",
            "উপরের কোনোটিই নয়"
        ],
        "answer": "C"
    },
    {
        "id": 99,
        "question": "IP - V6 এড্রেস কত বিটের?",
        "options": [
            "১২৮",
            "৩২",
            "১২",
            "৬"
        ],
        "answer": "A"
    },
    {
        "id": 100,
        "question": "নিচের কোনটি ইনপুট ডিভাইস?",
        "options": [
            "OMR",
            "COM",
            "Plotter",
            "Monitor"
        ],
        "answer": "A"
    },
    {
        "id": 101,
        "question": "ইউনিকোডের মাধ্যমে সম্ভাব্য কতগুলো চিহ্নকে নির্দিষ্ট করা যায়?",
        "options": [
            "২৫৬ টি",
            "৪০৯৬ টি",
            "৬৫৫৩৬ টি",
            "৪২৯৪৯৬৭২৯৬ টি"
        ],
        "answer": "C"
    },
    {
        "id": 102,
        "question": "এনড্রয়েড অপারেটিং সিস্টেমের ক্ষেত্রে নিচের কোনটি সঠিক?",
        "options": [
            "এটির নির্মাতা গুগল",
            "এটি লিনাক্স কার্নেল নির্ভর",
            "এটি প্রধানত টাচস্ক্রিন মোবাইল ডিভাইসের জন্য তৈরি",
            "উপরের সবগুলো সঠিক"
        ],
        "answer": "D"
    },
    {
        "id": 103,
        "question": "আইওএস (IOS) মোবাইল অপারেটিং সিস্টেমটি কোন প্রতিষ্ঠান বাজারজাত করে?",
        "options": [
            "অ্যাপেল",
            "গুগল",
            "মাইক্রোসফট",
            "আইবিএম"
        ],
        "answer": "A"
    },
    {
        "id": 104,
        "question": "EDSAC কম্পিউটার-এ ডাটা সংরক্ষণের জন্য কি ধরনের মেমোরি ব্যবহার হতো?",
        "options": [
            "RAM",
            "ROM",
            "Mercury Delay Lines",
            "Registors"
        ],
        "answer": "C"
    },
    {
        "id": 105,
        "question": "ই-কমার্স সাইট amazon.com কত সালে প্রতিষ্ঠিত হয়?",
        "options": [
            "১৯৯০ সালে",
            "১৯৮৮ সালে",
            "১৯৯৪ সালে",
            "১৯৯৮ সালে"
        ],
        "answer": "C"
    },
    {
        "id": 106,
        "question": "ই-মেইল আদান প্রদানে ব্যবহৃত SMTP এর পূর্ণরূপ কি?",
        "options": [
            "Simple Message Transmission Protocol",
            "Strategic Mail Transfer Protocol",
            "Strategic Mail Transmission Protocol",
            "Simple Mail Transfer Protocol"
        ],
        "answer": "D"
    },
    {
        "id": 107,
        "question": "TCP দিয়ে কোনটি বোঝানো হয়?",
        "options": [
            "প্রোগ্রাম",
            "প্রোটোকল",
            "প্রোগ্রামিং",
            "ফ্লোচার্ট"
        ],
        "answer": "B"
    },
    {
        "id": 108,
        "question": "Push এবং Pop নিচের কার সাথে সম্পর্কিত?",
        "options": [
            "Queue",
            "Stack",
            "Union",
            "Array"
        ],
        "answer": "B"
    },
    {
        "id": 109,
        "question": "ওয়াই-ফাই (Wi-Fi) নেটওয়ার্কে সংযোগের জন্য সংশ্লিষ্ট ডিভাইসটির সংযোগ মাধ্যম কোনটি?",
        "options": [
            "তামার তার",
            "অপটিক্যাল ফাইবার",
            "তারহীন সংযোগ",
            "উপরের সবকটি"
        ],
        "answer": "C"
    },
    {
        "id": 110,
        "question": "নিচের কোন মেমোরীটি Non-volatile?",
        "options": [
            "SRAM",
            "DRAM",
            "ROM",
            "উপরের সবগুলোই"
        ],
        "answer": "C"
    },
    {
        "id": 111,
        "question": "নিচের কোনটি 3G Language নয়?",
        "options": [
            "C",
            "Java",
            "Assembly Language",
            "C++"
        ],
        "answer": "C"
    },
    {
        "id": 112,
        "question": "নিচের কোন উক্তিটি সঠিক?",
        "options": [
            "১ কিলোবাইট = ১০২৪ বাইট",
            "১ মেগাবাইট = ১০২৪ বাইট",
            "১ কিলোবাইট = ১০০০ বাইট",
            "১ মেগাবাইট = ১০০০ বাইট"
        ],
        "answer": "A"
    },
    {
        "id": 113,
        "question": "Wi-fi কোন স্ট্যান্ডার্ড-এর উপর ভিত্তি করে কাজ করে?",
        "options": [
            "IEEE 802.11",
            "IEEE 804.11",
            "IEEE 803.11",
            "IEEE 806.11"
        ],
        "answer": "A"
    },
    {
        "id": 114,
        "question": "নিচের কোনটিতে সাধারণত ইনফ্রারেড ডিভাইস ব্যবহার করা হয়?",
        "options": [
            "WAN",
            "Satellite",
            "MAN",
            "TV রিমোট কন্ট্রোলে"
        ],
        "answer": "D"
    },
    {
        "id": 115,
        "question": "১০ এর ২ এর পরিপূরক (2's complement) কত?",
        "options": [
            "(1100)",
            "(11000)",
            "(01100)",
            "কোনোটিই নয়"
        ],
        "answer": "D"
    },
    {
        "id": 116,
        "question": "WI MAX- এর পূর্ণরূপ কি?",
        "options": [
            "Worldwide Interoperability for Microwave Access",
            "Worldwide Internet for Microwave Access",
            "Worldwide Interconection for Microwave Access",
            "কোনোটিই নয়"
        ],
        "answer": "A"
    },
    {
        "id": 117,
        "question": "Boolean Algebra -এর নিচের কোনটি সঠিক?",
        "options": [
            "A + Ā = 1",
            "A . Ā = 1",
            "A + A = 2A",
            "উপরের কোনোটিই নয়"
        ],
        "answer": "A"
    },
    {
        "id": 118,
        "question": "8086 কত বিটের মাইক্রো প্রসেসর?",
        "options": [
            "8",
            "16",
            "32",
            "উপরের কোনোটিই নয়"
        ],
        "answer": "B"
    },
    {
        "id": 119,
        "question": "Mobile Phone -এর কোনটি input device নয়?",
        "options": [
            "Keypad",
            "Touch Screen",
            "Camera",
            "Power Supply"
        ],
        "answer": "D"
    },
    {
        "id": 120,
        "question": "নিচের কোনটি ডাটাবেজ language?",
        "options": [
            "Oracle",
            "C",
            "MS-Word",
            "কোনোটিই নয়"
        ],
        "answer": "A"
    },
    {
        "id": 121,
        "question": "Linkedin --এর ক্ষেত্রে কোনটি সঠিক?",
        "options": [
            "এটি একটি বিজনেস অরিয়েন্টেড সোশ্যাল নেটওয়ার্কিং সার্ভিস",
            "এটি ২০০২ সালে প্রতিষ্ঠিত",
            "২০০৬ সালে এটির সদস্যসংখ্যা ২০ মিলিয়নের অধিক হয়",
            "উপরের সবগুলোই"
        ],
        "answer": "A"
    },
    {
        "id": 122,
        "question": "কমিউনিকেশন সিস্টেমে গেটওয়ে কি কাজে ব্যবহার হয়?",
        "options": [
            "বিভিন্ন নেটওয়ার্ক ডিভাইস সংযুক্ত করার কাজে",
            "দুই বা তার অধিক ভিন্ন ধরনের নেটওয়ার্ককে সংযুক্ত করার কাজে",
            "এটি নেটওয়ার্ক হাব কিংবা সুইচ এর মতই কাজ করে",
            "কোনোটিই নয়"
        ],
        "answer": "B"
    },
    {
        "id": 123,
        "question": "নিচের কোনটি কম্পিউটারের প্রাইমারি মেমোরি?",
        "options": [
            "RAM",
            "Hard Disk",
            "Pen drive",
            "কোনোটিই নয়"
        ],
        "answer": "A"
    },
    {
        "id": 124,
        "question": "Plotter কোন ধরনের ডিভাইস?",
        "options": [
            "ইনপুট",
            "আউটপুট",
            "মেমোরি",
            "উপরের কোনোটিই নয়"
        ],
        "answer": "B"
    },
    {
        "id": 125,
        "question": "কম্পিউটার সিস্টেম এ Scanner একটি কোন ধরনের যন্ত্র?",
        "options": [
            "Input",
            "Out put",
            "উভয়েই",
            "কোনোটিই নয়"
        ],
        "answer": "A"
    },
    {
        "id": 126,
        "question": "কম্পিউটারের মূল মেমোরি তৈরি হয় কি দিয়ে?",
        "options": [
            "এলুমিনিয়াম",
            "প্লাস্টিক",
            "সিলিকন",
            "কোনোটিই নয়"
        ],
        "answer": "C"
    },
    {
        "id": 127,
        "question": "Back up প্রোগ্রাম বলতে কী বোঝানো হয়?",
        "options": [
            "নির্ধারিত ফাইল কপি করা",
            "আগের প্রোগ্রামে ফিরে যাওয়া",
            "সবশেষ পরিবর্তন Undo করা",
            "কোনোটিই নয়"
        ],
        "answer": "A"
    },
    {
        "id": 128,
        "question": "একটি প্রতিষ্ঠানে ডিভাইস ভাগাভাগি করে নেয়ার সুবিধা হলো",
        "options": [
            "অর্থ সাশ্রয়",
            "সময় সাশ্রয়",
            "স্থানের সাশ্রয়",
            "উপরের সবকটি"
        ],
        "answer": "D"
    },
    {
        "id": 129,
        "question": "নিচের কোন সাইটটি কেনা-বেচার জন্য নয়?",
        "options": [
            "ekanei.com",
            "Olx.com",
            "google.com",
            "amazon.com"
        ],
        "answer": "C"
    },
    {
        "id": 130,
        "question": "নিচের কোনটি ছাড়া Internet- এ প্রবেশ করা সহজ নয়?",
        "options": [
            "Task bar",
            "Notification area",
            "Menu bar",
            "Web browser"
        ],
        "answer": "D"
    },
    {
        "id": 131,
        "question": "কম্পিউটার মেমোরি থেকে সংরক্ষিত ডাটা উত্তোলনের পদ্ধতিকে কি বলে?",
        "options": [
            "Read-out",
            "Read from",
            "Read",
            "উপরের সবগুলোই"
        ],
        "answer": "C"
    },
    {
        "id": 132,
        "question": "MICR-এর পূর্ণরূপ কি?",
        "options": [
            "Magnetic Ink Character Reader",
            "Magnetic Ink Code Reader",
            "Magnetic Ink Case Reader",
            "কোনোটিই নয়"
        ],
        "answer": "A"
    },
    {
        "id": 133,
        "question": "নিচের কোনটি ডাটাবেজ ল্যাংগুয়েজ?",
        "options": [
            "Data Definition Language",
            "Data Manipulation Language",
            "Query Language",
            "উপরের সবগুলোই"
        ],
        "answer": "D"
    },
    {
        "id": 134,
        "question": "সোশ্যাল নেটওয়ার্কিং টুইটার কত সালে তৈরি হয়?",
        "options": [
            "২০০৪",
            "২০০৬",
            "২০০৩",
            "২০০৮"
        ],
        "answer": "B"
    },
    {
        "id": 135,
        "question": "নিচের কোন স্মার্টফোন অপারেটিং সিস্টেমটি ওপেন সোর্স প্ল্যাটফর্ম?",
        "options": [
            "IOS",
            "Windows phone",
            "Android",
            "Symbian"
        ],
        "answer": "C"
    },
    {
        "id": 136,
        "question": "মোবাইল কমিউনিকেশনে 4G-এর ক্ষেত্রে 3G এর তুলনায় অতিরিক্ত বৈশিষ্ট্য কি?",
        "options": [
            "ভয়েস টেলিফোনি",
            "ভিডিও কল",
            "মোবাইল টিভি",
            "ব্রডব্যান্ড ইন্টারনেট সেবা"
        ],
        "answer": "D"
    },
    {
        "id": 137,
        "question": "Oracle Corporation--এর প্রতিষ্ঠাতা কে?",
        "options": [
            "Bill Gatea",
            "Tim Cook",
            "Andrew S Grove",
            "Lawrence J. Ellison"
        ],
        "answer": "D"
    },
    {
        "id": 138,
        "question": "প্রোগ্রাম থেকে কপি করা ডাটা কোথায় থাকে?",
        "options": [
            "RAM",
            "Clipboard",
            "Terminal",
            "Hard Disk"
        ],
        "answer": "B"
    },
    {
        "id": 139,
        "question": "পারসনাল কম্পিউটার যুক্ত করে নিচের কোনটি তৈরি করা যায়?",
        "options": [
            "Super Computer",
            "Network",
            "Server",
            "Enterprise"
        ],
        "answer": "B"
    },
    {
        "id": 140,
        "question": "The term PC means",
        "options": [
            "Private Computer",
            "Prime Computer",
            "Personal Computer",
            "Professional Computer"
        ],
        "answer": "C"
    },
    {
        "id": 141,
        "question": "ইন্টারনেট চালুর বছর",
        "options": [
            "১৯৫৯",
            "১৯৬৫",
            "১৯৬৯",
            "১৯৮১"
        ],
        "answer": "C"
    },
    {
        "id": 142,
        "question": "মডেম-এর মধ্যে যা থাকে তা হলো",
        "options": [
            "একটি মডুলেটর",
            "একটি মডুলেটর ও একটি ডিমডুলেটর",
            "একটি কোডেক",
            "একটি এনকোডার"
        ],
        "answer": "B"
    },
    {
        "id": 143,
        "question": "কম্পিউটার ভাইরাস কি?",
        "options": [
            "একটি ক্ষতিকারক জীবাণু",
            "একটি ক্ষতিকারক সার্কিট",
            "একটি ক্ষতিকারক চৌম্বক ফ্লাক্স",
            "একটি ক্ষতিকারক প্রোগ্রাম"
        ],
        "answer": "D"
    },
    {
        "id": 144,
        "question": "কোনটি তারবিহীন দ্রুতগতির ইন্টারনেট সংযোগের জন্য উপযোগী?",
        "options": [
            "ওয়াইম্যাক্স",
            "সি-মস",
            "ব্লু-টুথ",
            "ব্রডব্যান্ড"
        ],
        "answer": "A"
    },
    {
        "id": 145,
        "question": "কম্পিউটার-টু- কম্পিউটারের তথ্য আদান-প্রদানের প্রযুক্তিকে বলা হয়",
        "options": [
            "ই-মেইল",
            "ইন্টারকম",
            "ইন্টারনেট",
            "টেলিকমিউনিকেশন"
        ],
        "answer": "C"
    },
    {
        "id": 146,
        "question": "কম্পিউটার থেকে কম্পিউটারে তথ্য আদান-প্রদানের প্রযুক্তিকে বলা হয়",
        "options": [
            "ই-মেইল",
            "ইন্টারকম",
            "ইন্টারনেট",
            "টেলিগ্রাম"
        ],
        "answer": "C"
    },
    {
        "id": 147,
        "question": "কম্পিউটারের স্থায়ী স্মৃতিশক্তিকে কি বলে?",
        "options": [
            "RAM",
            "ROM",
            "হার্ডওয়্যার",
            "সফটওয়্যার"
        ],
        "answer": "B"
    },
    {
        "id": 148,
        "question": "পৃথিবীতে কখন ল্যাপটপ কম্পিউটার প্রবর্তিত হয় এবং কোন কোম্পানি এটা তৈরি করে?",
        "options": [
            "কমপ্যাক, ১৯৮৫",
            "এপসন, ১৯৮১",
            "আইবিএম, ১৯৮৩",
            "অ্যাপল, ১৯৭৭"
        ],
        "answer": "B"
    },
    {
        "id": 149,
        "question": "'ল্যাপটপ' কি?",
        "options": [
            "ছোট কুকুর",
            "পর্বতারোহণ সামগ্রী",
            "বাদ্যযন্ত্র",
            "ছোট কম্পিউটার"
        ],
        "answer": "D"
    },
    {
        "id": 150,
        "question": "কম্পিউটারে কোনটি নেই?",
        "options": [
            "স্মৃতি",
            "বুদ্ধি বিবেচনা",
            "দীর্ঘ সময় কাজ করার ক্ষমতা",
            "নির্ভুল কাজ করার ক্ষমতা"
        ],
        "answer": "B"
    },
    {
        "id": 151,
        "question": "কম্পিউটার ভাইরাস হলো-----",
        "options": [
            "এক ধরনের বিশেষ কম্পিউটার প্রোগ্রাম",
            "কম্পিউটারের যন্ত্রাংশে কোথাও শর্টসার্কিট",
            "কম্পিউটারের যন্ত্রাংশের মধ্যে জমে থাকা ধূলা",
            "কম্পিউটারের কোনো যন্ত্রাংশ সার্কিটে ঢিলা কানেকশন"
        ],
        "answer": "A"
    },
    {
        "id": 152,
        "question": "কম্পিউটার কে আবিষ্কার করেন?",
        "options": [
            "ইউলিয়াম অটরেড",
            "ব্লেইসি প্যাসকেল",
            "হাওয়ার্ড এইকিন",
            "আবাকাস"
        ],
        "answer": "C"
    },
    {
        "id": 153,
        "question": "'ল্যাপটপ' হলো এক ধরনের",
        "options": [
            "পর্বতারোহণ সামগ্রী",
            "ছোট কুকুর",
            "বাদ্যযন্ত্র",
            "ছোট কম্পিউটার"
        ],
        "answer": "D"
    },
    {
        "id": 154,
        "question": "বাংলাদেশের ভূ-উপগ্রহ কেন্দ্রের সংখ্যা কয়টি?",
        "options": [
            "এক",
            "দুই",
            "তিন",
            "চার"
        ],
        "answer": "D"
    },
    {
        "id": 155,
        "question": "ডিজিটাল ঘড়ি বা ক্যালকুলেটরে কালচে অনুজ্জ্বল যে লেখা ফুটে ওঠে তা কিসের ভিত্তিতে তৈরি?",
        "options": [
            "এলইডি",
            "সিলিকন চিপ",
            "এলসিডি",
            "আইসি"
        ],
        "answer": "C"
    },
    {
        "id": 156,
        "question": "কম্পিউটারের সফটওয়্যার বলতে বুঝানো হয়",
        "options": [
            "এর প্রোগ্রাম বা কর্ম পরিকল্পনার কৌশল",
            "তথ্য দেয়া ও তথ্য নেয়ার অংশ বিশেষ",
            "যেসব অংশ মুদ্রিত অবস্থায় থাকে",
            "কম্পিউটার তৈরির নকশা"
        ],
        "answer": "A"
    },
    {
        "id": 157,
        "question": "A class is a:",
        "options": [
            "Physical entity",
            "Real-world object",
            "Blueprint or template for creating objects",
            "Method within an object"
        ],
        "answer": "C"
    }
]

out_dir = r"JSON Data/BPSC ICT Wizard"
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, "BCS Computer পার্ট.json")

with open(out_file, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {out_file} with {len(questions)} MCQs.")
