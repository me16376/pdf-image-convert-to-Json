# -*- coding: utf-8 -*-
import os
import sys

questions = [
    {
        "id": 1362,
        "question": "Which is the conjunction here? [HED-2015]",
        "options": {
            "a": "the",
            "b": "up",
            "c": "to",
            "d": "and"
        },
        "answer": "ঘ",
        "explanation": "যে Parts of speech দুটি clause বা phrase-কে যুক্ত করে তাকে conjunction বলে। যেমন- and, or, but ইত্যাদি।"
    },
    {
        "id": 1363,
        "question": "What is the antonym of 'gentle'? [HED-2015]",
        "options": {
            "a": "harsh",
            "b": "modest",
            "c": "clever",
            "d": "rude"
        },
        "answer": "ঘ",
        "explanation": "Gentle-এর অর্থ ভদ্র, বিনয়ী, Harsh- কঠোর, Modest- ভদ্র, Rude- খিটখিটে, Clever- চালাক।"
    },
    {
        "id": 1364,
        "question": "The synonym of 'incredible' is— [HED-2015]",
        "options": {
            "a": "unthinkable",
            "b": "unbelievable",
            "c": "unlikely",
            "d": "unimaginable"
        },
        "answer": "খ",
        "explanation": "Incredible অর্থ অবিশ্বাস্য, unthinkable- অচিন্তনীয়, unbelievable- অবিশ্বাস্য, unimaginable- অকল্পনীয়, unlikely- অসদৃশ।"
    },
    {
        "id": 1365,
        "question": "The expression 'Lingua franca' means— [HED-2015]",
        "options": {
            "a": "The common language",
            "b": "The first language",
            "c": "International language",
            "d": "The French language"
        },
        "answer": "ক",
        "explanation": "Lingua franca একটি Italian word. যার অর্থ Common language অর্থাৎ সর্বসাধারণের ব্যবহারের ভাষা।"
    },
    {
        "id": 1366,
        "question": "If your sister ----, she would come. [HED-2015]",
        "options": {
            "a": "invited",
            "b": "inviting",
            "c": "invites",
            "d": "were invited"
        },
        "answer": "ঘ",
        "explanation": "প্রদত্ত Sentence-টি [second conditional-এর passive form-এ রয়েছে। [Second conditional sentence-এর passive form-এর Structure : If + subject + was/were + verb-এর Past participle form + subject + would/could + verb-এর base form। অথবা, Subject + would/could + verb-এর base form + if + subject + was/were + verb-এর Past participle form."
    },
    {
        "id": 1367,
        "question": "What do you mean by 'in the nick time'? [HED-2015]",
        "options": {
            "a": "in the appropriate time",
            "b": "in the wrong time",
            "c": "before the just time",
            "d": "after the just time"
        },
        "answer": "ক",
        "explanation": "In the nick time একটি Phrase। যার অর্থ যথোপযুক্ত সময় বা in the appropriate time।"
    },
    {
        "id": 1368,
        "question": "Which one is the verb of the word 'real'? [HED-2015]",
        "options": {
            "a": "reality",
            "b": "realize",
            "c": "reliable",
            "d": "really"
        },
        "answer": "খ",
        "explanation": "Real অর্থ বাস্তব, যা একটি Adjective। এর verb হলো Realize, যার অর্থ উপলব্ধি করা।"
    },
    {
        "id": 1369,
        "question": "Bees have compound eyes ------ almost 6,000 tiny lenses. [HED-2015]",
        "options": {
            "a": "made of",
            "b": "made in",
            "c": "made on",
            "d": "made up of"
        },
        "answer": "ঘ",
        "explanation": "Made of অর্থ গঠিত, Make up of অর্থ সংগঠিত করা। মৌমাছির ৬০০০ ক্ষুদ্র ক্ষুদ্র লেন্স নিয়ে তার চোখের উপাদান সুসংগঠিত হয়েছে। তাই Made up of অর্থপূর্ণ।"
    },
    {
        "id": 1370,
        "question": "Beethoven is considered one of the greatest personalities in the field of --------- [HED-2015]",
        "options": {
            "a": "technology",
            "b": "music",
            "c": "literature",
            "d": "sports"
        },
        "answer": "খ",
        "explanation": "বিটোভেন একজন জার্মান সুরকার।"
    },
    {
        "id": 1371,
        "question": "The team is ------ eleven players. [HED-2015]",
        "options": {
            "a": "made of",
            "b": "made up",
            "c": "made up of",
            "d": "made"
        },
        "answer": "গ",
        "explanation": "Make up- মনস্থির করা, Make of- কোনো কিছু দিয়ে তৈরি, made up of- কতগুলো অংশ দিয়ে গঠিত হওয়া। একটি দল গঠন করা হয়েছে ১১ জন খেলোয়াড়ের সমন্বয়ে গঠিত হয়।"
    },
    {
        "id": 1372,
        "question": "The poor man said \"I ---- starve than beg\". Fill up the space by– [HED-2015]",
        "options": {
            "a": "rather",
            "b": "better",
            "c": "would rather",
            "d": "would better"
        },
        "answer": "গ",
        "explanation": "Would rather; had better এদের পরে verb এর base form বসে।"
    },
    {
        "id": 1373,
        "question": "Which is the correct passive form of sentence? \"He is writing a letter\". [HED-2015]",
        "options": {
            "a": "A letter is written by him.",
            "b": "A letter was written by him.",
            "c": "A letter was being written by him.",
            "d": "A letter is being written by him."
        },
        "answer": "ঘ",
        "explanation": "Active থেকে Passive voice-এ রূপান্তর : Structure : Active voice-এর object প্রথমে আনতে হবে তারপর Auxiliary verb + being + verb এর Past participle + preposition + Active voice এর Subject বসবে।"
    },
    {
        "id": 1374,
        "question": "Noun of the word 'approve' is– [HED-2015]",
        "options": {
            "a": "approving",
            "b": "approved",
            "c": "approveness",
            "d": "approval"
        },
        "answer": "ঘ",
        "explanation": "approve অর্থ অনুমোদন করা। এর Noun form হচ্ছে Approval, যার অর্থ অনুমোদন।"
    },
    {
        "id": 1375,
        "question": "What do you mean by 'gala day'? [HED-2015]",
        "options": {
            "a": "a day of feast",
            "b": "a day of festivity",
            "c": "a day of farewell",
            "d": "a day of thanks"
        },
        "answer": "খ",
        "explanation": "A gala day অর্থ উৎসবমুখর দিন। আবার a day of festivity অর্থ উৎসবের দিন।"
    },
    {
        "id": 1376,
        "question": " 'Kith and kin' means —— [HED-2015]",
        "options": {
            "a": "friends",
            "b": "colleagues",
            "c": "competitors",
            "d": "relatives"
        },
        "answer": "ঘ",
        "explanation": "Kith and kin একটি Phrase, যার অর্থ আত্মীয়। Relatives অর্থ আত্মীয়।"
    },
    {
        "id": 1377,
        "question": "Which is the appropriate meaning for 'hush money'? [HED-2015]",
        "options": {
            "a": "silent money",
            "b": "money given as bribe",
            "c": "quite money",
            "d": "borrowed money"
        },
        "answer": "খ",
        "explanation": "hush money অর্থ ঘুষ। যে টাকা ঘুষ হিসেবে দেয়া হয়, তাকে hush money বলে।"
    },
    {
        "id": 1378,
        "question": "They travelled to Sylhet– [HED-2015]",
        "options": {
            "a": "by foot",
            "b": "by walking",
            "c": "on foot",
            "d": "on their feet"
        },
        "answer": "গ",
        "explanation": "পায়ে হেঁটে যাওয়া বলতে on foot বসে।"
    }
]
