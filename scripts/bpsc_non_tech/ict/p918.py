# Page 918
PAGE_NUM = 918

QUESTIONS = [
    {
        "id": 51,
        "page": 918,
        "question": "Source code translation and Program modularization are the activities of - [BB-2026]",
        "options": [
            "Reverse engineering",
            "Forward engineering",
            "Reengineering",
            "Testing"
        ],
        "answer": "গ",
        "explanation": "Reengineering হলো বিদ্যমান সফটওয়্যারকে বিশ্লেষণ করে তার গঠন, কর্মক্ষমতা বা রক্ষণাবেক্ষণযোগ্যতা উন্নত করার প্রক্রিয়া; যেখানে পুরোনো সিস্টেমকে নতুন চাহিদার সাথে মানানসই করা হয়।\nReverse Engineering হলো একটি বিদ্যমান সফটওয়্যার বা সিস্টেমকে বিশ্লেষণ করে তার নকশা, কাঠামো বা কার্যপ্রণালি বুঝার প্রক্রিয়া; যেখানে সোর্স কোড থেকে ডিজাইন বা ডকুমেন্টেশন বের করা হয়।\nForward Engineering হলো সিস্টেমের প্রয়োজনীয়তা ও ডিজাইন থেকে শুরু করে ধাপে ধাপে কোড লিখে সম্পূর্ণ নতুন সফটওয়্যার তৈরি করার প্রক্রিয়া।\nTesting হলো সফটওয়্যারে ত্রুটি আছে কিনা যাচাই করার প্রক্রিয়া, যার মাধ্যমে নিশ্চিত করা হয় যে সফটওয়্যারটি সঠিকভাবে কাজ করছে এবং ব্যবহারকারীর চাহিদা পূরণ করছে।"
    },
    {
        "id": 52,
        "page": 918,
        "question": "Which one of these is NOT shared by the same process's threads? [BB-2026]",
        "options": [
            "Address Space",
            "Stack",
            "Message Queue",
            "File Descriptor Table"
        ],
        "answer": "খ",
        "explanation": "একই প্রসেসের থ্রেডগুলো code, data এবং heap memory শেয়ার করে, কিন্তু প্রতিটি থ্রেডের নিজস্ব stack থাকে। কারণ stack-এ থ্রেডের local variables, function call information এবং return address সংরক্ষিত থাকে, যা অন্য থ্রেডের সাথে শেয়ার করা যায় না।"
    },
    {
        "id": 53,
        "page": 918,
        "question": "If a process is executing in its critical section, then no other processes can be executing in their critical section. What is this condition called? [BB-2026]",
        "options": [
            "mutual exclusion",
            "race condition",
            "critical condition",
            "synchronous condition"
        ],
        "answer": "ক",
        "explanation": "Mutual Exclusion নিশ্চিত করে যে, এক সময়ে মাত্র একটি process বা thread-ই critical section-এ প্রবেশ করতে পারে, ফলে shared resource ব্যবহার করার সময় ডাটা অসামঞ্জস্য (Race condition) এড়ানো যায়।"
    },
    {
        "id": 54,
        "page": 918,
        "question": "Which statement best describes a public IP address? [BB-2026]",
        "options": [
            "Used only within a local network",
            "Not routable on the internet",
            "Assigned only by local routers",
            "Unique and globally routable on the Internet"
        ],
        "answer": "ঘ",
        "explanation": "Public IP হলো একটি ইউনিক IP address, যা ইন্টারনেটে সরাসরি শনাক্তযোগ্য এবং ব্যবহারযোগ্য। এটি ISP (Internet Service Provider) দ্বারা প্রদান করা হয় এবং ইন্টারনেটে থাকা যেকোনো সার্ভার বা ডিভাইসের সাথে সরাসরি যোগাযোগ করতে পারে।"
    },
    {
        "id": 55,
        "page": 918,
        "question": "Which scheduling algorithm gives minimum average waiting time? [BB-2026]",
        "options": [
            "FCFS",
            "Round Robin",
            "SJF",
            "Priority"
        ],
        "answer": "গ",
        "explanation": "SJF scheduling algorithm গড় অপেক্ষার সময় (average waiting time) সর্বনিম্ন দেয়, কারণ এতে যে প্রসেসের CPU burst time সবচেয়ে কম, সেটিকে আগে execute করা হয়, ফলে ছোট কাজগুলো দ্রুত শেষ হয়ে যায় এবং সামগ্রিক waiting time কমে।"
    },
    {
        "id": 56,
        "page": 918,
        "question": "Context switching occurs in- [BB-2026]",
        "options": [
            "Compiler",
            "Memory",
            "CPU",
            "I/O device"
        ],
        "answer": "গ",
        "explanation": "Context switching ঘটে CPU-তে, যখন CPU একটি প্রসেসের কাজ থামিয়ে অন্য প্রসেস চালু করে। এ সময় পূর্বের প্রসেসের অবস্থা (registers, program counter ইত্যাদি) সংরক্ষণ করে এবং নতুন প্রসেসের অবস্থা লোড করে।"
    },
    {
        "id": 57,
        "page": 918,
        "question": "Port number for HTTP is- [BB-2026]",
        "options": [
            "21",
            "25",
            "80",
            "443"
        ],
        "answer": "গ",
        "explanation": "HTTP (Hyper Text Transfer Protocol) সাধারণত port number 80 ব্যবহার করে ওয়েব ব্রাউজার ও ওয়েব সার্ভারের মধ্যে ডাটা আদান-প্রদানের জন্য। FTP (File Transfer Protocol)-এর পোর্ট নাম্বার 21। SMTP (Simple Mail Transfer Protocol)-এর পোর্ট নাম্বার 25। HTTPS (Hyper Text Transfer Protocol Secure) এর পোর্ট নাম্বার 443।"
    },
    {
        "id": 58,
        "page": 918,
        "question": "Which language is used to manage databases? [BB-2026]",
        "options": [
            "HTML",
            "SQL",
            "XML",
            "Java"
        ],
        "answer": "খ",
        "explanation": "SQL (Structured Query Language) ডাটাবেজ তৈরি, পরিচালনা ও ডাটা অনুসন্ধানের জন্য ব্যবহৃত হয়, তাই ডাটাবেজ ম্যানেজমেন্টের জন্য এটি আদর্শ ভাষা।"
    },
    {
        "id": 59,
        "page": 918,
        "question": "Which command is used to remove a table? [BB-2026]",
        "options": [
            "DELETE",
            "DROP",
            "REMOVE",
            "TRUNCATE"
        ],
        "answer": "খ",
        "explanation": "DROP কমান্ড ব্যবহার করে ডাটাবেজ থেকে একটি টেবিল সম্পূর্ণভাবে মুছে ফেলা হয়, অর্থাৎ টেবিলের স্ট্রাকচার ও ডাটা দুটোই স্থায়ীভাবে অপসারণ করা হয়। যেমন- DROP TABLE TABLE_NAME;"
    },
    {
        "id": 60,
        "page": 918,
        "question": "Which is not a programming language? [BB-2026]",
        "options": [
            "Python",
            "Java",
            "HTML",
            "C++"
        ],
        "answer": "গ",
        "explanation": "HTML (Hyper Text Markup Language) একটি markup language, যা ওয়েবপেজের কাঠামো তৈরি করতে ব্যবহৃত হয়। এটি Programming language নয়, কারণ এতে লজিক বা প্রোগ্রামিং কন্ট্রোল স্ট্রাকচার নেই। অন্যদিকে Python, Java এবং C++ হলো পূর্ণাঙ্গ Programming Languages।"
    },
    {
        "id": 61,
        "page": 918,
        "question": "চীনের কোন এআই মডেলটি বিশ্বে সাড়া ফেলেছে? [MOFL-2025]",
        "options": [
            "চ্যাটজিপিটি",
            "জেমিনি",
            "ক্লুড",
            "ডিপসিক"
        ],
        "answer": "ঘ",
        "explanation": "চীনের ডিপসিক (Deepseek) এআই মডেলটি বিশ্বে সাড়া ফেলেছে। এটি ২০২৪ সাল থেকে বিশ্বজুড়ে ব্যাপক সাড়া ফেলেছে। এটি চ্যাটজিপিটি, জেমিনি এর মতো একটি জেনারেটিভ AI মডেল, যা মানুষের মতো করে লিখতে, অনুবাদ করতে এবং বিশ্লেষণ করতে পারে। চীনের স্থানীয় প্রযুক্তি অবকাঠামো ও ভাষা অনুযায়ী এটি বিভিন্ন ভাষাতে দক্ষ। উন্নত চিপ ও কম রিসোর্স ব্যবহার করেও এটি চ্যাটজিপিটি, জেমিনি-এর সঙ্গে প্রতিযোগিতায় সক্ষম হয়ে উঠেছে।"
    },
    {
        "id": 62,
        "page": 918,
        "question": "Binary consists of : [GDA-2025]",
        "options": [
            "0 + 0",
            "1 + 1",
            "0 + 1",
            "1 + 2"
        ],
        "answer": "গ",
        "explanation": "এখানে সঠিক উত্তর হবে 0 + 1। আর Binary বলতে হয় '0' অথবা '1'-কে বুঝায়।"
    }
]
