# -*- coding: utf-8 -*-
import json
import os

questions = [
    {
        "id": 1,
        "question": "Which one is non-linear Data Structure? [নিচের কোনটি non-linear ডাটা স্ট্রাকচার?]",
        "options": ["Stack", "List", "Array", "Map"],
        "answer": "D"
    },
    {
        "id": 2,
        "question": "Which one follow LIFO? [নিচের কোনটি LIFO অনুসরণ করে] (BPSC AP, AME)",
        "options": ["Stack", "Linked list", "Array", "Queue"],
        "answer": "A"
    },
    {
        "id": 3,
        "question": "POP/PUSH related to? [POP/PUSH কোনটার সাথে সম্পর্কিত?] (Bank)",
        "options": ["Stack", "Linked list", "Array", "Queue"],
        "answer": "A"
    },
    {
        "id": 4,
        "question": "In which, Data elements stored at Continuous memory location? [ডেটা এলিমেন্টস পাশাপাশি মেমরি লোকেশন সংরক্ষণ করা হয় কোনটায়?]",
        "options": ["Stack", "Linked list", "Array", "Queue"],
        "answer": "C"
    },
    {
        "id": 5,
        "question": "\"Patient serial for Doctor\" related to? [\"ডাক্তারের জন্য রোগীর সিরিয়াল\" কোন ডেটা স্ট্রাকচারের সাথে সম্পর্কিত?]",
        "options": ["Stack", "Linked list", "Array", "Queue"],
        "answer": "D"
    },
    {
        "id": 6,
        "question": "Which data structure is a collection of elements where each element is connected to the next and previous element? [কোন ডেটা স্ট্রাকচার এ প্রতিটি এলিমেন্টস পরবর্তী এবং পূর্ববর্তী এলিমেন্টস সাথে সংযুক্ত থাকে?]",
        "options": ["Stack", "Queue", "Linked List", "Array"],
        "answer": "C"
    },
    {
        "id": 7,
        "question": "What is the process of adding an element to a queue called? [একটি Queue তে একটি element যুক্ত করার প্রক্রিয়াকে কী বলা হয়?]",
        "options": ["Push", "Pop", "Enqueue", "Dequeue"],
        "answer": "C"
    },
    {
        "id": 8,
        "question": "What is the primary advantage of a linked list over an array? [Array চেয়ে Linked List এ প্রধান সুবিধা কী?]",
        "options": ["Faster random access to elements", "Static size", "Dynamic size", "Better cache performance"],
        "answer": "C"
    },
    {
        "id": 9,
        "question": "Link list can be implemented by? [নিচের কোনটি Linked List মাধ্যমে ইমপ্লিমেন্ট করা যায়?] (Bank)",
        "options": ["Array", "Pointer", "Recursion", "Both A & B"],
        "answer": "D"
    },
    {
        "id": 10,
        "question": "Link list have minimum two field on is Data another? লিঙ্কড লিস্টের কমপক্ষে দুটি ফিল্ড থাকে, একটি হলো ডেটা, অন্যটি কী? (BPSC AP)",
        "options": ["Pointer to char", "Pointer", "Node", "Null"],
        "answer": "B"
    },
    {
        "id": 11,
        "question": "Which of the following expressions is a valid postfix expression? [নিচের এক্সপ্রেশনগুলির মধ্যে কোনটি একটি বৈধ পোস্টফিক্স এক্সপ্রেশন? ] (BPSC AP)",
        "options": ["+ 2 3", "2 + 3", "2 3 +", "(2 + 3)"],
        "answer": "C"
    },
    {
        "id": 12,
        "question": "Scheduling queue is generally stored as [শিডিউলিং কিউতে সাধারণত কোন ডেটা স্ট্রাকচার হিসেবে সংরক্ষণ করা হয়?] (BPSC AME)",
        "options": ["Stack", "Queue", "Linked List", "Array"],
        "answer": "C"
    },
    {
        "id": 13,
        "question": "What is the precedence of arithmetic operator (High-Low) [অ্যারিথমেটিক অপারেটর বড় থেকে ছোট অনুযায়ী কি হবে?] - (Bank)",
        "options": ["*,/,%,+,-", "/, %,*, ,+,-", "%,/,*,+,-", "-, +,*,/,%,"],
        "answer": "C"
    },
    {
        "id": 14,
        "question": "Which Type of Data structure use recursion in Java [Java তে রিকার্শনের জন্য কোন ধরনের ডাটা স্ট্রাকচার ব্যবহার করা হয়?] - (Bank)",
        "options": ["Stack", "Queue", "Linked List", "Array"],
        "answer": "A"
    },
    {
        "id": 15,
        "question": "BFS related to? [BFS কিসের সাথে সম্পৃক্ত]",
        "options": ["Tree", "Heap", "Graph", "Map"],
        "answer": "C"
    },
    {
        "id": 16,
        "question": "In Max-heap, Which have large number? [Max-heap এ কোনটি বড়?] (BPSC AP, AME)",
        "options": ["leaf", "Internal Node", "Root", "Outside"],
        "answer": "C"
    },
    {
        "id": 17,
        "question": "Path between two vertices in a graph defined as? [গ্রাফে, দুইটা ভার্টেক্সের মধ্যবর্তি দূরত্বকে কি বলে?]",
        "options": ["The number of edges in the graph", "A sequence of vertices and edges", "The degree of a vertex", "A connected component"],
        "answer": "B"
    },
    {
        "id": 18,
        "question": "Path exists between every pair of vertices, called-? [যদি গ্রাফের প্রতিটি জোড়া ভার্টেক্সের মধ্যে একটি path থাকে, তবে সেই গ্রাফকে বলা হয়...?]",
        "options": ["Disconnected Graph", "Directed Graph", "Complete Graph", "Connected Graph"],
        "answer": "D"
    },
    {
        "id": 19,
        "question": "What is a graph where the edges have a specific direction called? [যে গ্রাফের edges গুলোতে একটি নির্দিষ্ট direction থাকে, তাকে বলা হয়...?]",
        "options": ["Undirected Graph", "Simple Graph", "Directed Graph", "Weighted Graph"],
        "answer": "C"
    },
    {
        "id": 20,
        "question": "Algorithm used to find the shortest path from a single source vertex to all other vertices in a weighted graph? [একটি weighted graph একটি নির্দিষ্ট সোর্স ভার্টেক্স থেকে অন্যান্য সমস্ত ভার্টেক্সের মধ্যে সর্বনিম্ন পথের দৈর্ঘ্য খুঁজে বের করে কোন অ্যালগরিদম ?]",
        "options": ["Breadth-First Search (BFS)", "Depth-First Search (DFS)", "Dijkstra's Algorithm", "Prim's Algorithm"],
        "answer": "C"
    },
    {
        "id": 21,
        "question": "Which of the following is an example of a graph traversal algorithm? [নিচের কোনটি গ্রাফ ট্রাভার্সালের জন্য ব্যবহার করা হয়]",
        "options": ["Kruskal's Algorithm", "Dijkstra's Algorithm", "Topological Sort", "Breadth-First Search"],
        "answer": "D"
    },
    {
        "id": 22,
        "question": "What is a graph with no cycles called? [সাইকেল ছাড়া গ্রাফকে কি বলে?]",
        "options": ["Tree", "Connected Graph", "Complete Graph", "Disconnected Graph"],
        "answer": "A"
    },
    {
        "id": 23,
        "question": "What is the number of edges connected to a vertex called? [একটি Vertex সাথে সংযুক্ত Edges সংখ্যাকে তার ... বলা হয়।]",
        "options": ["Path", "Degree", "Cycle", "Weight"],
        "answer": "B"
    },
    {
        "id": 24,
        "question": "Which algorithm is used to find a Minimum Spanning Tree (MST)? [নিচের কোন অ্যালগরিদম মিনিমাম স্প্যানিং ট্রি ব্যবহার করা হয়?]",
        "options": ["Dijkstra's Algorithm", "Bellman-Ford Algorithm", "Kruskal's Algorithm", "Floyd-Warshall Algorithm"],
        "answer": "C"
    },
    {
        "id": 25,
        "question": "What is a graph called where the edges have numerical values? [যে গ্রাফের Edges সংখ্যাসূচক মান দেওয়া থাকে, তাকে ......বলা হয়।]",
        "options": ["Directed Graph", "Undirected Graph", "Weighted Graph", "Simple Graph"],
        "answer": "C"
    },
    {
        "id": 26,
        "question": "Which sorting technique not compare among element numbers? [কোন Sorting কৌশলটি Elements গুলোর মধ্যে তুলনা করে না?]",
        "options": ["Bubble Sort", "Selection Sort", "Quick Sort", "Radix Sort"],
        "answer": "D"
    },
    {
        "id": 27,
        "question": "Time complexity of Selection sort ? [Selection Sort'র টাইম কমপ্লেক্সিটি কত?]",
        "options": ["Ω(N log n)", "O(N²)", "Ω(N)", "θ(N log N)"],
        "answer": "B"
    },
    {
        "id": 28,
        "question": "Which sorting technique is better?[কোন সর্টিং টেকনিকটি সবচেয়ে ভালো?] (BPSC AP)",
        "options": ["Bubble Sort", "Selection Sort", "Quick Sort", "Merge Sort"],
        "answer": "C"
    },
    {
        "id": 29,
        "question": "What is the time complexity of the binary search algorithm? [বাইনারি সার্চ অ্যালগরিদমের টাইম কমপ্লেক্সিটি কত?] Bank, BPSC AME",
        "options": ["O(N)", "O(N²)", "O(N LOG N)", "O(LOG N)"],
        "answer": "D"
    },
    {
        "id": 30,
        "question": "What is the time complexity of the Buble sort? [Bubble sort এর time complexity কত?] (Bank)",
        "options": ["O(N)", "O(N²)", "O(N LOG N)", "O(LOG N)"],
        "answer": "B"
    },
    {
        "id": 31,
        "question": "What is the main purpose of a hash function? [Hash Function এর প্রধান উদ্দেশ্য কী?]",
        "options": ["To sort data.", "To encrypt data.", "To map a key to an index.", "To compress data."],
        "answer": "C"
    },
    {
        "id": 32,
        "question": "Which data structure is used to build the code tree in the Huffman Algorithm? [Huffman Algorithm e code tree তৈরি করতে কোন ডেটা কাঠামো ব্যবহার করা হয়?]",
        "options": ["A linked list.", "A stack.", "A binary heap", "An array."],
        "answer": "C"
    }
]

out_dir = "JSON Data/BPSC ICT Wizard"
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, "7. Data Structure and Algorithm.json")

with open(out_file, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Saved {len(questions)} MCQs to {out_file}")
