import os
import re
import json
import sys
import pymupdf
sys.path.insert(0, os.path.abspath('.'))
from bijoy2unicode import converter
from scripts.process_bangla_all import bijoy_to_unicode, cluster_spans_into_lines, ANSWER_KEY_MAP

sys.stdout.reconfigure(encoding='utf-8')

GK_TOPICS = {
    1: ("লেকচার-০১. বাংলাদেশের ভৌগোলিক পরিচিতি, ভূ-প্রকৃতি, আবহাওয়া ও জলবায়ু, জাতীয় বিষয়াবলি", "বাংলাদেশের ভৌগোলিক পরিচিতি, ভূ-প্রকৃতি, আবহাওয়া ও জলবায়ু, জাতীয় বিষয়াবলি"),
    2: ("লেকচার-০২. বাংলাদেশের নদ-নদী, হাওড়, বিল ও হ্রদ, দ্বীপ ও চরসমূহ, পাহাড়-পর্বত", "বাংলাদেশের নদ-নদী, হাওড়, বিল ও হ্রদ, দ্বীপ ও চরসমূহ, পাহাড়-পর্বত"),
    3: ("লেকচার-০৩. বাঙালি জাতির উদ্ভব ও বিকাশ, বাংলার প্রাচীন জনপদ ও শাসন, মুঘল শাসন", "বাঙালি জাতির উদ্ভব ও বিকাশ, বাংলার প্রাচীন জনপদ ও শাসন, মুঘল শাসন"),
    4: ("লেকচার-০৪. বাংলাদেশের মহান স্বাধীনতা যুদ্ধের ইতিহাস (১৯৫২-৭১), ভাষা আন্দোলন, যুক্তফ্রন্ট, ছয়দফা", "বাংলাদেশের মহান স্বাধীনতা যুদ্ধের ইতিহাস (১৯৫২-৭১), ভাষা আন্দোলন, যুক্তফ্রন্ট, ছয়দফা"),
    5: ("লেকচার-০৫. ৭ মার্চের ভাষণ, মুক্তিযুদ্ধ, সেক্টর, বীরশ্রেষ্ঠ পরিচিতি", "৭ মার্চের ভাষণ, মুক্তিযুদ্ধ, সেক্টর, বীরশ্রেষ্ঠ পরিচিতি"),
    6: ("লেকচার-০৬. বাংলাদেশের সংবিধান, জনসংখ্যা ও জনশুমারি, জাতিগোষ্ঠী ও উপজাতি", "বাংলাদেশের সংবিধান, জনসংখ্যা ও জনশুমারি, জাতিগোষ্ঠী ও উপজাতি"),
    7: ("লেকচার-০৭. বিশিষ্ট ব্যক্তিত্ব, গুরুত্বপূর্ণ স্থাপনা, ভাস্কর্য, কৃষ্টি ও সংস্কৃতি, শিক্ষা ব্যবস্থা", "বিশিষ্ট ব্যক্তিত্ব, গুরুত্বপূর্ণ স্থাপনা, ভাস্কর্য, কৃষ্টি ও সংস্কৃতি, শিক্ষা ব্যবস্থা"),
    8: ("লেকচার-০৮. বাংলাদেশের কৃষি সম্পদ, মৎস্য সম্পদ, খনিজ সম্পদ, অর্থনীতি, ব্যাংক ও বীমা", "বাংলাদেশের কৃষি সম্পদ, মৎস্য সম্পদ, খনিজ সম্পদ, অর্থনীতি, ব্যাংক ও বীমা"),
    9: ("লেকচার-০৯. বিশ্ব মানচিত্র, প্রাচীন সভ্যতাসমূহ, মহাদেশ পরিচিতি ও এশিয়া মহাদেশ", "বিশ্ব মানচিত্র, প্রাচীন সভ্যতাসমূহ, মহাদেশ পরিচিতি ও এশিয়া মহাদেশ"),
    10: ("লেকচার-১০. আমেরিকা ও অন্যান্য মহাদেশ, ভৌগোলিক উপনাম, বিভিন্ন দেশের আইনসভা, বিখ্যাত স্থাপত্য", "আমেরিকা ও অন্যান্য মহাদেশ, ভৌগোলিক উপনাম, বিভিন্ন দেশের আইনসভা, বিখ্যাত স্থাপত্য"),
    11: ("লেকচার-১১. জাতিপুঞ্জ, জাতিসংঘ, বৈশ্বিক অর্থনৈতিক প্রতিষ্ঠান, আঞ্চলিক ও আন্তর্জাতিক সংস্থা", "জাতিপুঞ্জ, জাতিসংঘ, বৈশ্বিক অর্থনৈতিক প্রতিষ্ঠান, আঞ্চলিক ও আন্তর্জাতিক সংস্থা"),
    12: ("লেকচার-১২. প্রথম ও দ্বিতীয় বিশ্বযুদ্ধ, বিখ্যাত চুক্তি, সামরিক জোট, বিপ্লব, সীমারেখা", "প্রথম ও দ্বিতীয় বিশ্বযুদ্ধ, বিখ্যাত চুক্তি, সামরিক জোট, বিপ্লব, সীমারেখা"),
    13: ("লেকচার-১৩. বিশ্বের গুরুত্বপূর্ণ দ্বীপ, পাহাড়-পর্বত, প্রণালী, সাগর, মহাসাগর, খাল ও নদী", "বিশ্বের গুরুত্বপূর্ণ দ্বীপ, পাহাড়-পর্বত, প্রণালী, সাগর, মহাসাগর, খাল ও নদী"),
    14: ("লেকচার-১৪. সাম্প্রতিক বাংলাদেশ ও আন্তর্জাতিক বিষয়াবলি, পুরস্কার, খেলাধুলা", "সাম্প্রতিক বাংলাদেশ ও আন্তর্জাতিক বিষয়াবলি, পুরস্কার, খেলাধুলা"),
    15: ("লেকচার-১৫. পদার্থ, পরমাণু, এসিড-ক্ষার, শব্দ ও তরঙ্গ, আলো ও শক্তি, বায়ুমণ্ডল", "পদার্থ, পরমাণু, এসিড-ক্ষার, শব্দ ও তরঙ্গ, আলো ও শক্তি, বায়ুমণ্ডল"),
    16: ("লেকচার-১৬. গ্যাস ও জ্বালানি, মানবদেহ, খাদ্য ও ভিটামিন, উদ্ভিদজগৎ, রোগব্যাধি, সৌরজগৎ", "গ্যাস ও জ্বালানি, মানবদেহ, খাদ্য ও ভিটামিন, উদ্ভিদজগৎ, রোগব্যাধি, সৌরজগৎ"),
    17: ("লেকচার-১৭. কম্পিউটারের ইতিহাস, প্রজন্ম, প্রকারভেদ, সংগঠন, পেরিফেরালস, মেমোরি", "কম্পিউটারের ইতিহাস, প্রজন্ম, প্রকারভেদ, সংগঠন, পেরিফেরালস, মেমোরি"),
    18: ("লেকচার-১৮. কম্পিউটার সফটওয়্যার, অপারেটিং সিস্টেম, প্রোগ্রামিং, ইন্টারনেট, নেটওয়ার্ক, সাইবার ক্রাইম", "কম্পিউটার সফটওয়্যার, অপারেটিং সিস্টেম, প্রোগ্রামিং, ইন্টারনেট, নেটওয়ার্ক, সাইবার ক্রাইম")
}

