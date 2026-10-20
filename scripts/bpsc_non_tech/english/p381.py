# -*- coding: utf-8 -*-
import os
import sys

questions = [
    {
        "id": 1419,
        "question": "Which is the correct sentence? [R&H-2012]",
        "options": {
            "a": "He spoke to me to wait.",
            "b": "He wished for me to wait.",
            "c": "The boat was drowned.",
            "d": "Two-thirds of it is true."
        },
        "answer": "ঘ",
        "explanation": "ভগ্নাংশের of-যুক্ত পরের subject singular হলে verb singular এবং Subject plural হলে verb plural হবে।"
    },
    {
        "id": 1420,
        "question": "Which one is in singular number? [R&H-2012]",
        "options": {
            "a": "Phenomena",
            "b": "Criterion",
            "c": "Oases",
            "d": "Ultimata"
        },
        "answer": "খ",
        "explanation": "Criterion শব্দটি Singular। শব্দের শেষে on থাকলে তা Singular এবং Criterion শব্দটির Plural হলো criteria."
    },
    {
        "id": 1421,
        "question": "Which one is in plural number? [R&H-2012]",
        "options": {
            "a": "School",
            "b": "Oxen",
            "c": "Leaf",
            "d": "Mathematics"
        },
        "answer": "খ",
        "explanation": "Oxen একটি Plural number. এর Singular form Ox."
    },
    {
        "id": 1422,
        "question": "What is the passive voice of “Who did this?” [R&H-2012]",
        "options": {
            "a": "By whom was this done?",
            "b": "Who has done this?",
            "c": "By whom this has been done?",
            "d": "Whom did this?"
        },
        "answer": "ক",
        "explanation": "Active voice-এ who থাকলে passive-এ By whom বসে। তারপর Tense অনুযায়ী Auxiliary verb + subject + verb-এর Past participle."
    },
    {
        "id": 1423,
        "question": "What is the active voice of “The gate was opened by the peon.” [R&H-2012]",
        "options": {
            "a": "The peon opened the gate.",
            "b": "The peon had opened the gate.",
            "c": "The peon has opened the gate.",
            "d": "The peon opens the gate."
        },
        "answer": "ক",
        "explanation": "Object (passive) + verb (Past form) + sub (passive)."
    },
    {
        "id": 1424,
        "question": "‘De facto’ means– [R&H-2012]",
        "options": {
            "a": "de jure",
            "b": "two friends",
            "c": "in fact",
            "d": "surely"
        },
        "answer": "গ",
        "explanation": "De facto অর্থ কার্যত, বস্তুত। Infact - বস্তুত।"
    },
    {
        "id": 1425,
        "question": "‘Proclaim’ means– [R&H-2012]",
        "options": {
            "a": "pronounce",
            "b": "declare",
            "c": "announce",
            "d": "circulate"
        },
        "answer": "খ",
        "explanation": "Proclaim অর্থ সরকারীভাবে ব্যাপক প্রচার করা। এবং circulate অর্থ চতুর্দিকে ছাড়াইয়া পড়া। সরকারীভাবে কোন ঘোষণা জারি হলে সেটা ব্যাপকভাবে চতুর্দিকে ছড়িয়ে পড়ে।"
    },
    {
        "id": 1426,
        "question": "The word ‘sympathise’ is– [R&H-2012]",
        "options": {
            "a": "an adjective",
            "b": "a verb",
            "c": "a noun",
            "d": "a preposition"
        },
        "answer": "খ",
        "explanation": "Sympathise একটি verb, যার অর্থ সহানুভূতি প্রকাশ করা।"
    },
    {
        "id": 1427,
        "question": "The phrase ‘Tide over’ means : [R&H-2012]",
        "options": {
            "a": "overcome",
            "b": "pass over",
            "c": "cross over",
            "d": "carry over"
        },
        "answer": "ক",
        "explanation": "Proclaim অর্থ করা এবং Declare অর্থ ঘোষণা করা। (Tide over-এর অর্থ overcome)."
    },
    {
        "id": 1428,
        "question": "‘Posterity’ means– [R&H-2012]",
        "options": {
            "a": "later generations",
            "b": "prosperity",
            "c": "present time",
            "d": "past days"
        },
        "answer": "ক",
        "explanation": "Posterity অর্থ পরবর্তী প্রজন্ম/বংশধর, Later generation - পরবর্তী প্রজন্ম।"
    },
    {
        "id": 1429,
        "question": "Which one is ‘present continuous tense’? [R&H-2012]",
        "options": {
            "a": "I read.",
            "b": "I am reading.",
            "c": "I have read.",
            "d": "I had read."
        },
        "answer": "খ",
        "explanation": "Sub + auxiliary verb + principle (verb-ing) + object."
    },
    {
        "id": 1430,
        "question": "Which one is correct? [R&H-2012]",
        "options": {
            "a": "It is quarter past ten.",
            "b": "It is a quarter past ten.",
            "c": "It is 15 plus ten.",
            "d": "It is quarter minutes past ten."
        },
        "answer": "ক",
        "explanation": "quarter এর পূর্বে Article বসে না।"
    },
    {
        "id": 1431,
        "question": "Which word is not a noun? [PWD-2011]",
        "options": {
            "a": "Articulation",
            "b": "Simulation",
            "c": "Defame",
            "d": "Indemnity"
        },
        "answer": "গ",
        "explanation": "Defame একটি verb, যার অর্থ নিন্দা করা, মানহানি করা।"
    },
    {
        "id": 1432,
        "question": "Which sentence is in Imperative mood? [PWD-2011]",
        "options": {
            "a": "He does not smoke.",
            "b": "I must go, come what may.",
            "c": "The earth is round.",
            "d": "May I come in, Sir?"
        },
        "answer": "ঘ",
        "explanation": "যে Sentence দ্বারা অনুরোধ, আদেশ, নিষেধ ইত্যাদি বুঝায়, তাকে Imperative Sentence বলে।"
    },
    {
        "id": 1433,
        "question": "Which word is not an adjective? [PWD-2011]",
        "options": {
            "a": "Solar",
            "b": "Polar",
            "c": "Linear",
            "d": "Hammer"
        },
        "answer": "ঘ",
        "explanation": "Hammer একটি Noun, যার অর্থ হাতুড়ি। অন্যগুলো Adjective।"
    },
    {
        "id": 1434,
        "question": "The synonym of 'identical' is– [PWD-2011]",
        "options": {
            "a": "familiar",
            "b": "recognisable",
            "c": "same",
            "d": "close"
        },
        "answer": "গ",
        "explanation": "Identical অর্থ অভিন্ন/একই, Familiar- পরিচিত, Same- একই।"
    },
    {
        "id": 1435,
        "question": "What does CV stand for? [PWD-2011]",
        "options": {
            "a": "Curriculum Vital",
            "b": "Curriculum Value",
            "c": "Current Value",
            "d": "Curriculum Vitae"
        },
        "answer": "ঘ",
        "explanation": "CV means Curriculum Vitae, যার অর্থ জীবনবৃত্তান্ত।"
    },
    {
        "id": 1436,
        "question": "Alexander Pope's \"An Essay on Man\" is a– [PWD-2011]",
        "options": {
            "a": "novel",
            "b": "treatise",
            "c": "short story",
            "d": "poem"
        },
        "answer": "ঘ",
        "explanation": "Alexander Pope is the greatest English poet. He was also an essayist. The Rape of the Lock, The Dunciad, An Essay on Criticism. The famous poem of Pope is \"An Essay on Man.\""
    },
    {
        "id": 1437,
        "question": "\"Ode to Autumn\" is written by– [PWD-2011]",
        "options": {
            "a": "Shelley",
            "b": "Wordsworth",
            "c": "Keats",
            "d": "Coleridge"
        },
        "answer": "গ",
        "explanation": "Romantic period-এর কবি John Keats. তাকে Poet of beauty বলা হয়। তার কবিতাগুলো An Ode to Autumn, Ode to a Nightingale etc. তিনি যক্ষ্মায় আক্রান্ত হয়ে মারা যান।"
    }
]
