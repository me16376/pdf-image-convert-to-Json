# -*- coding: utf-8 -*-
import os
import sys

questions = [
    {
        "id": 1379,
        "question": "Choose the correctly spelt word. [HED-2015]",
        "options": {
            "a": "Leisure",
            "b": "Liesure",
            "c": "Leasure",
            "d": "Lesiure"
        },
        "answer": "ক",
        "explanation": "Leisure বানানটি সঠিক। Leisure এর বাংলা অর্থ অবসর। অন্যগুলোর বানান সঠিক নয়।"
    },
    {
        "id": 1380,
        "question": "Your conduct admits —— no excuse. [HED-2015]",
        "options": {
            "a": "to",
            "b": "for",
            "c": "of",
            "d": "at"
        },
        "answer": "গ",
        "explanation": "২৯তম BCS-এর ৩নং প্রশ্নের ব্যাখ্যা দেখুন।"
    },
    {
        "id": 1381,
        "question": "Amicable means —— [HED-2015]",
        "options": {
            "a": "interesting",
            "b": "loving",
            "c": "affectionate",
            "d": "friendly"
        },
        "answer": "ঘ",
        "explanation": "Amicable- বন্ধুত্বপূর্ণ, interesting- মজাদার, friendly- বন্ধুত্বপূর্ণ, affectionate- আন্তরিক।"
    },
    {
        "id": 1382,
        "question": "\"Crocodile tears\" means– [HED-2015]",
        "options": {
            "a": "tears of a crocodile",
            "b": "deceptive cry",
            "c": "tears of any animal",
            "d": "tears of an unlucky person"
        },
        "answer": "খ",
        "explanation": "Crocodile tears একটি Phrase, যার অর্থ মায়াকান্না। deceptive cry- ছলনাময়ী কান্না বা মায়াকান্না।"
    },
    {
        "id": 1383,
        "question": "Choose the direct speech of the sentence : She told us to hurry up. [PWD-2015]",
        "options": {
            "a": "She said, \"Do hurry up\".",
            "b": "She said to us, \"Hurry up\".",
            "c": "She told, \"hurry up\".",
            "d": "She said us, \"hurry up\"."
        },
        "answer": "খ",
        "explanation": "Indirect speech-এ told থাকলে direct speech-এ said to বসে।"
    },
    {
        "id": 1384,
        "question": "The singular form of 'phenomena' is– [PWD-2015]",
        "options": {
            "a": "phenomenna",
            "b": "phenomenon",
            "c": "phenomenone",
            "d": "phenom"
        },
        "answer": "খ",
        "explanation": "Phenomena plural শব্দ। এর singular শব্দ Phenomenon- যার অর্থ হচ্ছে বিস্ময়কর ব্যক্তি/বিষয়/ঘটনা।"
    },
    {
        "id": 1385,
        "question": "'Heart of Darkness' is a novel written by– [PWD-2015]",
        "options": {
            "a": "D.H. Lawrence",
            "b": "E.M. Forster",
            "c": "Conrad",
            "d": "Virgina Woolf"
        },
        "answer": "গ",
        "explanation": "\"Heart of Darkness\" বইটির লেখক Joseph Conrad। তার অন্যান্য গ্রন্থের মধ্যে Lord Jim, The Arrow of God উল্লেখযোগ্য।"
    },
    {
        "id": 1386,
        "question": "Which of the following are semi-modals? [PWD-2015]",
        "options": {
            "a": "can, could",
            "b": "need, dare",
            "c": "will, would",
            "d": "must, should"
        },
        "answer": "খ",
        "explanation": "Semi-modal verb গুলো হলো Need, Dare, Used to ইত্যাদি।"
    },
    {
        "id": 1387,
        "question": "The antonym of the word 'awesome'– [PWD-2015]",
        "options": {
            "a": "grand",
            "b": "daunting",
            "c": "majestic",
            "d": "disguisting"
        },
        "answer": "ঘ",
        "explanation": "awesome অর্থ অসাধারণ। Disguisting অর্থ জঘন্য। Daunting অর্থ কঠিন, ভীত করা। Grand অর্থ মহান।"
    },
    {
        "id": 1388,
        "question": "The phrase 'pass the buck' means– [PWD-2015]",
        "options": {
            "a": "to suffer",
            "b": "to succeed",
            "c": "to complete a task",
            "d": "to pass the blame to someone else"
        },
        "answer": "ঘ",
        "explanation": "Pass the buck অর্থ নিজের দোষ অন্যের ঘাড়ে চাপিয়ে দেয়া। to pass the blame to someone else."
    },
    {
        "id": 1389,
        "question": "Which of the following sentences expresses a request? [PWD-2015]",
        "options": {
            "a": "Would you mind opening the window.",
            "b": "Would that he were here.",
            "c": "Never do this.",
            "d": "Liza and Shuvo are in love."
        },
        "answer": "ক",
        "explanation": "would you mind-এর পর verb এর v + ing হয়।"
    },
    {
        "id": 1390,
        "question": "Fill in the blank: The man died —— overeating. [PWD-2015]",
        "options": {
            "a": "from",
            "b": "for",
            "c": "on",
            "d": "of"
        },
        "answer": "ক",
        "explanation": "Overeating এর জন্য মারা গেলে die from হয়। Disease এর কারণে মারা গেলে die of হয়। দেশের জন্য মারা গেলে Die for হয়।"
    },
    {
        "id": 1391,
        "question": "\"After death the doctor\" is– [PWD-15]",
        "options": {
            "a": "a proverb",
            "b": "a phrase",
            "c": "an idiom",
            "d": "a smile"
        },
        "answer": "খ",
        "explanation": "After death the doctor একটা Phrase, যার অর্থ চোর পালালে বুদ্ধি বাড়ে।"
    },
    {
        "id": 1392,
        "question": "One who is the hater of woman is a– [PWD-2015]",
        "options": {
            "a": "imposter",
            "b": "somnambulist",
            "c": "misogynist",
            "d": "pilgrim"
        },
        "answer": "গ",
        "explanation": "Misogynist অর্থ নারীবিদ্বেষী, স্ত্রীদ্বেষী। Imposter = ছদ্মবেশী, Somnambulist = স্বপ্নচারী, Pilgrim অর্থ তীর্থযাত্রী, ভ্রমণকারী।"
    },
    {
        "id": 1393,
        "question": "Which one of the following is not collective noun? [PWD-2015]",
        "options": {
            "a": "class",
            "b": "audience",
            "c": "peer",
            "d": "public"
        },
        "answer": "গ",
        "explanation": "কোনো জাতি বা দল, গুচ্ছ বুঝাতে Collective noun বা সমষ্টিবাচক বিশেষ্য হয়। যেমন— team, school, audience, class, public ইত্যাদি। ‘peer’ শব্দটি সম্ভ্রান্ত শ্রেণীর ব্যক্তিদের কাউকে (individual) ভাবে বুঝায়। এটি collective noun-এর আওতায় পড়ে না। তাই, অপশন (গ) সঠিক উত্তর।"
    },
    {
        "id": 1394,
        "question": "'He is not himself' means– [PWD-2015]",
        "options": {
            "a": "He does not feel well.",
            "b": "He is a different person.",
            "c": "He is not what he seems to be.",
            "d": "He is not a well-known person."
        },
        "answer": "ক",
        "explanation": "He is not himself অর্থ উদাসীন, না বুঝতে পারা। He does not feel well অর্থ উদাসীন, অনুভবহীন।"
    },
    {
        "id": 1395,
        "question": "'The Daffodils' is a poem written by– [PWD-2015]",
        "options": {
            "a": "Wordsworth Longfellow",
            "b": "William Wordsworth",
            "c": "Alfred Tennyson",
            "d": "Robert Browning"
        },
        "answer": "খ",
        "explanation": "'The Daffodils' কবিতাটির লেখক William Wordsworth এবং 'To Daffodils' লিখেছেন Robert Herrick।"
    },
    {
        "id": 1396,
        "question": "I have– my lunch. [PWD-2015]",
        "options": {
            "a": "have",
            "b": "will",
            "c": "had taken",
            "d": "had"
        },
        "answer": "ঘ",
        "explanation": "অর্থানুসারে Present perfect tense হবে। তাই had হবে।"
    },
    {
        "id": 1397,
        "question": "Which of the following is an incorrect sentence? [PWD-2015]",
        "options": {
            "a": "I have a bad headache.",
            "b": "He has just come here.",
            "c": "Keep to the left.",
            "d": "I took your leave."
        },
        "answer": "ঘ",
        "explanation": "সঠিক বাক্যটি হবে 'I took leave of you'।"
    }
]
