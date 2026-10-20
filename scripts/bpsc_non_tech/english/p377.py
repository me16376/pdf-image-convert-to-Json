# -*- coding: utf-8 -*-
import os
import sys

questions = [
    {
        "id": 1345,
        "question": "Choose the correct meaning of the word 'Viable'. [SB-2016]",
        "options": {
            "a": "Capable",
            "b": "Possible",
            "c": "that can be done",
            "d": "that will work"
        },
        "answer": "নোট",
        "explanation": "Viable অর্থ টিকে থাকতে সক্ষম, Capable- সক্ষম, that can be done যা করা যেতে পারে। ক ও গ দুটিই সঠিক।"
    },
    {
        "id": 1346,
        "question": "The correct meaning of 'a man of letter' is-. [SB-2016]",
        "options": {
            "a": "a postman",
            "b": "a scholar",
            "c": "a bad man",
            "d": "a good man"
        },
        "answer": "খ",
        "explanation": "A man of letter একটি Phrase, যার অর্থ বিদ্বান ব্যক্তি; a scholar অর্থ পণ্ডিত ব্যক্তি।"
    },
    {
        "id": 1347,
        "question": "What is the verb of the word 'Ability'? [SB-2016]",
        "options": {
            "a": "Ableness",
            "b": "Able",
            "c": "Ably",
            "d": "Enable"
        },
        "answer": "ঘ",
        "explanation": "Ability একটি Noun form. এর verb হচ্ছে Enable, যার অর্থ সক্ষম করা। Noun-এর পূর্বে [prefix 'en'] যুক্ত verb গঠন করা হয়েছে।"
    },
    {
        "id": 1348,
        "question": "A good entrepreneur starts a business with —— and ——. [SB-2016]",
        "options": {
            "a": "commitment, responsibility",
            "b": "quality, product",
            "c": "courage, energy",
            "d": "none of these"
        },
        "answer": "ক",
        "explanation": "Commitment অর্থ অঙ্গীকার/প্রতিশ্রুতি এবং responsibility অর্থ দায়িত্ব। এ শব্দ দুটিই যথোপযুক্ত শব্দ। একজন ভালো উদ্যোক্তা হবে। হলে প্রতিশ্রুতিবদ্ধ এবং দায়িত্বশীল হতে হয়।"
    },
    {
        "id": 1349,
        "question": "Instead of 'continue' we can say ——. [SB-2016]",
        "options": {
            "a": "carry out",
            "b": "carry off",
            "c": "carry on",
            "d": "carry away"
        },
        "answer": "গ",
        "explanation": "Continue অর্থ চালিয়ে যাওয়া বা চলমান, Carry on- অর্থ চালিয়ে যাওয়া, Carry out- সম্পন্ন করা, Carry off- আহরণ করা।"
    },
    {
        "id": 1350,
        "question": "Good example of a complex sentence is —— [SB-2016]",
        "options": {
            "a": "Tell me the name you bear.",
            "b": "Tell me what is your name.",
            "c": "Tell me what your name.",
            "d": "Tell me what your name is."
        },
        "answer": "ঘ",
        "explanation": "দুটি Sentence-কে What, Which, Who, When দ্বারা যুক্ত করলে Sentence-টি Complex sentence হয়।"
    },
    {
        "id": 1351,
        "question": "“দেরী হওয়ার জন্য আমি তার উপর বিরক্ত ছিলাম”- বাক্যটির ইংরেজি অনুবাদ কোনটি? [BREB-2016]",
        "options": {
            "a": "I was annoyed with him for being late.",
            "b": "I was annoyed open him for being late.",
            "c": "I was annoyed on him for being late.",
            "d": "I was annoyed on him as he was late."
        },
        "answer": "ক",
        "explanation": "“দেরী হওয়ার জন্য তার উপর বিরক্ত ছিলাম” এর সঠিক অনুবাদ হলো : I was annoyed with him/her for being late."
    },
    {
        "id": 1352,
        "question": "“সে তাহার দোষ অস্বীকার করিল”-বাক্যটির ইংরেজি অনুবাদ কোনটি? [BREB-2016]",
        "options": {
            "a": "He refused fault.",
            "b": "He denied his guilt.",
            "c": "He refused his guilt.",
            "d": "He denied his fault."
        },
        "answer": "ঘ",
        "explanation": "‘সে তাহার দোষ অস্বীকার করিল’। এর সঠিক অনুবাদ হলো : He denied his fault."
    },
    {
        "id": 1353,
        "question": "Which is the singular form of “Data”? [BREB-2016]",
        "options": {
            "a": "Datam",
            "b": "Datum",
            "c": "Datas",
            "d": "Datee"
        },
        "answer": "খ",
        "explanation": "Singular noun-এর শেষে um থাকলে plural করার সময় um উঠিয়ে a বসানো হয়। তাই উত্তর Datum হবে।"
    },
    {
        "id": 1354,
        "question": "What is the feminine form of “Author”? [BREB-2016]",
        "options": {
            "a": "Authorss",
            "b": "Authores",
            "c": "Authories",
            "d": "Authoress"
        },
        "answer": "ঘ",
        "explanation": "শব্দের শেষে or থাকলে ess যোগ করে Feminine করা হয়। তাই সঠিক উত্তর : Authoress."
    },
    {
        "id": 1355,
        "question": "What is the verb form of the noun “Power”? [BREB-2016]",
        "options": {
            "a": "Powering",
            "b": "Powerd",
            "c": "Empower",
            "d": "Powered"
        },
        "answer": "গ",
        "explanation": "কিছু noun এর আগে prefix যোগ করে verb করা হয়। এখানে Power এর আগে 'em' prefix যোগে Empower হবে।"
    },
    {
        "id": 1356,
        "question": "A 'pilgrim' is a person who undertakes a journey to a—. [R&H-2006; HED-2015]",
        "options": {
            "a": "mosque",
            "b": "new country",
            "c": "holy place",
            "d": "bazar"
        },
        "answer": "গ",
        "explanation": "Pilgrim অর্থ তীর্থযাত্রী, যে ধর্মীয় উদ্দেশ্যে Sacred place-এ গমন করে। Holy place অর্থ পবিত্র স্থান।"
    },
    {
        "id": 1357,
        "question": "What is the noun of the word \"Waste\"? [BREB-2015]",
        "options": {
            "a": "waste",
            "b": "wasting",
            "c": "wastage",
            "d": "wasteful"
        },
        "answer": "গ",
        "explanation": "Waste একটি Verb, যার অর্থ অপচয় করা। verb এর শেষে suffix 'age' যুক্ত করে verb গঠন করা হয়েছে। এক্ষেত্রে waste-এর শেষে 'e' উঠে গিয়ে 'age' যুক্ত হবে।"
    },
    {
        "id": 1358,
        "question": "What is the antonym of the word 'Honorary'? [BREB-2015]",
        "options": {
            "a": "literary",
            "b": "honorable",
            "c": "salaried",
            "d": "official"
        },
        "answer": "গ",
        "explanation": "Honorary অর্থ অবৈতনিক। যার Antonym salaried, অর্থাৎ বেতনিক।"
    },
    {
        "id": 1359,
        "question": "Choose the correct meaning: He raised his eye brow at my exploration. [BREB-2015]",
        "options": {
            "a": "show surprise or disapproval",
            "b": "show agreement",
            "c": "show happiness",
            "d": "show indifference"
        },
        "answer": "ক",
        "explanation": "Raise one's eye brow অর্থ অবাক হওয়া বা অনাগ্রহী হওয়া।"
    },
    {
        "id": 1360,
        "question": "Which is the adjective form of 'home'? [HED-15]",
        "options": {
            "a": "home maker",
            "b": "homely",
            "c": "homeland",
            "d": "homage"
        },
        "answer": "খ",
        "explanation": "Noun এর সাথে 'ly' suffix যোগ করলে Adjective গঠন করা হয়। যেমন- Homely, Housely।"
    },
    {
        "id": 1361,
        "question": "He -------- out just now. [HED-2015]",
        "options": {
            "a": "went",
            "b": "goes",
            "c": "has gone",
            "d": "went away"
        },
        "answer": "গ",
        "explanation": "কোনো Sentence-এ Just now, yet, Just থাকলে Sentence-টি Present perfect tense হয়।"
    }
]
