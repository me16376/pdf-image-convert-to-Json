# -*- coding: utf-8 -*-
import os
import sys

questions = [
    {
        "id": 1398,
        "question": "Which of the following words is not related to laughing? [PWD-2015]",
        "options": {
            "a": "stinking",
            "b": "smiling",
            "c": "giggle",
            "d": "chuckle"
        },
        "answer": "ক",
        "explanation": "Laughing, giggle, smiling, chuckle অর্থ হাসি, হাস্যা, হাসা এবং Stinking অর্থ কান্না।"
    },
    {
        "id": 1399,
        "question": "\"Much Ado About Nothing\" is written by– [PWD-2015]",
        "options": {
            "a": "Jane Austene",
            "b": "Charles Dickens",
            "c": "William Shakespeare",
            "d": "Virgina Woolf"
        },
        "answer": "গ",
        "explanation": "\"Much Ado About Nothing\" drama টির লেখক William Shakespeare। তার অন্যান্য নাটকগুলোর মধ্যে Hamlet, Macbeth, Othello, The Merchant of Venice উল্লেখযোগ্য।"
    },
    {
        "id": 1400,
        "question": "She was a beauty in her youth. Here the underlined word is a/an [PWD-15]",
        "options": {
            "a": "adjective",
            "b": "noun",
            "c": "verb",
            "d": "adverb"
        },
        "answer": "খ",
        "explanation": "Beauty শব্দটি noun, যার অর্থ সৌন্দর্য। এর adjective form Beautiful এবং verb Beautify."
    },
    {
        "id": 1401,
        "question": "'Run into debt' is– [PWD-2015]",
        "options": {
            "a": "phrase",
            "b": "idiom",
            "c": "verbal noun",
            "d": "adverb clause"
        },
        "answer": "খ",
        "explanation": "Run into debt একটি idiom, যার অর্থ ঋণে পর্যবসিত হওয়া বা ঋণে জর্জরিত হওয়া।"
    },
    {
        "id": 1402,
        "question": "Choose the correct tag \"Let me do the work\"–? [PWD-2015]",
        "options": {
            "a": "shall we",
            "b": "is n't it",
            "c": "will you",
            "d": "shon't it"
        },
        "answer": "গ",
        "explanation": "Tag question-এ Let me থাকলে will you? হয়।"
    },
    {
        "id": 1403,
        "question": "The thief broke — the house. [PWD-2015]",
        "options": {
            "a": "at",
            "b": "up",
            "c": "on",
            "d": "into"
        },
        "answer": "ঘ",
        "explanation": "\"Broke into\" appropriate preposition টির অর্থ ভেঙে ফেলা।"
    },
    {
        "id": 1404,
        "question": "Choose the word correctly spelt—. [PWD-2015]",
        "options": {
            "a": "soverinty",
            "b": "soverignty",
            "c": "sovereignty",
            "d": "sovereiginity"
        },
        "answer": "গ",
        "explanation": "Sovereignty সঠিক বানান, যার অর্থ সার্বভৌমত্ব।"
    },
    {
        "id": 1405,
        "question": "I had a talk with him. Here 'talk' is a— [PWD-2015]",
        "options": {
            "a": "verb",
            "b": "noun",
            "c": "pronoun",
            "d": "adverb"
        },
        "answer": "খ",
        "explanation": "Article-এর পর noun হয় এবং Sentence এর Object হিসেবে noun হয় তাই এখানে talk হলো noun।"
    },
    {
        "id": 1406,
        "question": "Which sentence is correct? [R&H-2012]",
        "options": {
            "a": "I lodged a complaint.",
            "b": "I made a complain.",
            "c": "I lodged a complained.",
            "d": "Do not complaint any more."
        },
        "answer": "ক",
        "explanation": "Lodge অর্থ দায়ের করা। প্রথম বাক্যটি দ্বারা অভিযোগ দায়ের করা বুঝিয়েছে।"
    },
    {
        "id": 1407,
        "question": "'Pilferage' is a soft word for— [R&H-2012]",
        "options": {
            "a": "stealing",
            "b": "piller",
            "c": "pilgrimage",
            "d": "piled up"
        },
        "answer": "ক",
        "explanation": "Pilferage অর্থ চুরি। অনুরূপ stealing অর্থ চুরি।"
    },
    {
        "id": 1408,
        "question": "I called for his explanation. Here call for means : [R&H-2012]",
        "options": {
            "a": "demand",
            "b": "want",
            "c": "expect",
            "d": "hope"
        },
        "answer": "খ",
        "explanation": "Call for – অর্থ দাবি করা, want – অর্থ চাওয়া। 'call for' এর synonym হলো 'want'।"
    },
    {
        "id": 1409,
        "question": "The word 'orphanage' is– [R&H-2012]",
        "options": {
            "a": "a verb",
            "b": "an adjective",
            "c": "a noun",
            "d": "an adverb"
        },
        "answer": "গ",
        "explanation": "Orphanage অর্থ এতিমখানা, যা একটি Noun।"
    },
    {
        "id": 1410,
        "question": "'Cute' means— [R&H-2012]",
        "options": {
            "a": "sharp-witted",
            "b": "accurate",
            "c": "flute",
            "d": "to cut"
        },
        "answer": "ক",
        "explanation": "Cute অর্থ চতুর, আকর্ষণীয়। Sharp witted অর্থ তীক্ষ্ণ বুদ্ধি সম্পন্ন।"
    },
    {
        "id": 1411,
        "question": "What is the noun form of 'stupid'? [R&H-2012]",
        "options": {
            "a": "stupidity",
            "b": "idiot",
            "c": "stupendous",
            "d": "stupefy"
        },
        "answer": "ক",
        "explanation": "Stupid একটি adjective, যার noun হলো stupidity। এর অর্থ অজ্ঞতা।"
    },
    {
        "id": 1412,
        "question": "The word 'genocide' is– [R&H-2012]",
        "options": {
            "a": "a verb",
            "b": "a preposition",
            "c": "a noun",
            "d": "an adjective"
        },
        "answer": "গ",
        "explanation": "Genocide অর্থ গণহত্যা, যা একটি Noun।"
    },
    {
        "id": 1413,
        "question": "The interrogative form of the sentence \"He is a great scholar\" is– [R&H-2012]",
        "options": {
            "a": "Is he a great scholar?",
            "b": "Is he not a great scholar?",
            "c": "Is he a big scholar?",
            "d": "Is not he a great scholar?"
        },
        "answer": "খ",
        "explanation": "Option (খ) সঠিক উত্তর। Pronoun subject হিসেবে থাকলে [Assertive বাক্যকে Interrogative করার Structure : Auxiliary verb + subject + not + Principal verb (যদি থাকে) + extension + ?"
    },
    {
        "id": 1414,
        "question": "'A red letter day' means– [R&H-2012]",
        "options": {
            "a": "A red day",
            "b": "A historical day",
            "c": "A memorable day",
            "d": "A day of joy"
        },
        "answer": "গ",
        "explanation": "A red letter day একটি phrase, যার অর্থ স্মরণীয় দিন। A memorable day- অর্থ স্মরণীয় দিন।"
    },
    {
        "id": 1415,
        "question": "“Learn the poem —— heart.” [R&H-2012]",
        "options": {
            "a": "by",
            "b": "with",
            "c": "withing",
            "d": "of"
        },
        "answer": "ক",
        "explanation": "মন দিয়ে পড়া বা মুখস্থ করা অর্থে learn + by + heart বসে।"
    },
    {
        "id": 1416,
        "question": "'At a stretch' means : [R&H-2012]",
        "options": {
            "a": "irregularly",
            "b": "without break",
            "c": "decaying",
            "d": "long way"
        },
        "answer": "খ",
        "explanation": "At a stretch অর্থ একটানা, বিরতিহীন। without break- বিরতিহীন।"
    },
    {
        "id": 1417,
        "question": "Which word is in Masculine gender? [R&H-2012]",
        "options": {
            "a": "Cow",
            "b": "Bitch",
            "c": "Nun",
            "d": "Ox"
        },
        "answer": "ঘ",
        "explanation": "Ox হলো- Masculine, যার Feminine হলো- Cow।"
    },
    {
        "id": 1418,
        "question": "Which word is in Feminine gender? [R&H-2012]",
        "options": {
            "a": "Nun",
            "b": "Firar",
            "c": "Hart",
            "d": "Colt"
        },
        "answer": "ক",
        "explanation": "Nun একটি Feminine gender. এর Masculine Monk. যার অর্থ সন্ন্যাসিনী।"
    }
]
