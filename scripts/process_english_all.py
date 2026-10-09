import os
import re
import json
import sys
import pymupdf
sys.path.insert(0, os.path.abspath('.'))
from bijoy2unicode import converter
from scripts.process_bangla_all import bijoy_to_unicode, cluster_spans_into_lines

sys.stdout.reconfigure(encoding='utf-8')

ANS_MAP = {
    'a': 'ক', 'b': 'খ', 'c': 'গ', 'd': 'ঘ',
    'p': 'ক', 'q': 'খ', 'r': 'গ', 's': 'ঘ',
    'k': 'ক', 'l': 'খ', 'm': 'গ', 'n': 'ঘ',
    '1': 'ক', '2': 'খ', '3': 'গ', '4': 'ঘ'
}

ENGLISH_TOPICS = {
    1: ("লেকচার-০১. Parts of Speech-I (Noun, Pronoun, Adjective, Adverb)", "Parts of Speech-I (Noun, Pronoun, Adjective, Adverb)"),
    2: ("লেকচার-০২. Parts of Speech-II (Verb, Conjunction, Interjection)", "Parts of Speech-II (Verb, Conjunction, Interjection)"),
    3: ("লেকচার-০৩. Tense, Conditional Sentence", "Tense, Conditional Sentence"),
    4: ("লেকচার-০৪. Right form of Verb", "Right form of Verb"),
    5: ("লেকচার-০৫. Subject-Verb Agreement", "Subject-Verb Agreement"),
    6: ("লেকচার-০৬. Preposition, Spelling, Spelling Mistakes", "Preposition, Spelling/Spelling Mistakes"),
    7: ("লেকচার-০৭. Appropriate Preposition, Group Verb", "Appropriate Preposition, Group Verb"),
    8: ("লেকচার-০৮. Article, Determiner, Number, Gender", "Article, Determiner, Number, Gender"),
    9: ("লেকচার-০৯. Voice", "Voice"),
    10: ("লেকচার-১০. Narration", "Narration"),
    11: ("লেকচার-১১. Word Formation, Degree", "Word Formation, Degree"),
    12: ("লেকচার-১২. Sentence, Transformation of Sentence", "Sentence, Transformation of Sentence"),
    13: ("লেকচার-১৩. One Word Substitution, Synonym & Antonym", "One Word Substitution, Synonym & Antonym"),
    14: ("লেকচার-১৪. Translation, Idioms & Phrases", "Translation, Idioms & Phrases"),
    15: ("লেকচার-১৫. Correction", "Correction"),
    16: ("লেকচার-১৬. Different Authors & Their Literary Works, Figure of Speech", "Different Authors & Their Literary Works, Figure of Speech")
}

def convert_span(text, font):
    if not text: return ''
    if any(k in font.lower() for k in ['sutonnymj', 'karnaphulimj', 'bijoy']):
        return bijoy_to_unicode(text)
    return text

def parse_english_stream(lines, is_class_test=False, ct_answers=None):
    questions = []
    cur_q = None
    cur_opt_idx = -1

    for line in lines:
        spans = line['spans']
        if not spans: continue
        first_span = spans[0]
        first_text = first_span[2].strip()

        # Check if line starts with question number
        m_q = None
        m = re.match(r'^(\d+)\.\s*(.*)', first_text)
        if m and 'ProshnaP' not in first_span[1] and first_text not in ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ']:
            m_q = int(m.group(1))
            q_start_text = convert_span(m.group(2), first_span[1])

        # If it's a new question start
        if m_q is not None:
            if cur_q and len(cur_q['options']) == 4:
                if is_class_test and ct_answers and not cur_q['ans']:
                    cur_q['ans'] = ct_answers.get(cur_q['source_id'])
                if cur_q['ans'] is not None:
                    cur_q['options'] = [re.sub(r'\s+', ' ', opt).strip() for opt in cur_q['options']]
                    cur_q['q_text'] = re.sub(r'\s+', ' ', cur_q['q_text']).strip()
                    questions.append(cur_q)

            cur_q = {
                'source_id': m_q,
                'q_text': q_start_text,
                'options': [],
                'ans': None
            }
            cur_opt_idx = -1

            for s in spans[1:]:
                stext = s[2].strip()
                sfont = s[1]
                if not stext: continue

                if 'ProshnaP' in sfont and stext.lower() in ANS_MAP:
                    cur_q['ans'] = ANS_MAP[stext.lower()]
                    cur_opt_idx = -2
                elif stext == 'ⓐ':
                    cur_opt_idx = 0
                    cur_q['options'].append('')
                elif stext == 'ⓑ':
                    cur_opt_idx = 1
                    cur_q['options'].append('')
                elif stext == 'ⓒ':
                    cur_opt_idx = 2
                    cur_q['options'].append('')
                elif stext == 'ⓓ':
                    cur_opt_idx = 3
                    cur_q['options'].append('')
                else:
                    conv = convert_span(s[2], sfont)
                    if cur_opt_idx == -1:
                        cur_q['q_text'] += (' ' if cur_q['q_text'] else '') + conv
                    elif 0 <= cur_opt_idx < len(cur_q['options']):
                        cur_q['options'][cur_opt_idx] += (' ' if cur_q['options'][cur_opt_idx] else '') + conv
            continue

        if not cur_q:
            continue

        for s in spans:
            stext = s[2].strip()
            sfont = s[1]
            if not stext: continue

            if 'ProshnaP' in sfont and stext.lower() in ANS_MAP:
                cur_q['ans'] = ANS_MAP[stext.lower()]
                cur_opt_idx = -2
            elif stext == 'ⓐ':
                cur_opt_idx = 0
                cur_q['options'].append('')
            elif stext == 'ⓑ':
                cur_opt_idx = 1
                cur_q['options'].append('')
            elif stext == 'ⓒ':
                cur_opt_idx = 2
                cur_q['options'].append('')
            elif stext == 'ⓓ':
                cur_opt_idx = 3
                cur_q['options'].append('')
            else:
                conv = convert_span(s[2], sfont)
                if cur_opt_idx == -1:
                    cur_q['q_text'] += (' ' if cur_q['q_text'] else '') + conv
                elif 0 <= cur_opt_idx < len(cur_q['options']):
                    cur_q['options'][cur_opt_idx] += (' ' if cur_q['options'][cur_opt_idx] else '') + conv

    if cur_q and len(cur_q['options']) == 4:
        if is_class_test and ct_answers and not cur_q['ans']:
            cur_q['ans'] = ct_answers.get(cur_q['source_id'])
        if cur_q['ans'] is not None:
            cur_q['options'] = [re.sub(r'\s+', ' ', opt).strip() for opt in cur_q['options']]
            cur_q['q_text'] = re.sub(r'\s+', ' ', cur_q['q_text']).strip()
            questions.append(cur_q)

    return questions

