# Page 917
PAGE_NUM = 917

QUESTIONS = [
    {
        "id": 41,
        "page": 917,
        "question": "Which neural network architecture is the foundation of most modern LLMs? [BB-2026]",
        "options": [
            "Bayesian Netowrk",
            "Convolutional Neural Network (CNN)",
            "Transformer",
            "Autoencoder"
        ],
        "answer": "গ",
        "explanation": "আধুনিক LLMs (Large Language Models) মূলত Transformer আর্কিটেকচারের উপর ভিত্তি করে তৈরি। কারণ, এটি Self-Attention মেকানিজম ব্যবহার করে টেক্সটের মধ্যে দূরের সম্পর্কও ধরতে পারে। এই কারণে Transformers বড় টেক্সট ডাটা দ্রুত এবং কার্যকরভাবে প্রক্রিয়াকরণ করতে সক্ষম, যা LLMs-এর জন্য অত্যন্ত গুরুত্বপূর্ণ। জিপিটি (GPT), বার্ট (BERT) বা ল্যামা (Lama)-র মতো আজকের জনপ্রিয় সব শক্তিশালী এআই মডেল এই ট্রান্সফরমার আর্কিটেকচার ব্যবহার করেই তৈরি করা হয়েছে।"
    },
    {
        "id": 42,
        "page": 917,
        "question": "If a process fails, most operating systems write the error information to a - [BB-2026]",
        "options": [
            "new file",
            "another running process",
            "log file",
            "database"
        ],
        "answer": "গ",
        "explanation": "যখন কোনো প্রসেস ব্যর্থ হয়, তখন OS সেই ত্রুটির তথ্য log file-এ সংরক্ষণ করে, যেমন ত্রুটির টাইমস্ট্যাম্প, ধরন ও প্রসেস আইডি। এটি পরে সিস্টেম অ্যাডমিন বা ডেভেলপারদের জন্য সমস্যা নির্ণয় ও সমাধান সহজ করার জন্য ব্যবহৃত হয়।"
    },
    {
        "id": 43,
        "page": 917,
        "question": "Which data structure is generally used for implementing recursion? [BB-2026]",
        "options": [
            "Stack",
            "Queue",
            "List",
            "Array"
        ],
        "answer": "ক",
        "explanation": "যখন কোনো ফাংশন recursively নিজেকে কল করে, তখন প্রতিটি কলের Local variables, return address এবং প্যারামিটারসমূহ stack-এ সংরক্ষিত হয়। এটি নিশ্চিত করে যে, প্রতিটি recursive call-এর প্রেক্ষাপট ঠিকঠাক মনে রাখা হয় এবং ফাংশন সম্পন্ন হলে control ঠিকভাবে previous call-এ ফিরে আসে।"
    },
    {
        "id": 44,
        "page": 917,
        "question": "Which of the following tags is used to define an image in HTML? [BB-2026]",
        "options": [
            "<img>",
            "<image>",
            "<picture>",
            "<src>"
        ],
        "answer": "ক",
        "explanation": "HTML-এ কোনো ছবি ওয়েবপেজে দেখানোর জন্য <img> ট্যাগ ব্যবহার করা হয়। এই ট্যাগে সাধারণত দুইটি প্রধান অ্যাট্রিবিউট থাকে : src-ছবির ফাইলের পথ বা URL এবং alt ছবি লোড না হলে প্রদর্শিত বিকল্প টেক্সট।\nউদাহরণ : <img src = \"image.jpg\" alt = \"Example Image\">"
    },
    {
        "id": 45,
        "page": 917,
        "question": "What does CSS stand for? [BB-2026]",
        "options": [
            "Computer Style Sheets",
            "Creative Style Sheets",
            "Cascading Style Sheets",
            "Colourful Style Sheets"
        ],
        "answer": "গ",
        "explanation": "Cascading Style Sheets (CSS) হলো একটি স্টাইলিং ভাষা, যা HTML উপাদানগুলোর দৃশ্যমান রূপ, যেমন- রঙ, ফন্ট, লেআউট এবং স্পেসিং নিয়ন্ত্রণ করতে ব্যবহৃত হয়। CSS ব্যবহার করে ওয়েবপেজকে সুন্দর, সুশৃঙ্খল এবং ব্যবহারকারী-বান্ধব করা যায়, পাশাপাশি একই স্টাইল একাধিক পেজে প্রয়োগ করা সম্ভব।"
    },
    {
        "id": 46,
        "page": 917,
        "question": "Which of the following is a type of memory that retains its contents even when the power is turned off? [BB-2026]",
        "options": [
            "RAM",
            "ROM",
            "Cache memory",
            "Register"
        ],
        "answer": "খ",
        "explanation": "ROM (Read-Only Memory) হলো একটি non-volatile memory, যার মানে হলো এতে সংরক্ষিত ডাটা বিদ্যুৎ বন্ধ থাকলেও মুছে যায় না। এটি সাধারণত সিস্টেমের গুরুত্বপূর্ণ তথ্য বা প্রোগ্রাম সংরক্ষণ করতে ব্যবহৃত হয়, যেমন কম্পিউটারের বুটিং ইন্সট্রাকশন।"
    },
    {
        "id": 47,
        "page": 917,
        "question": "After groups have been established, SQL applies predicates in the - clause, allowing aggregate functions to be used. [BB-2026]",
        "options": [
            "having",
            "where",
            "with",
            "select"
        ],
        "answer": "ক",
        "explanation": "HAVING হলো SQL-এ ব্যবহৃত একটি ক্লজ, যা GROUP By-এর পর aggregate function-এর উপর শর্ত আরোপ করতে ব্যবহার করা হয়। WHERE ক্লজ individual rows-এর শর্তের জন্য ব্যবহার হয়। HAVING ক্লজ grouped rows বা aggregated data-এর জন্য শর্ত দেয়।"
    },
    {
        "id": 48,
        "page": 917,
        "question": "An administrator is troubleshooting network connectivity and would like to view the path that packets are taking from workstation A to server 1. Which of the following command line tools is MOST appropriate to use? [BB-2026]",
        "options": [
            "traceroute",
            "dig",
            "ping",
            "route"
        ],
        "answer": "ক",
        "explanation": "Traceroute হলো একটি নেটওয়ার্ক টুল, যা ব্যবহার করা হয় এক ডিভাইস থেকে অন্য ডিভাইস পর্যন্ত ডাটা প্যাকেট কোন কোন intermediate router বা hop দিয়ে যাচ্ছে এবং কত সময় নিচ্ছে তা দেখার জন্য। এটি মূলত নেটওয়ার্ক সমস্যা নির্ণয় এবং প্যাকেটের পথ বিশ্লেষণ করতে ব্যবহৃত হয়, ফলে নেটওয়ার্কের ধীরগতি বা লেটেন্সির উৎস চিহ্নিত করা সহজ হয়।"
    },
    {
        "id": 49,
        "page": 917,
        "question": "Wrapping data and its related functionality into a single entity is known as- [BB-2026]",
        "options": [
            "Abstraction",
            "Encapsulation",
            "Polymorphism",
            "Modularity"
        ],
        "answer": "খ",
        "explanation": "Encapsulation হলো Object-Oriented Programming (OOP)-এর একটি গুরুত্বপূর্ণ ধারণা, যেখানে ডাটা (Variables) এবং সেই ডাটার উপর কাজ করা মেথডগুলোকে একসাথে একটি ক্লাসের ভিতরে আবদ্ধ রাখা হয় এবং বাইরের দিক থেকে ডাটায় সরাসরি প্রবেশ সীমিত করা হয়, ফলে ডাটা নিরাপদ থাকে ও প্রোগ্রামের কাঠামো আরও সুশৃঙ্খল হয়।"
    },
    {
        "id": 50,
        "page": 917,
        "question": "In the Model-View-Controller (MVC) architecture used in web applications, which components is responsible for handling HTTP requests such as GET and POST? [BB-2026]",
        "options": [
            "Model",
            "View",
            "Controller",
            "Both Model and View"
        ],
        "answer": "গ",
        "explanation": "Controller ইউজারের request গ্রহণ ও প্রসেস করে।"
    }
]
