import json

with open('JSON Data/Ict-wizard-NTRCA-313-and-325/অধ্যায়- ঙ. অপারেটিভ পদ্ধতি.json', encoding='utf-8') as f:
    ref_data = json.load(f)

os_mcqs = []

# Questions 1 to 22 from ref_data (indices 0 to 21)
for i in range(22):
    item = ref_data[i]
    os_mcqs.append({
        "id": len(os_mcqs) + 1,
        "question": item["question"],
        "options": item["options"],
        "answer": item["answer"]
    })

# In the PDF, Q23 was skipped in numbering, jumping straight to Q24 (ref_data index 23: COMMAND.COM)
# Questions 24 to 39 in PDF correspond to ref_data indices 23 to 25 and 27 to 38
# Wait, let's verify indices:
# ref_data[23]: COMMAND.COM (PDF Q24)
# ref_data[24]: মাইক্রোসফট উইন্ডোজ কোন ধরনের ইন্টারফেস ব্যবহার করে? (PDF Q25)
# ref_data[25]: GUI এর পূর্ণরূপ কী? (PDF Q26)
# ref_data[26]: মাইক্রোসফট উইন্ডোজের প্রথম ভার্সন কত সালে মুক্তি পায়? (not in PDF page 8, PDF jumped to Q28!)
# ref_data[27]: উইন্ডোজের কোন সংস্করণটি প্রথম পূর্ণাঙ্গ 32-বিট... (PDF Q28)
# ref_data[28]: উইন্ডোজ ভিস্তা এর পরবর্তী সংস্করণ কোনটি? (PDF Q29)
# ref_data[29]: বর্তমানে মাইক্রোসফটের সবচেয়ে ব্যবহৃত... (PDF Q30)
# ref_data[30]: উইন্ডোজ অপারেটিং সিস্টেমে 'Task Manager'... (PDF Q31)
# ref_data[31]: উইন্ডোজ অপারেটিং সিস্টেমে কোনো ফাইল বা ফোল্ডার স্থায়ীভাবে... (PDF Q32)
# ref_data[32]: উইন্ডোজের ডেস্কটপে কোনো প্রোগ্রাম... (PDF Q33)
# ref_data[33]: উইন্ডোজে বর্তমানে সক্রিয় উইন্ডো বন্ধ করার... (PDF Q34)
# ref_data[34]: উইন্ডোজের কোন অংশটি ব্যবহারকারী এবং কম্পিউটারের মধ্যে সেতু... (PDF Q35)
# ref_data[35]: উইন্ডোজের কোর বা মূল অংশ কোনটি... (PDF Q36)
# ref_data[36]: উইন্ডোজের সর্বশেষ সংস্করণ কোনটি? (PDF Q37)
# ref_data[37]: উইন্ডোজ অপারেটিং সিস্টেমে ফাইল বা ফোল্ডার খুঁজে... (PDF Q38)
# ref_data[38]: উইন্ডোজ 95/98-এ কোন সুবিধাটি MS-DOS-এর চেয়ে বড় পরিবর্তন এনেছিল? (PDF Q39)

selected_indices = [23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]
for idx in selected_indices:
    item = ref_data[idx]
    os_mcqs.append({
        "id": len(os_mcqs) + 1,
        "question": item["question"],
        "options": item["options"],
        "answer": item["answer"]
    })