def process_english_pdf(sheet_num):
    fname = f"Lecture Sheet-{sheet_num:02d}.pdf"
    fpath = os.path.join(r"PDF/বিদ্যাবাড়ি ১৯ তম কোর্স PDF/English", fname)
    if not os.path.exists(fpath):
        print(f"File not found: {fpath}")
        return None

    doc = pymupdf.open(fpath)
    total_pages = len(doc)
    file_title, full_topic = ENGLISH_TOPICS.get(sheet_num, (f"লেকচার-{sheet_num:02d}", f"লেকচার-{sheet_num:02d}"))

    # 1. Class Test answers from last page
    last_page = doc[-1]
    ct_answers = {}
    for b in last_page.get_text('blocks'):
        txt = b[4].strip()
        lines = [l.strip() for l in txt.split('\n') if l.strip()]
        idx = 0
        while idx < len(lines) - 1:
            if lines[idx].isdigit() and lines[idx+1].lower() in ANS_MAP:
                qnum = int(lines[idx])
                ans = ANS_MAP[lines[idx+1].lower()]
                if 1 <= qnum <= 25:
                    ct_answers[qnum] = ans
                idx += 2
            else:
                idx += 1

    all_raw_questions = []
    in_home_work = False

    for pno in range(total_pages):
        page = doc[pno]
        is_ct = (pno == total_pages - 1)

        spans_all = []
        spans_left = []
        spans_right = []
        for b in page.get_text('dict')['blocks']:
            if 'lines' in b:
                for l in b['lines']:
                    for s in l['spans']:
                        if s['text'].strip() and 55 <= s['bbox'][1] <= 735:
                            if is_ct and s['bbox'][0] > 500:
                                continue
                            mid_x = (s['bbox'][0] + s['bbox'][2]) / 2
                            span_item = (s['bbox'], s['font'], s['text'])
                            spans_all.append(span_item)
                            if mid_x < 305:
                                spans_left.append(span_item)
                            else:
                                spans_right.append(span_item)

        ll = cluster_spans_into_lines(spans_left)
        lr = cluster_spans_into_lines(spans_right)
        l_all = cluster_spans_into_lines(spans_all)

        qs_2col = parse_english_stream(ll, is_class_test=is_ct, ct_answers=ct_answers) + \
                  parse_english_stream(lr, is_class_test=is_ct, ct_answers=ct_answers)
        qs_comb = parse_english_stream(ll + lr, is_class_test=is_ct, ct_answers=ct_answers)
        qs_1col = parse_english_stream(l_all, is_class_test=is_ct, ct_answers=ct_answers)

        candidates = [qs_2col, qs_comb, qs_1col]
        qs_page = max(candidates, key=len)

        for q in qs_page:
            if is_ct:
                q['section'] = 'Class Test'
            else:
                if not in_home_work and pno >= (total_pages // 2):
                    if q['source_id'] == 1 and len(qs_page) >= 8:
                        in_home_work = True
                if pno >= total_pages - 4:
                    in_home_work = True
                q['section'] = 'Home Work' if in_home_work else 'Teacher’s Work'

        all_raw_questions.extend(qs_page)

    # Format into final schema
    final_questions = []
    sec_counts = {}
    for idx, q in enumerate(all_raw_questions, 1):
        sec = q['section']
        sec_counts[sec] = sec_counts.get(sec, 0) + 1
        final_questions.append({
            "id": idx,
            "section": sec,
            "question": q['q_text'],
            "options": q['options'],
            "answer": q['ans'],
            "explanation": ""
        })

    result_data = {
        "title": file_title,
        "lecture_sheet": fname,
        "subject": "English",
        "total_questions": len(final_questions),
        "sections_breakdown": sec_counts,
        "questions": final_questions
    }

    out_dir = r"JSON Data/বিদ্যাবাড়ি ১৯ তম কোর্স PDF/English"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{file_title}.json")

    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)

    print(f"Processed Sheet {sheet_num:02d}: {file_title} -> {len(final_questions)} MCQs {sec_counts}")
    return len(final_questions)

if __name__ == '__main__':
    total_mcqs = 0
    for s in range(1, 17):
        cnt = process_english_pdf(s)
        if cnt:
            total_mcqs += cnt
    print(f"\nCompleted all 16 English lectures! Total MCQs: {total_mcqs}")
