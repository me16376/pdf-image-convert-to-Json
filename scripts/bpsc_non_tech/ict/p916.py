# Page 916
PAGE_NUM = 916

QUESTIONS = [
    {
        "id": 28,
        "page": 916,
        "question": "Which port must be open to allow sending emails from a client to a server? [BB-2026]",
        "options": [
            "25 or 587",
            "110",
            "143",
            "443"
        ],
        "answer": "ক",
        "explanation": "SMTP প্রটোকল ইমেইল পাঠানোর জন্য ব্যবহৃত হয়, যার পোর্ট 25 বা 587।"
    },
    {
        "id": 29,
        "page": 916,
        "question": "Which of the following is the most secure method for remote administration of a Linux server? [BB-2026]",
        "options": [
            "Telnet using root account",
            "SSH using password authentication",
            "SSH using key-based authentication",
            "VNC without encryption"
        ],
        "answer": "গ",
        "explanation": "Key-based SSH হলো একটি নিরাপদ লগইন পদ্ধতি, যেখানে সার্ভারে পাসওয়ার্ডের পরিবর্তে প্রাইভেট ও পাবলিক কী ব্যবহার করা হয়। ক্লায়েন্টের প্রাইভেট কী দিয়ে সার্ভারকে প্রমাণ পাঠানো হয় এবং সার্ভার পাবলিক কী দিয়ে যাচাই করে। এটি পাসওয়ার্ডের তুলনায় বেশি নিরাপদ এবং স্বয়ংক্রিয় লগইন ও স্ক্রিপ্টিংয়ের জন্য সুবিধাজনক এবং Brute-force আক্রমণ প্রতিরোধ করে।"
    },
    {
        "id": 30,
        "page": 916,
        "question": "What describes a \"Dictionary Attack\"? [BB-2026]",
        "options": [
            "Guessing passwords by trying every word in a pre-defined list",
            "Trying every possible combination of characters (Brute Force)",
            "Stealing the physical password notebook",
            "Asking the user for their password"
        ],
        "answer": "ক",
        "explanation": "Dictionary Attack হলো একটি সাইবার আক্রমণ পদ্ধতি, যেখানে হ্যাকার আগে থেকে তৈরি করা সম্ভাব্য পাসওয়ার্ডের তালিকা (Dictionary) ব্যবহার করে কোনো অ্যাকাউন্টের পাসওয়ার্ড ভাঙার চেষ্টা করে।"
    },
    {
        "id": 31,
        "page": 916,
        "question": "What is the primary purpose of a \"Demilitarized zone\" (DMZ)? [BB-2026]",
        "options": [
            "To store the core database",
            "To host public-facing services (Web, Email) separate from the internal LAN",
            "To connect the CEO's computer to the internet",
            "To test viruses safely"
        ],
        "answer": "খ",
        "explanation": "Demilitarized Zone (DMZ) হলো একটি নেটওয়ার্ক সেগমেন্ট, যা একটি প্রতিষ্ঠান বা সংস্থার ভিতরের নেটওয়ার্ক (Internal Network) এবং ইন্টারনেটের মধ্যে রাখা হয়, যাতে বাইরের ব্যবহারকারীরা নির্দিষ্ট সার্ভারগুলোতে প্রবেশ করতে পারে, কিন্তু ভিতরের নেটওয়ার্ক নিরাপদ থাকে।"
    },
    {
        "id": 32,
        "page": 916,
        "question": "Which command is used to view active connections and listening ports? [BB-2026]",
        "options": [
            "netstat",
            "ping",
            "nslookup",
            "ipconfig"
        ],
        "answer": "ক",
        "explanation": "netstat কমান্ডের মাধ্যমে নেটওয়ার্কের active connections ও listening ports দেখা যায়।"
    },
    {
        "id": 33,
        "page": 916,
        "question": "What is the decimal value of the binary number 111? [BB-2026]",
        "options": [
            "3",
            "5",
            "7",
            "9"
        ],
        "answer": "গ",
        "explanation": "(111)₂ = 1 × 4 + 1 × 2 + 1 × 1 = (7)₁₀"
    },
    {
        "id": 34,
        "page": 916,
        "question": "The data structure required to check whether an expression contains a balanced parenthesis is- [BB-2026]",
        "options": [
            "Stack",
            "Queue",
            "Tree",
            "Array"
        ],
        "answer": "ক",
        "explanation": "Stack হলো একটি LIFO (Last In, First Out) ডাটা স্ট্রাকচার যেখানে শেষ প্রবেশ করা উপাদানটিই প্রথমে বের হয়। বৈশিষ্ট্যের কারণে এটি Parentheses matching-এর জন্য আদর্শ কারণ প্রতিটি ওপেন ব্র্যাকেট push করা হয় এবং ক্লোজ ব্র্যাকেট এলে সর্বশেষ push করা ব্র্যাকেট pop করে মিল যাচাই করা হয়।"
    },
    {
        "id": 35,
        "page": 916,
        "question": "What data structure often results in a time-space tradeoff by using extra memory to speed up operations? [BB-2026]",
        "options": [
            "Arrays",
            "Hash tables",
            "Stacks",
            "Queues"
        ],
        "answer": "খ",
        "explanation": "Hash Table অতিরিক্ত মেমরি ব্যবহার করে (hash table- এর সাইজ বা buckets) যাতে ডাটা দ্রুত খোঁজা, যোগ বা মুছে ফেলার অপারেশন O(1) সময়ে করা যায়। এটি Time-space tradeoff এর উদাহরণ, যেখানে বেশি মেমরি ব্যবহার করে সময় বাঁচানো হয়।"
    },
    {
        "id": 36,
        "page": 916,
        "question": "Which dynamic programming approach starts solving from the smallest subproblems? [BB-2026]",
        "options": [
            "Greedy approach",
            "Recursive approach",
            "Top-down approach",
            "Bottom-up approach"
        ],
        "answer": "ঘ",
        "explanation": "Bottom-Up Dynamic Programming হলো এমন একটি পদ্ধতি, যেখানে ছোট ছোট সাবপ্রবলেমের সমাধান আগে করা হয় এবং সেগুলো ব্যবহার করে ধীরে ধীরে বড় সমস্যা সমাধান করা হয়; এতে intermediate ফলাফল টেবিল বা অ্যারেতে সংরক্ষণ করা হয়, ফলে একই হিসাব বারবার করার প্রয়োজন পড়ে না।"
    },
    {
        "id": 37,
        "page": 916,
        "question": "Which of the following services use TCP? [BB-2026]",
        "options": [
            "DHCP",
            "SMTP",
            "CSMA",
            "DNS"
        ],
        "answer": "খ",
        "explanation": "SMTP TCP ব্যবহার করে, কারণ এটি বিশ্বস্ততার সাথে ইমেইল পাঠানোর জন্য ডিজাইন করা। TCP নিশ্চিত করে যে, ডাটা ঠিকভাবে পৌঁছাবে এবং কোনো অংশ হারাবে না, তাই SMTP-এর জন্য উপযুক্ত।"
    },
    {
        "id": 38,
        "page": 916,
        "question": "Which standard TCP port is assigned for contracting SSH servers? [BB-2026]",
        "options": [
            "21",
            "22",
            "23",
            "24"
        ],
        "answer": "খ",
        "explanation": "SSH সার্ভার সাধারণত TCP পোর্ট 22 ব্যবহার করে।"
    },
    {
        "id": 39,
        "page": 916,
        "question": "The memory that is allocated for any object is- [BB-2026]",
        "options": [
            "Cache",
            "HDD",
            "ROM",
            "RAM"
        ],
        "answer": "ঘ",
        "explanation": "প্রোগ্রাম চলাকালীন Object-গুলো RAM-এ সংরক্ষিত হয়।"
    },
    {
        "id": 40,
        "page": 916,
        "question": "What does ACID stand for in database transactions? [BB-2026]",
        "options": [
            "All Columns in Database",
            "Atomicity, Consistency, Isolation, Durability",
            "Automated Commit in Database",
            "Association of Conditions in Data"
        ],
        "answer": "খ",
        "explanation": "ACID হলো ডাটাবেজ ট্রানজেকশনের চারটি গুরুত্বপূর্ণ বৈশিষ্ট্য, যা ডাটার সঠিকতা ও স্থায়িত্ব নিশ্চিত করে।\n• A - Atomicity : ট্রানজেকশন সম্পূর্ণভাবে সফল হবে বা একেবারেই হবে না; আংশিক পরিবর্তন থাকবে না।\n• C - Consistency : ট্রানজেকশন শেষ হওয়ার পর ডাটাবেজ সব নিয়ম ও কনস্ট্রেইন্ট মেনে চলবে।\n• I - Isolation : একাধিক ট্রানজেকশন একসাথে চললেও একে অপরের উপর প্রভাব ফেলবে না।\n• D - Durability : ট্রানজেকশন সম্পন্ন হলে ডাটা স্থায়ী হবে, কোনো সিস্টেম ক্র্যাশ হলেও ডাটা হারাবে না।"
    }
]
