# -*- coding: utf-8 -*-
import os
import sys

questions = [
    {
        "id": 1456,
        "question": "Which one is noun? [R&H-2010]",
        "options": {
            "a": "Cute",
            "b": "Acute",
            "c": "Flute",
            "d": "Mute"
        },
        "answer": "গ",
        "explanation": "Flute হচ্ছে Noun, যার অর্থ বাঁশি। Cute- সুন্দর (Adjective), Acute- তীব্র (Adjective), Mute- নীরব (বোবা)।"
    },
    {
        "id": 1457,
        "question": "Fill in the gap choosing appropriate prepositions out of four alternatives : \"I am inclined --- stick -- it. [R&H-2010]",
        "options": {
            "a": "to/to",
            "b": "to/for",
            "c": "for/against",
            "d": "at/to"
        },
        "answer": "ক",
        "explanation": "Inclined-এর পরে To এবং stick + to বসে।"
    },
    {
        "id": 1458,
        "question": "What is the plural of 'spectrum'? [R&H-2010]",
        "options": {
            "a": "Spectrums",
            "b": "Spectra",
            "c": "Species",
            "d": "Image"
        },
        "answer": "খ",
        "explanation": "Spectrum-এর plural spectra। কোনো শব্দের শেষে um থাকলে তার পরিবর্তে ‘a’ বসে। যেমন Medium-এর plural Media."
    },
    {
        "id": 1459,
        "question": "'By fits and starts' means– [R&H-2010]",
        "options": {
            "a": "irregularly",
            "b": "carefully",
            "c": "regularly",
            "d": "attentively"
        },
        "answer": "ক",
        "explanation": "by fits and starts একটি phrase, যার অর্থ অনিয়মিতভাবে, Irregularly- অনিয়মিতভাবে।"
    },
    {
        "id": 1460,
        "question": "'Penultimate' means– [R&H-2010]",
        "options": {
            "a": "final",
            "b": "ultimate",
            "c": "last but one",
            "d": "penalty"
        },
        "answer": "গ",
        "explanation": "Penultimate অর্থ শেষের আগেরটা, last but one অর্থও শেষের আগেরটা।"
    },
    {
        "id": 1461,
        "question": "What is the masculine gender of 'Mare'? [R&H-2010]",
        "options": {
            "a": "Mermaid",
            "b": "Stallion",
            "c": "Dog",
            "d": "Boar"
        },
        "answer": "খ",
        "explanation": "Mare- ঘোটকী আর stallion- ঘোটক। Mare-এর Masculine form stallion."
    },
    {
        "id": 1462,
        "question": "The word \"Lunar\" is related to – [R&H-2010]",
        "options": {
            "a": "sun",
            "b": "light",
            "c": "moon",
            "d": "earth"
        },
        "answer": "গ",
        "explanation": "lunar চন্দ্রসংক্রান্ত, যেটি Moon-এর সাথে সম্পর্কিত।"
    },
    {
        "id": 1463,
        "question": "The meaning of the word 'comprehension' is– [R&H-2010]",
        "options": {
            "a": "application",
            "b": "apprehension",
            "c": "compounding",
            "d": "understanding"
        },
        "answer": "ঘ",
        "explanation": "Comprehension অর্থ উপলব্ধি। Understanding- বুঝতে পারা। Apprehension- চেতনা, প্রতীক্ষা।"
    },
    {
        "id": 1464,
        "question": "'Virtual' means– [R&H-2010]",
        "options": {
            "a": "virtuous",
            "b": "being in fact",
            "c": "verily",
            "d": "vertical"
        },
        "answer": "খ",
        "explanation": "Virtual Means being in fact not completely fact."
    },
    {
        "id": 1465,
        "question": "Fill in the gap: \"Frustration results--- violence\" [R&H-2010]",
        "options": {
            "a": "at",
            "b": "in",
            "c": "of",
            "d": "with"
        },
        "answer": "খ",
        "explanation": "Result in অর্থ পর্যবসিত হওয়া বা কার্যে পরিণত হওয়া।"
    },
    {
        "id": 1466,
        "question": "Which one is reptile? [R&H-2010]",
        "options": {
            "a": "Colt",
            "b": "Anaconda",
            "c": "Vixen",
            "d": "Boar"
        },
        "answer": "খ",
        "explanation": "Anaconda is a reptile. Several examples of reptiles are– lizards, tuatara, snakes etc. Reptile-সরীসৃপ।"
    },
    {
        "id": 1467,
        "question": "Which of the following four alternatives is not a tree? [R&H-2010]",
        "options": {
            "a": "Pagoda",
            "b": "Cedar",
            "c": "Banyan",
            "d": "Birch"
        },
        "answer": "ক",
        "explanation": "Pagoda is not tree. It is an Asian religious building especially a multi story tower erected as a Buddhist temple."
    },
    {
        "id": 1468,
        "question": "Antonym of the word 'meticulous' is– [R&H-2010]",
        "options": {
            "a": "careless",
            "b": "meritorious",
            "c": "ordinary",
            "d": "careful"
        },
        "answer": "ক",
        "explanation": "Meticulous অর্থ অতি সতর্ক, Careless- উদাসীন, Ordinary- সাধারণ, Careful- সতর্ক।"
    },
    {
        "id": 1469,
        "question": "The word 'Contemporary' means– [R&H-2010]",
        "options": {
            "a": "Temporary",
            "b": "Belonging to the same time",
            "c": "last",
            "d": "future"
        },
        "answer": "খ",
        "explanation": "Contemporary অর্থ সমসাময়িক, Temporary- ক্ষণস্থায়ী, belonging to the same time- একই সময়ের, last- শেষ, future- ভবিষ্যৎ।"
    },
    {
        "id": 1470,
        "question": "'Heptagon' means– [R&H-2010]",
        "options": {
            "a": "five sides",
            "b": "triangle",
            "c": "seven sides",
            "d": "straight"
        },
        "answer": "গ",
        "explanation": "Heptagon- যেটাতে ৭টি তল থাকে। pentagon-এ ৫টি Side থাকে।"
    },
    {
        "id": 1471,
        "question": "Which one give the meaning of 'out break'? [R&H-2010]",
        "options": {
            "a": "Break out",
            "b": "Break into",
            "c": "Break up",
            "d": "Break down"
        },
        "answer": "ক",
        "explanation": "Out break অর্থ শুরু হওয়া, break out- আরম্ভ হওয়া, Break into- ভাঙা।"
    },
    {
        "id": 1472,
        "question": "'Notation' has relevance to – [R&H-10]",
        "options": {
            "a": "Legal affairs",
            "b": "music",
            "c": "sports",
            "d": "insurance"
        },
        "answer": "খ",
        "explanation": "Notation অর্থ স্বরলিপি, যা সংগীতের সাথে সম্পর্কিত।"
    },
    {
        "id": 1473,
        "question": "Adjective of the word 'blood' is–. [R&H-06]",
        "options": {
            "a": "blood",
            "b": "bloody",
            "c": "bloodshed",
            "d": "bleeding"
        },
        "answer": "খ",
        "explanation": "Blood একটি Noun। এর Adjective form Bloody, যার অর্থ রক্তাক্ত।"
    },
    {
        "id": 1474,
        "question": "Which is the noun of the word 'enter'? [R&H-2006]",
        "options": {
            "a": "Entry",
            "b": "Entrance",
            "c": "Enterity",
            "d": "Enterance"
        },
        "answer": "খ",
        "explanation": "Enter-এর Noun form Entrance, যার অর্থ প্রবেশ।"
    },
    {
        "id": 1475,
        "question": "'Temporal' means–. [R&H-2006]",
        "options": {
            "a": "Temporary",
            "b": "Tempting",
            "c": "Worldly",
            "d": "Religious"
        },
        "answer": "গ",
        "explanation": "Temporal অর্থ পার্থিব, বিষয়ী। Worldly- পার্থিব। Tempting- প্রলুব্ধকর।"
    },
    {
        "id": 1476,
        "question": "Choose the correct sentence. [R&H-2006]",
        "options": {
            "a": "Give me five dozens pencils.",
            "b": "Give me five dozen pencils.",
            "c": "Give me five dozens pencil.",
            "d": "Give me five dozen pencil."
        },
        "answer": "খ",
        "explanation": "dozen কখনো Plural হয় না। এদের পূর্বে সংখ্যা বসে পরবর্তী শব্দটি plural হয়। তাই dozen-এর পূর্বে five বসে পরে pencils বসেছে।"
    }
]
