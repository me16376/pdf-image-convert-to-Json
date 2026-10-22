# -*- coding: utf-8 -*-
import json
import os

questions = [
    # Section 1: Pages 7-8 (4 MCQs)
    {
        "id": 1,
        "question": "IPv6 address length? [IPv6 address কত বিট?] [BPSC AP'20, AME'19]",
        "options": ["32 Bits", "128 Bits", "256 Bits", "64 Bits"],
        "answer": "B"
    },
    {
        "id": 2,
        "question": "Routing is clearly the major issue for? [ রাউটিং কোন লেয়ারের অন্যতম কাজ] [BPSC AME'19]",
        "options": ["Transport layer", "Data link layer", "Network Layer", "Physical Layer"],
        "answer": "C"
    },
    {
        "id": 3,
        "question": "Congestion Control happened... [কনগেশন কন্ট্রোল ঘটে ...] ? [BPSC AME'19]",
        "options": ["Transport layer", "Data link layer", "Network Layer", "Physical Layer"],
        "answer": "B"
    },
    {
        "id": 4,
        "question": "DHCP DISCOVER message is [DHCP DISCOVER হচ্ছে ?] ? [BPSC ANE'19]",
        "options": ["Unicast", "Anycast", "Multicast", "Broadcast"],
        "answer": "D"
    },

    # Section 2: Pages 9-10 (6 MCQs)
    {
        "id": 5,
        "question": "Bridge is a ............ device[ব্রিজ হচ্ছে একটি ...... ডিভাইস]? [BPSC AME'19]",
        "options": ["layer 2", "layer 1", "layer 3", "layer 2 & 3"],
        "answer": "A"
    },
    {
        "id": 6,
        "question": "Which device can stop broadcast? [নিচের কোন ডিভাইস ব্রডকাস্ট বন্ধ করে?] [BPSC ANE'19]",
        "options": ["Router", "Switch", "RJ45", "HUB"],
        "answer": "A"
    },
    {
        "id": 7,
        "question": "How many Cables need for 5 Device in Mesh Topology? [ ৫টা ডিভাইসের জন্য মেস টপোলজিতে কয়টি ক্যাবল লাগে?]",
        "options": ["5", "6", "10", "11"],
        "answer": "C"
    },
    {
        "id": 8,
        "question": "A network that connects multiple star topologies to a central bus backbone is known as a: [যদি নেটওয়ার্কে একাধিক স্টার টপোলজি একটা সেন্ট্রাল বাস ব্যাকবোনে যুক্ত করলে যে টপোলজি হয়?]",
        "options": ["Mesh", "Ring", "Tree", "Hybrid"],
        "answer": "C"
    },
    {
        "id": 9,
        "question": "Unidirectional Data Transmission happened in --- [ইউনিডিরেক্টয়.../একমুখী ডাটা ট্রান্সমিশন হয়...]",
        "options": ["Mesh", "Ring", "Tree", "Hybrid"],
        "answer": "B"
    },
    {
        "id": 10,
        "question": "-------- topology requires a multipoint connection. [... টপোলজিতে একাধিক কানেকশন লাগে]",
        "options": ["Mesh", "Ring", "star", "bus"],
        "answer": "D"
    },

    # Section 3: Pages 12-13 (14 MCQs)
    {
        "id": 11,
        "question": "Which one is related to Email Services? [নিচের কোনটি ইমেইল সার্ভিসের সাথে জড়িত] [BPSC AP'20]",
        "options": ["SMTP", "TELNET", "UDP", "SSH"],
        "answer": "A"
    },
    {
        "id": 12,
        "question": "FTP Protocol used -[FTP প্রোটোকল ব্যবহার করা হয়] ? [BPSC AP'20, ANE'19]",
        "options": ["IP", "UDP", "SMTP", "TCP"],
        "answer": "D"
    },
    {
        "id": 13,
        "question": "Which one is first Network - [নিচের কোনটি প্রথম নেটওয়ার্ক]? [BPSC AP'20]",
        "options": ["CNNET", "ASPANET", "NSFNET", "ARPANET"],
        "answer": "D"
    },
    {
        "id": 14,
        "question": "Name of the protocol to find MAC address using IP Address [IP Address থেকে MAC বের করার পদ্ধতিকে বলে...] ? [BPSC ANE'19]",
        "options": ["RIP", "TCP", "ARP", "BGP"],
        "answer": "C"
    },
    {
        "id": 15,
        "question": "UDP Protocol Used [UDP প্রোটোকল ব্যবহার করে]? [BPSC ANE'19]",
        "options": ["SMPT", "DNS", "HTTP", "FTP"],
        "answer": "B"
    },
    {
        "id": 16,
        "question": "Which of the following is a characteristic of TCP [TCP এর বৈশিষ্ট্য নিচের কোনটি]?",
        "options": ["Connectionless", "Unreliable", "Connection-oriented", "Used for fast, real-time applications"],
        "answer": "C"
    },
    {
        "id": 17,
        "question": "Which application layer protocol relies on TCP for reliable data transfer [নিচের কোন অ্যাপ্লিকেশন লেয়ার প্রোটোকল TCP এর উপর নির্ভরশীল] ?",
        "options": ["DNS", "HTTP", "UDP", "DHCP"],
        "answer": "B"
    },
    {
        "id": 18,
        "question": "IP is considered a _________ protocol [আইপি এড্রেস হচ্ছে ...].",
        "options": ["Connectionless", "Connection-oriented", "Unreliable", "Both a and c"],
        "answer": "A"
    },
    {
        "id": 19,
        "question": "What does UDP lack that TCP provides [নিচের কোনটি TCP তে আছি কিন্তু UDP তে নাই]?",
        "options": ["Addressing", "Port numbers", "Reliability and flow control", "Data transfer capability"],
        "answer": "C"
    },
    {
        "id": 20,
        "question": "Which protocol is primarily used by DNS for simple queries [DNS কোয়েরির জন্য প্রধানত ইউজার ডেটাগ্রাম প্রোটোকল (UDP) ব্যবহৃত হয়...]?",
        "options": ["TCP", "UDP", "HTTP", "SMTP"],
        "answer": "B"
    },
    {
        "id": 21,
        "question": "Automatically IP এসাইন করার নিয়মকে বলে --?",
        "options": ["DHCP", "HTTP", "TCP", "DNS"],
        "answer": "A"
    },
    {
        "id": 22,
        "question": "SSH Port নাম্বার কত?",
        "options": ["21", "22", "20", "23"],
        "answer": "B"
    },
    {
        "id": 23,
        "question": "Data communication যখন দেশ থেকে অন্য দেশ কানেক্ট করে তাকে বলে ?",
        "options": ["LAN", "WAN", "MAN", "PAN"],
        "answer": "B"
    },
    {
        "id": 24,
        "question": "Data communication যদি একটা ক্যাম্পাসের মধ্যে হয় তখন সেটাকে বলে_______",
        "options": ["LAN", "WAN", "MAN", "PAN"],
        "answer": "A"
    },

    # Section 4: Pages 19-20 (14 MCQs)
    {
        "id": 25,
        "question": "কোন তারযুক্ত মাধ্যমে ডেটা স্থানান্তরের জন্য আলোর পালস ব্যবহৃত হয়?",
        "options": ["Twisted Pair Cable", "Coaxial Cable", "Fiber Optic Cable", "Ethernet Cable"],
        "answer": "গ"
    },
    {
        "id": 26,
        "question": "তারবিহীন সংযোগগুলোর মধ্যে কোনটি সাধারণত স্বল্প দূরত্বে এবং কম গতিতে ডিভাইস যুক্ত করতে ব্যবহৃত হয়?",
        "options": ["Wi-Fi", "Bluetooth", "Satellite", "Cellular (5G)"],
        "answer": "খ"
    },
    {
        "id": 27,
        "question": "Twisted Pair Cable-এ তারগুলো প্যাঁচানো থাকার প্রধান কারণ কী?",
        "options": [
            "ক্যাবলের দাম কমানো",
            "ইলেক্ট্রোম্যাগনেটিক Interference হ্রাস করা",
            "ডেটা ট্রান্সমিশনের গতি বাড়ানো",
            "ক্যাবলকে আরও নমনীয় করা"
        ],
        "answer": "খ"
    },
    {
        "id": 28,
        "question": "Wired নেটওয়ার্কের একটি প্রধান সুবিধা কোনটি?",
        "options": [
            "গতিশীলতা",
            "ইনস্টলেশন সহজ",
            "কাভারেজ দূরত্ব বেশি",
            "উচ্চ নির্ভরযোগ্যতা ও নিরাপত্তা"
        ],
        "answer": "ঘ"
    },
    {
        "id": 29,
        "question": "Wi-Fi কোন ধরনের নেটওয়ার্ক মিডিয়ামের উদাহরণ?",
        "options": ["Guided Medium", "Unguided Medium", "Coaxial Medium", "Optical Medium"],
        "answer": "খ"
    },
    {
        "id": 30,
        "question": "নেটওয়ার্ক নিরাপত্তা ব্যবস্থা, যা পূর্বনির্ধারিত নিয়মের ভিত্তিতে ইনকামিং এবং আউটগোয়িং ট্র্যাফিক নিয়ন্ত্রণ ও নিরীক্ষণ করে— তার নাম কী?",
        "options": ["অ্যান্টিভাইরাস", "এনক্রিপশন", "ফায়ারওয়াল", "ইন্ট্রুশন ডিটেকশন সিস্টেম"],
        "answer": "গ"
    },
    {
        "id": 31,
        "question": "কোন সাইবার অ্যাটাক কৌশলটি ব্যবহারকারীকে বিশ্বস্ত উৎস সেজে সংবেদনশীল তথ্য (যেমন: পাসওয়ার্ড) ফাঁস করতে প্ররোচিত করে?",
        "options": ["ফিশিং", "DoS অ্যাটাক", "ম্যান-ইন-দ্য-মিডল", "র‍্যানসমওয়্যার"],
        "answer": "ক"
    },
    {
        "id": 32,
        "question": "কোন ম্যালওয়্যার সিস্টেমের ফাইল এনক্রিপ্ট করে এবং অ্যাক্সেসের জন্য মুক্তিপণ দাবি করে?",
        "options": ["ট্রোজান হর্স", "ভাইরাস", "ওয়ার্ম", "র‍্যানসমওয়্যার"],
        "answer": "ঘ"
    },
    {
        "id": 33,
        "question": "একটি সার্ভার বা নেটওয়ার্ককে অতিরিক্ত ট্র্যাফিক বা রিকোয়েস্ট পাঠিয়ে অপ্রাপ্য করে তোলার অ্যাটাকটির নাম কী?",
        "options": ["ফিশিং", "ডিনায়াল অফ সার্ভিস", "এসকিউএল ইনজেকশন", "প্যাকেট স্নিফিং"],
        "answer": "খ"
    },
    {
        "id": 34,
        "question": "একটি পাবলিক নেটওয়ার্কের উপর দিয়ে ডেটা পাঠানোর সময় গোপনীয়তা ও নিরাপত্তা নিশ্চিত করতে কোনটি একটি এনক্রিপ্টেড টানেল তৈরি করে?",
        "options": ["ফায়ারওয়াল", "IDS", "NAC", "ভার্চুয়াল প্রাইভেট নেটওয়ার্ক"],
        "answer": "ঘ"
    },
    {
        "id": 35,
        "question": "আক্রমণকারী যখন প্রেরক এবং প্রাপকের যোগাযোগের মধ্যে নীরবে ডেটা চুরি বা পরিবর্তন করে, সেই অ্যাটাকের নাম কী?",
        "options": ["DoS অ্যাটাক", "ফিশিং", "ম্যান-ইন-দ্য-মিডল", "ক্রস-সাইট স্ক্রিপ্টিং"],
        "answer": "গ"
    },
    {
        "id": 36,
        "question": "ডেটাকে শুধুমাত্র অনুমোদিত প্রাপকের জন্য পাঠযোগ্য করার প্রক্রিয়াকে কী বলা হয়?",
        "options": ["এনক্রিপশন", "ডিক্রিপশন", "অথেনটিকেশন", "অ্যাক্সেস কন্ট্রোল"],
        "answer": "ক"
    },
    {
        "id": 37,
        "question": "একটি নেটওয়ার্কের নিরাপত্তা দুর্বলতা বা সন্দেহজনক কার্যকলাপ শনাক্ত করার জন্য ব্যবহৃত হয় কোনটি?",
        "options": ["VPN", "ফায়ারওয়াল", "ইন্ট্রুশন ডিটেকশন সিস্টেম", "এনক্রিপশন"],
        "answer": "গ"
    },
    {
        "id": 38,
        "question": "একটি Botnet অ্যাটাকের প্রধান উদ্দেশ্য কী?",
        "options": ["একক ইউজারের পাসওয়ার্ড চুরি করা", "DDoS অ্যাটাক চালানো", "ইমেল ফিশিং করা", "ফিজিক্যাল ক্যাবল কেটে দেওয়া"],
        "answer": "খ"
    },

    # Section 5: Pages 23-25 (15 MCQs)
    {
        "id": 39,
        "question": "ডেটা কমিউনিকেশন সিস্টেমে ডেটা আদান-প্রদানের জন্য ব্যবহৃত নিয়ম বা পদ্ধতির সেটকে কী বলা হয়?",
        "options": ["প্রসেসর", "মাধ্যম", "বার্তা", "প্রোটোকল"],
        "answer": "ঘ"
    },
    {
        "id": 40,
        "question": "কোন তারবিহীন প্রযুক্তিটি সাধারণত শুধুমাত্র স্বল্প পরিসরের ডিভাইস সংযোগের জন্য ব্যবহৃত হয়?",
        "options": ["Wi-Fi", "Bluetooth", "Cellular Network", "Satellite"],
        "answer": "খ"
    },
    {
        "id": 41,
        "question": "তারযুক্ত মাধ্যমগুলোর মধ্যে কোনটিতে ইলেক্ট্রোম্যাগনেটিক হস্তক্ষেপ (EMI) হওয়ার সম্ভাবনা সবচেয়ে কম?",
        "options": ["Twisted Pair Cable", "Coaxial Cable", "Fiber Optic Cable", "Ethernet Cable"],
        "answer": "গ"
    },
    {
        "id": 42,
        "question": "দুটি ডিভাইসের মধ্যে ডেটা আদান-প্রদান করার সময় তথ্যকে দুর্বোধ্য ফর্মে পরিবর্তন করার প্রক্রিয়াকে কী বলে?",
        "options": ["ডিক্রিপশন", "অথেনটিকেশন", "এনক্রিপশন", "ব্রডকাস্ট"],
        "answer": "গ"
    },
    {
        "id": 43,
        "question": "ডেটা কমিউনিকেশনের ক্ষেত্রে, প্রেরক ও প্রাপক ডিভাইসের মাঝে ডেটা বহনের জন্য ব্যবহৃত ভৌত পথকে কী বলে?",
        "options": ["প্রোটোকল", "মাধ্যম", "টার্মিনাল", "মোডেম"],
        "answer": "খ"
    },
    {
        "id": 44,
        "question": "কোন ডেটা প্রবাহের মোডে ডেটা শুধুমাত্র এক দিকেই প্রবাহিত হতে পারে?",
        "options": ["হাফ-ডুপ্লেক্স", "সিমপ্লেক্স", "ফুল-ডুপ্লেক্স", "মাল্টিকাস্ট"],
        "answer": "খ"
    },
    {
        "id": 45,
        "question": "ওয়াকি-টকি (Walkie-Talkie) নিচের কোন ডেটা প্রবাহের মোড অনুসরণ করে?",
        "options": ["ফুল-ডুপ্লেক্স", "হাফ-ডুপ্লেক্স", "সিমপ্লেক্স", "ইউনিকাস্ট"],
        "answer": "খ"
    },
    {
        "id": 46,
        "question": "টেলিফোনে কথোপকথন নিচের কোন ডেটা প্রবাহের মোডের সর্বোত্তম উদাহরণ?",
        "options": ["হাফ-ডুপ্লেক্স", "সিমপ্লেক্স", "ফুল-ডুপ্লেক্স", "ব্রডকাস্ট"],
        "answer": "গ"
    },
    {
        "id": 47,
        "question": "একটি উৎস থেকে একই নেটওয়ার্ক সেগমেন্টের সমস্ত ডিভাইসের কাছে ডেটা পাঠানোর পদ্ধতিকে কী বলে?",
        "options": ["ইউনিকাস্ট", "মাল্টিকাস্ট", "ব্রডকাস্ট", "এনিকাস্ট"],
        "answer": "গ"
    },
    {
        "id": 48,
        "question": "লাইভ ভিডিও স্ট্রিমিং এবং অনলাইন গেমিং-এর ক্ষেত্রে ব্যান্ডউইথ সাশ্রয়ের জন্য কোন ডেটা বিতরণের মোড ব্যবহৃত হয়?",
        "options": ["ব্রডকাস্ট", "ইউনিকাস্ট", "মাল্টিকাস্ট", "এনিকাস্ট"],
        "answer": "গ"
    },
    {
        "id": 49,
        "question": "সিরিয়াল ট্রান্সমিশনের ক্ষেত্রে ডেটা বাইট বা অক্ষরগুলো একটি নির্দিষ্ট সময় ব্যবধানে ব্লক আকারে পাঠানোর পদ্ধতিকে কী বলে?",
        "options": ["অ্যাসিনক্রোনাস", "সিনক্রোনাস", "প্যারালাল", "হাফ-ডুপ্লেক্স"],
        "answer": "খ"
    },
    {
        "id": 50,
        "question": "অ্যাসিনক্রোনাস সিরিয়াল ট্রান্সমিশনে প্রতিটি ডেটা বাইট বা অক্ষরের সমাপ্তি নির্দেশ করতে কোনটি ব্যবহৃত হয়?",
        "options": ["স্টার্ট বিট", "স্টপ বিট", "ক্লক সিগন্যাল", "প্যারিটি বিট"],
        "answer": "খ"
    },
    {
        "id": 51,
        "question": "কম্পিউটার এবং প্রিন্টারের মতো স্বল্প দূরত্বের ডিভাইসের মধ্যে দ্রুত ডেটা স্থানান্তরের জন্য কোন পদ্ধতিটি ব্যবহার করা যেতে পারে?",
        "options": ["সিরিয়াল ট্রান্সমিশন", "প্যারালাল ট্রান্সমিশন", "সিনক্রোনাস ট্রান্সমিশন", "ফাইবার অপটিক ট্রান্সমিশন"],
        "answer": "খ"
    },
    {
        "id": 52,
        "question": "সিনক্রোনাস ট্রান্সমিশনের একটি প্রধান সুবিধা কী?",
        "options": ["Start/Stop বিটের ব্যবহার", "সরল হার্ডওয়্যার", "ডেটা স্থানান্তরের দক্ষতা ও গতি", "অনিয়মিত বিরতিতে ডেটা প্রেরণ"],
        "answer": "গ"
    },
    {
        "id": 53,
        "question": "ডেটা বিটগুলো একটিমাত্র চ্যানেল ব্যবহার করে একের পর এক পর্যায়ক্রমে পাঠানোর পদ্ধতিকে কী বলে?",
        "options": ["প্যারালাল ট্রান্সমিশন", "সিরিয়াল ট্রান্সমিশন", "ফুল-ডুপ্লেক্স", "মাল্টিকাস্ট"],
        "answer": "খ"
    }
]

out_dir = "JSON Data/BPSC ICT Wizard"
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, "3. Data Communication and Networking.json")

with open(out_file, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Saved {len(questions)} MCQs to {out_file}")