# Section 2: Questions 1 to 18 from Pages 15 and 16
sec2_questions = [
  {
    "question": "নিচের কোনটি অপারেটিং সিস্টেম নয়? [অধিদপ্তর]",
    "options": ["লিনাক্স", "মজিলা", "উইন্ডোজ", "উবুন্টু"],
    "answer": "খ"
  },
  {
    "question": "নিচের কোনটি সিস্টেম সফটওয়্যার? [অধিদপ্তর]",
    "options": ["এমএস এক্সেল", "নোটপ্যাড", "উইন্ডোজ ভিস্তা", "ওরাকল"],
    "answer": "গ"
  },
  {
    "question": "নিচের কোন স্মার্টফোন অপারেটিং সিস্টেমটি ওপেন সোর্স প্ল্যাটফর্ম? [BCS 2015]",
    "options": ["iOS", "Windows phone", "Android", "Symbian"],
    "answer": "গ"
  },
  {
    "question": "নিচের কোনটি OS এর কাজ নয়? [BANK]",
    "options": ["ইউজার ইন্টারফেস সরবরাহ করা", "হার্ডওয়্যার ডিভাইস নিয়ন্ত্রণ করা", "নেটওয়ার্ক থেকে স্বয়ংক্রিয়ভাবে ফাইল কপি করা", "প্রোগ্রাম সচল রাখা"],
    "answer": "গ"
  },
  {
    "question": "নিচের কোনটি একটি কম্পিউটার অপারেটিং সিস্টেম? [BANK]",
    "options": ["Java", "C++", "Oracle", "LINUX"],
    "answer": "ঘ"
  },
  {
    "question": "নিচের কোনটি পিসিতে ব্যবহৃত সর্বাপেক্ষা জনপ্রিয় অপারেটিং সিস্টেম? [BANK]",
    "options": ["Apple MAC OS X", "DOS", "Microsoft Windows", "UNIX"],
    "answer": "গ"
  },
  {
    "question": "UNIX অপারেটিং সিস্টেমের উদ্ভাবক প্রতিষ্ঠান? [BANK]",
    "options": ["Intel", "IBM", "Apple", "Bell Lab"],
    "answer": "ঘ"
  },
  {
    "question": "DOS অপারেটিং সিস্টেমের প্রস্তুতকারী প্রতিষ্ঠান কোনটি? [BANK]",
    "options": ["Apple", "IBM", "Microsoft", "INTEL"],
    "answer": "গ"
  },
  {
    "question": "একটি প্রসেস হলো: [Ministry]",
    "options": ["ডিস্কে সংরক্ষিত নির্দেশাবলীর সেট", "থ্রেডের মতো একই", "একটি ভাইরাস", "এক্সিকিউশনে থাকা একটি প্রোগ্রামের ইনস্ট্যান্স"],
    "answer": "ঘ"
  },
  {
    "question": "Operating System is an/a - [অপারেটিং সিস্টেম হল-]",
    "options": ["Collection of Application Software", "Utility Software", "System Software", "Collection of Similar Software"],
    "answer": "গ"
  },
  {
    "question": "যখন একটি Process একটি I/O অপারেশন সম্পন্ন হওয়ার জন্য অপেক্ষা করে, তখন প্রসেসটির সেই অবস্থাকে কী বলা হয়?",
    "options": ["Running", "New", "Waiting", "Terminated"],
    "answer": "গ"
  },
  {
    "question": "A deadlock is a state where: [ডেডলক এমন অবস্থা যেখানে--]",
    "options": ["A process has finished its execution.", "Two or more processes are waiting for a resource held by another.", "The operating system is booting up.", "A single process is using all the system's resources."],
    "answer": "খ"
  },
  {
    "question": "একটি প্রসেস t1 সময়ে এসে পৌঁছায়, যার Burst Time t2 এবং প্রসেসটি t3 সময়ে সম্পূর্ণ হয়। এই প্রসেসটির Turnaround Time কত? [bpsc Non Cadre]",
    "options": ["t1+t2", "t3-t1", "t3-t2", "t1+t"],
    "answer": "খ"
  },
  {
    "question": "একটি প্রসেসের Arrival Time 10 ms এবং Completion Time 25 ms। যদি প্রসেসটির Burst Time ms হয়, তাহলে প্রসেসটির Waiting Time কত? [bpsc Non Cadre]",
    "options": ["3ms", "22ms", "15ms", "12ms"],
    "answer": "ক"
  },
  {
    "question": "A page fault occurs when: [49th BCS]",
    "options": ["deadlock happens", "segmentation starts", "page is found in memory", "page is not found in memory"],
    "answer": "ঘ"
  },
  {
    "question": "______ is a non-preemptive algorithm. [49th BCS]",
    "options": ["FCFS", "Round Robin", "Shortest Remaining Time", "None of the above"],
    "answer": "ক"
  },
  {
    "question": "OS System Calls perform the following basic operations on files: [49th BCS]",
    "options": ["Read, Write, Delete", "Write, Print, Reposition", "Delete, Truncate, Sort Data", "Modify, update, sort data"],
    "answer": "ক"
  },
  {
    "question": "Assuming P1, P2, P3 have burst time (in ms) 6, 8, 3, respectively, which statement is true about SJF? [49th BCS]",
    "options": ["Waiting time of P1 is 3ms", "Turn around time of P1 is 8ms", "Completion time of p2 is 17ms", "Turn around time of P3 is 9ms"],
    "answer": "ক"
  }
]

for item in sec2_questions:
    os_mcqs.append({
        "id": len(os_mcqs) + 1,
        "question": item["question"],
        "options": item["options"],
        "answer": item["answer"]
    })

with open('JSON Data/BPSC ICT Wizard/9. Operating System.json', 'w', encoding='utf-8') as f:
    json.dump(os_mcqs, f, ensure_ascii=False, indent=2)

print('Saved 9. Operating System.json with', len(os_mcqs), 'MCQs')
