# -*- coding: utf-8 -*-
import os
import sys

questions = [
    {
        "id": 1438,
        "question": "'The programme was telecast live'. What parts of speech is 'live'? [PWD-2011]",
        "options": {
            "a": "verb",
            "b": "adverb",
            "c": "abstract",
            "d": "noun"
        },
        "answer": "খ",
        "explanation": "Verb-কে modify করে Adverb। এখানে live, telecast (সম্প্রচার)-কে modify করে, তাই live একটি Adverb।"
    },
    {
        "id": 1439,
        "question": "The word ‘dilly-dally’ means– [PWD-11]",
        "options": {
            "a": "dilute",
            "b": "wait",
            "c": "waste time",
            "d": "repeat"
        },
        "answer": "গ",
        "explanation": "Dilly-dally একটি phrase, যার অর্থ ঘুরে বেড়িয়ে সময় নষ্ট করা। Waste time অর্থ সময় নষ্ট করা।"
    },
    {
        "id": 1440,
        "question": "What parts of speech is ‘honesty’? [PWD-2011]",
        "options": {
            "a": "Proper",
            "b": "Common",
            "c": "Abstract",
            "d": "Material"
        },
        "answer": "গ",
        "explanation": "Noun পাঁচ প্রকার। Abstract Noun বলতে কোনো বস্তু বা ব্যক্তির গুণ, দোষ ইত্যাদির নাম বুঝায়। যেমন- Honesty, Childhood, Justice, Joy etc."
    },
    {
        "id": 1441,
        "question": "What parts of speech is 'Beauty'? [PWD-2011]",
        "options": {
            "a": "Adjective",
            "b": "Noun",
            "c": "Pronoun",
            "d": "Verb"
        },
        "answer": "খ",
        "explanation": "Beauty একটি Noun, যার অর্থ সৌন্দর্য-এর verb হলো Beautify।"
    },
    {
        "id": 1442,
        "question": "Who is the greatest dramatist of all times? [PWD-2011]",
        "options": {
            "a": "G.B. Shaw",
            "b": "William Shakespeare",
            "c": "William Wordsworth",
            "d": "Jonathan Swift"
        },
        "answer": "খ",
        "explanation": "Elizabethan period-এর Dramatist William Shakespeare সর্বশ্রেষ্ঠ নাট্যকার। তিনি ১৫৬৪ সালে জন্মগ্রহণ করেন। তার নাটকগুলো Othello, Macbeth, Hamlet, As You Like It, King Lear."
    },
    {
        "id": 1443,
        "question": "The antonym of 'Retreat' is– [PWD-2011]",
        "options": {
            "a": "Return",
            "b": "Advance",
            "c": "Treat",
            "d": "Go"
        },
        "answer": "খ",
        "explanation": "Retreat অর্থ পশ্চাদপসরণ। Return মানে প্রত্যাবর্তন। Advance মানে আগানো। treat মানে আচরণ করা। Go মানে যাওয়া।"
    },
    {
        "id": 1444,
        "question": "The synonym of 'Noble' is– [PWD-2011]",
        "options": {
            "a": "Courteous",
            "b": "Big",
            "c": "Virtuous",
            "d": "Of great quality and character"
        },
        "answer": "ঘ",
        "explanation": "Noble অর্থ অভিজাত, উন্নত। Of great quality and character অর্থ মহৎ চরিত্র ও গুণ।"
    },
    {
        "id": 1445,
        "question": "\"Dr Faustus\" was written by– [PWD-2011]",
        "options": {
            "a": "Ben Jonson",
            "b": "W. Shakespeare",
            "c": "Christopher Marlowe",
            "d": "John Webster"
        },
        "answer": "গ",
        "explanation": "Elizabethan period-এর writer Christopher Marlowe \"Dr Faustus\" লেখেন। তার রচিত গ্রন্থগুলো Hero and Leander, The Passionate Shepherd to His Love।"
    },
    {
        "id": 1446,
        "question": "Which parts of speech is the word \"Obstinacy\"? [PWD-2011]",
        "options": {
            "a": "Pronoun",
            "b": "Adjective",
            "c": "Noun",
            "d": "Adverb"
        },
        "answer": "গ",
        "explanation": "Obstinacy একটি Noun, যার অর্থ একগুঁয়েমি, জেদ।"
    },
    {
        "id": 1447,
        "question": "The correct translation of “দূর্ঘটনাটি কখন ঘটেছিল?” is– [PWD-2011]",
        "options": {
            "a": "When was the accident occurred?",
            "b": "When did the accident occur?",
            "c": "What time has the accident occurred?",
            "d": "When the accident occurred?"
        },
        "answer": "খ",
        "explanation": "‘দূর্ঘটনাটি কখন ঘটেছিল?’ এটি একটি Past indefinite tense। বাক্যের did থাকলে verb এর present form হয়।"
    },
    {
        "id": 1448,
        "question": "'She takes after her mother'. Here \"takes after\" is– [PWD-2011]",
        "options": {
            "a": "verbal idiom",
            "b": "phrasal verb",
            "c": "regular verb",
            "d": "intransitive verb"
        },
        "answer": "খ",
        "explanation": "takes after একটি phrase, যার অর্থ সদৃশ হওয়া, অনুরূপ হওয়া। তাই এ verbটি phrasal verb।"
    },
    {
        "id": 1449,
        "question": "You are looking smart — this dress. Choose the right preposition for the blank. [PWD-2011]",
        "options": {
            "a": "on",
            "b": "in",
            "c": "for",
            "d": "with"
        },
        "answer": "খ",
        "explanation": "উপরের sentence-এ in preposition উপযুক্ত। look in- মানে দেখা।"
    },
    {
        "id": 1450,
        "question": "Nobody likes a liar. The affirmative form of this sentence is– [PWD-2011]",
        "options": {
            "a": "Everybody dislikes lying.",
            "b": "All people dislike a liar.",
            "c": "Everybody hates a liar.",
            "d": "Everybody likes the truth."
        },
        "answer": "গ",
        "explanation": "Everybody, Everyone Subject হিসেবে থাকলে Verbটি Singular হয়। Negative বাক্যে Nobody থাকলে Affirmative এ Everybody হয়।"
    },
    {
        "id": 1451,
        "question": "Oval is an adjective of– [PWD-2011]",
        "options": {
            "a": "over",
            "b": "eye",
            "c": "egg",
            "d": "lip"
        },
        "answer": "গ",
        "explanation": "egg-এর Adjective হলো Oval, যার অর্থ ডিম্বাকার।"
    },
    {
        "id": 1452,
        "question": "Which word is different from the other three? [PWD-2011]",
        "options": {
            "a": "Media",
            "b": "War",
            "c": "Newspaper",
            "d": "Radio"
        },
        "answer": "খ",
        "explanation": "Media, Radio, Newspaper এগুলো গণমাধ্যম। অন্যদিকে War মানে যুদ্ধ।"
    },
    {
        "id": 1453,
        "question": "'Bibliography 'means– [PWD-2011]",
        "options": {
            "a": "History of the Bible",
            "b": "History of Books",
            "c": "Collection of Books",
            "d": "Worshipper of Books"
        },
        "answer": "গ",
        "explanation": "Bibliography অর্থ গ্রন্থপঞ্জি, Collection of books মানে বইয়ের সংকলন।"
    },
    {
        "id": 1454,
        "question": "'Capital punishment' means– [PWD-2011]",
        "options": {
            "a": "Heavy punishment",
            "b": "Confiscation of capital",
            "c": "Death penalty",
            "d": "Life imprisonment"
        },
        "answer": "গ",
        "explanation": "Capital punishment অর্থ মৃত্যুদণ্ড। Death penalty অর্থ মৃত্যুদণ্ড।"
    },
    {
        "id": 1455,
        "question": "This is the fashion of the day. Here fashion is a- [R&H-2011]",
        "options": {
            "a": "noun",
            "b": "pronoun",
            "c": "verb",
            "d": "adverb"
        },
        "answer": "ক",
        "explanation": "কোনো শব্দের পূর্বে Article এবং পরে preposition থাকলে Wordটি Noun হিসেবে ব্যবহৃত হয়।"
    }
]