def parse_gk_stream(lines, default_sec='Teacher’s Work', is_class_test=False, ct_answers=None):
    questions = []
    cur_q = None

    for line in lines:
        spans_in_line = line['spans']
        first_span = spans_in_line[0]

        if any(w in first_span[2] for w in ['GK K_vq', 'cÖ‡kœvËi', 'DËi:', 'DËigvjv']):
            continue

        m = re.match(r'^(\d+)\.$', first_span[2].strip())
        m_q = None
        if m: m_q = int(m.group(1))
        elif re.match(r'^\d+\.', first_span[2].strip()):
            m_q = int(first_span[2].strip().split('.', 1)[0])

        if m_q is not None and not any('ProshnaP' in s[1] and s[2].strip() in ['K', 'L', 'M', 'N'] for s in spans_in_line):
            if cur_q and len(cur_q['options']) == 4:
                if is_class_test and ct_answers and not cur_q['ans']:
                    cur_q['ans'] = ct_answers.get(cur_q['source_id'])
                if cur_q['ans'] is not None:
                    cur_q['options'] = [re.sub(r'\s+', ' ', opt).strip() for opt in cur_q['options']]
                    cur_q['q_text'] = re.sub(r'\s+', ' ', cur_q['q_text']).strip()
                    questions.append(cur_q)

            cur_q = {
                'source_id': m_q,
                'section': default_sec,
                'q_text': '',
                'options': [],
                'ans': None
            }
            if m:
                q_rest = ' '.join([bijoy_to_unicode(s[2]) for s in spans_in_line[1:]])
            else:
                first_text = bijoy_to_unicode(first_span[2].strip().split('.', 1)[1])
                q_rest = (first_text + ' ' + ' '.join([bijoy_to_unicode(s[2]) for s in spans_in_line[1:]])).strip()
            cur_q['q_text'] = q_rest
            continue

        if not cur_q: continue

        has_opt = any('ProshnaP' in s[1] and s[2].strip() in ['K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S'] for s in spans_in_line)
        if has_opt:
            i = 0
            while i < len(spans_in_line):
                s = spans_in_line[i]
                stext = s[2].strip()
                if 'ProshnaP' in s[1]:
                    if stext in ['K', 'L', 'M', 'N']:
                        opt_parts = []
                        i += 1
                        while i < len(spans_in_line) and 'ProshnaP' not in spans_in_line[i][1]:
                            opt_parts.append(bijoy_to_unicode(spans_in_line[i][2]))
                            i += 1
                        cur_q['options'].append(' '.join(opt_parts).strip())
                        continue
                    elif stext in ['P', 'Q', 'R', 'S']:
                        cur_q['ans'] = ANSWER_KEY_MAP.get(stext)
                        i += 1
                        continue
                i += 1
        else:
            cont_text = ' '.join([bijoy_to_unicode(s[2]) for s in spans_in_line])
            if len(cur_q['options']) == 0:
                cur_q['q_text'] += ' ' + cont_text
            else:
                if cur_q['options']:
                    cur_q['options'][-1] += ' ' + cont_text

    if cur_q and len(cur_q['options']) == 4:
        if is_class_test and ct_answers and not cur_q['ans']:
            cur_q['ans'] = ct_answers.get(cur_q['source_id'])
        if cur_q['ans'] is not None:
            cur_q['options'] = [re.sub(r'\s+', ' ', opt).strip() for opt in cur_q['options']]
            cur_q['q_text'] = re.sub(r'\s+', ' ', cur_q['q_text']).strip()
            questions.append(cur_q)

    return questions

def process_gk_pdf(sheet_num):
    fname = f"Lecture Sheet-{sheet_num:02d}.pdf"
    fpath = os.path.join(r"PDF/বিদ্যাবাড়ি ১৯ তম কোর্স PDF/GK", fname)
    if not os.path.exists(fpath):
        print(f"File not found: {fpath}")
        return None

    doc = pymupdf.open(fpath)
    total_pages = len(doc)
    file_title, full_topic = GK_TOPICS.get(sheet_num, (f"লেকচার-{sheet_num:02d}", f"লেকচার-{sheet_num:02d}"))

    # 1. Answer Key from DËigvjv on the last page(s)
    ct_answers = {}
    for p_offset in [1, 2]:
        if len(doc) >= p_offset:
            chk_page = doc[-p_offset]
            chk_text = chk_page.get_text('text')
            chk_lines = [l.strip() for l in chk_text.split('\n') if l.strip()]
            if 'DËigvjv' in chk_lines:
                idx = chk_lines.index('DËigvjv') + 1
                i = idx
                while i < len(chk_lines) - 1:
                    if chk_lines[i].isdigit() and chk_lines[i+1] in ['K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S']:
                        q_num = int(chk_lines[i])
                        ans_char = chk_lines[i+1]
                        ct_answers[q_num] = ANSWER_KEY_MAP.get(ans_char, ans_char)
                        i += 2
                        if q_num >= 10: break
                    else: i += 1
                break

    all_raw_questions = []

    for pno in range(total_pages):
        page = doc[pno]
        is_ct = (pno == total_pages - 1)
        sec = 'Teacher’s Work'
        if is_ct:
            sec = 'Class Test'
        elif pno >= total_pages - 4:
            sec = 'Home Work'
        elif pno >= total_pages - 6:
            sec = 'Student Practice'

        spans = []
        spans_left = []
        spans_right = []
        for b in page.get_text('dict')['blocks']:
            if 'lines' in b:
                for l in b['lines']:
                    for s in l['spans']:
                        if s['text'].strip() and 85 <= s['bbox'][1] <= 735:
                            if is_ct and (s['bbox'][0] > 480 and s['bbox'][1] > 350):
                                continue
                            span_item = (s['bbox'], s['font'], s['text'])
                            spans.append(span_item)
                            mid_x = (s['bbox'][0] + s['bbox'][2]) / 2
                            if mid_x < 305:
                                spans_left.append(span_item)
                            else:
                                spans_right.append(span_item)

        ll = cluster_spans_into_lines(spans_left)
        lr = cluster_spans_into_lines(spans_right)
        l_all = cluster_spans_into_lines(spans)

        qs_2c = parse_gk_stream(ll, sec, is_ct, ct_answers) + parse_gk_stream(lr, sec, is_ct, ct_answers)
        qs_comb = parse_gk_stream(ll + lr, sec, is_ct, ct_answers)
        qs_1c = parse_gk_stream(l_all, sec, is_ct, ct_answers)

        qs_page = max([qs_2c, qs_comb, qs_1c], key=len)
        all_raw_questions.extend(qs_page)

    final_questions = []
    sec_counts = {}
    for idx, q in enumerate(all_raw_questions, 1):
        sname = q['section']
        sec_counts[sname] = sec_counts.get(sname, 0) + 1
        final_questions.append({
            "id": idx,
            "section": sname,
            "question": q['q_text'],
            "options": q['options'],
            "answer": q['ans'],
            "explanation": ""
        })

    result_data = {
        "title": file_title,
        "lecture_sheet": fname,
        "subject": "GK",
        "total_questions": len(final_questions),
        "sections_breakdown": sec_counts,
        "questions": final_questions
    }

    out_dir = r"JSON Data/বিদ্যাবাড়ি ১৯ তম কোর্স PDF/GK"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{file_title}.json")

    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)

    print(f"Processed GK Sheet {sheet_num:02d}: {file_title} -> {len(final_questions)} MCQs {sec_counts}")
    return len(final_questions)

if __name__ == '__main__':
    total_mcqs = 0
    for s in range(1, 19):
        if s == 13:
            print("Skipping Sheet 13 for specialized OCR extraction...")
            continue
        cnt = process_gk_pdf(s)
        if cnt:
            total_mcqs += cnt
    print(f"\nCompleted vector GK lectures! Total MCQs: {total_mcqs}")
