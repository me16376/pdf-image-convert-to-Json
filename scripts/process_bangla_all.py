import os
import re
import json
import sys
import pymupdf
from bijoy2unicode import converter

sys.stdout.reconfigure(encoding='utf-8')
conv = converter.Unicode()

def bijoy_to_unicode(text):
    if not text:
        return ""
    pre_map = {
        'ÿ': '¶',
        '•ÿ': '•¶',
        'nè': 'হ্ণ',
        'Ì': 'ত্থ',
        'Í': 'ত্ম',
        'ä': 'ব্ধ',
        '®§': 'ষ্ম',
        'š’': 'ন্থ',
        'É': 'ণ্ঠ',
        'Z¥': 'ত্ম',
        'åƒ': 'ভ্রূ',
        'åæ': 'ভ্ৰু',
        '²': 'ক্ষ্ম',
        'ò': 'ষ্ণ',
        'ý': 'হ্ন',
        'þ': 'হ্ম',
        '×': 'দ্ধ',
        'Ä': 'ঞ্জ',
        'Æ': 'ট্ট',
        '¼': 'ঙ্ক',
        'Ü': 'ন্ধ',
        'Á': 'জ্ঞ',
        'Â': 'ঞ্চ',
        'Ã': 'ঞ্ছ',
        '‘': '্তু',
        '’': '্থ',
        '‹': '্ক',
        '—': '্ত',
        '˜': 'দ্',
        'š': 'ন্',
        'œ': '্ন',
        '¯': 'স্',
        '°': 'ক্ক',
        '³': 'ক্ত',
        'µ': 'ক্র',
        '»': 'গ্ধ',
        '½': 'ঙ্গ',
        '¾': 'জ্জ',
        '¿': '্ত্র',
        'Ç': 'ড্ড',
        'È': 'ণ্ট',
        'Ê': 'ণ্ড',
        'Ë': 'ত্ত',
        'Î': 'ত্র',
        'Ï': 'দ্দ',
        'Ø': 'দ্ব',
        'Ù': 'দ্ম',
        'Ú': 'ন্ঠ',
        'Û': 'ন্ড',
        'Ý': 'ন্স',
        'ß': 'প্ত',
        'å': 'ভ্র',
        'é': 'ল্ক',
        'ê': 'ল্গ',
        'ë': 'ল্ট',
        'ì': 'ল্ড',
        'í': 'ল্প',
        'ï': 'শু',
        'ð': 'শ্চ',
        'ó': 'ষ্ট',
        'ô': 'ষ্ঠ',
        '÷': 'স্ট',
        'ø': 'স্ন',
        'û': 'হু',
        'ü': 'হৃ',
    }
    for k, v in pre_map.items():
        text = text.replace(k, v)
    u = conv.convertBijoyToUnicode(text)
    
    # Fix reph positioning
    u = re.sub(r'([ক-হড়-য়](?:্[ক-হড়-য়])?[া-ৌ]?)র্', r'র্\1', u)
    
    # Fix words / ligatures
    post_map = {
        'রম্ন': 'রু',
        'রূ': 'রূ',
        'বিশেস্নষণ': 'বিশ্লেষণ',
        'বিশিস্নষ্ট': 'বিশ্লিষ্ট',
        'কতির্ক': 'কর্তৃক',
        'পূণর্': 'পূর্ণ',
        'দীঘর্': 'দীর্ঘ',
        'অধর্মাত্রা': 'অর্ধমাত্রা',
        'পবর্ত': 'পর্বত',
        'জরম্নরী': 'জরুরী',
        'নজরম্নল': 'নজরুল',
        'ফররম্নখ': 'ফররুখ',
        'আখতারম্নজ্জামান': 'আখতারুজ্জামান',
        'দ্বিরম্নক্ত': 'দ্বিরুক্ত',
        'চযার্পদ': 'চর্যাপদ',
        'কীতর্ন': 'কীর্তন',
        'প্রণয়োপাখ্যান': 'প্রণয়োপাখ্যান',
        'নিমের্লন্দু': 'নির্মলেন্দু',
        'বণের্র': 'বর্ণের',
        'বণির্ট': 'বর্ণটি',
        'বণর্': 'বর্ণ',
        'অন্ত্মজাির্তক': 'আন্তর্জাতিক',
        'আন্ত্মজাির্তক': 'আন্তর্জাতিক',
        'সবার্ত্মক': 'সর্বাত্মক',
        'শিÿা': 'শিক্ষা',
        'দীÿা': 'দীক্ষা',
        'পরীÿা': 'পরীক্ষা',
        'যুক্তাÿর': 'যুক্তাক্ষর',
        'আকাঙ্ÿা': 'আকাঙ্ক্ষা',
        'আকাঙ্ÿিত': 'আকাঙ্ক্ষিত',
        'উচ্চমধ্-': 'উচ্চমধ্য-',
        'দন্ত্ম্য': 'দন্ত্য',
        'দন্ত্ম': 'দন্ত',
        'স্বরান্ত্ম': 'স্বরান্ত',
        'উড়িযা': 'উড়িয়া',
        'পলস্নী': 'পল্লী',
        'মুহম্মদ শহীদুলস্নাহ্‌': 'মুহম্মদ শহীদুল্লাহ্',
        'শহীদুলস্নাহ্': 'শহীদুল্লাহ্',
        'শহীদুলস্নাহ': 'শহীদুল্লাহ্',
        'ওয়ালীউলস্নাহ': 'ওয়ালীউল্লাহ',
        'আলস্নাহ': 'আল্লাহ',
    }
    for k, v in post_map.items():
        u = u.replace(k, v)
    u = re.sub(r'ন্ত্ম', 'ন্ত', u)
    return u.strip()

ANSWER_KEY_MAP = {
    'P': 'ক',
    'Q': 'খ',
    'R': 'গ',
    'S': 'ঘ',
    'K': 'ক',
    'L': 'খ',
    'M': 'গ',
    'N': 'ঘ',
    'a': 'ক',
    'b': 'খ',
    'c': 'গ',
    'd': 'ঘ',
}

BANGLA_TOPICS = {
    1: ("লেকচার-০১. বাংলা ভাষার উদ্ভব ও ক্রমবিকাশ, বাংলা লিপি, ধ্বনি ও বর্ণ, অক্ষর, যুক্তবর্ণ", "বাংলা ভাষার উদ্ভব ও ক্রমবিকাশ, বাংলা লিপি, ধ্বনি ও বর্ণ, অক্ষর, যুক্তবর্ণ"),
    2: ("লেকচার-০২. বাংলা ভাষার রীতি ও বিভাজন, ধ্বনি পরিবর্তন", "বাংলা ভাষার রীতি ও বিভাজন, ধ্বনি পরিবর্তন"),
    3: ("লেকচার-০৩. ণ-ত্ব বিধান এবং ষ-ত্ব বিধান, শব্দের শ্রেণিবিভাগ", "ণ-ত্ব বিধান এবং ষ-ত্ব বিধান, শব্দের শ্রেণিবিভাগ"),
    4: ("লেকচার-০৪. সন্ধি, সমার্থক শব্দ ও প্রতিশব্দ", "সন্ধি, সমার্থক শব্দ/প্রতিশব্দ"),
    5: ("লেকচার-০৫. পদ প্রকরণ, বিভিন্ন শব্দের অর্থ, বিপরীত শব্দ", "পদ প্রকরণ, বিভিন্ন শব্দের অর্থ, বিপরীত শব্দ"),
    6: ("লেকচার-০৬. লিঙ্গ, বচন, উপসর্গ", "লিঙ্গ, বচন, উপসর্গ"),
    7: ("লেকচার-০৭. সংখ্যাবাচক শব্দ, দ্বিরুক্ত শব্দ", "সংখ্যাবাচক শব্দ, দ্বিরুক্ত শব্দ"),
    8: ("লেকচার-০৮. প্রকৃতি ও প্রত্যয়", "প্রকৃতি প্রত্যয়"),
    9: ("লেকচার-০৯. বানান শুদ্ধিকরণ, বাক্য শুদ্ধিকরণ, বাক্য ও বাক্য পরিবর্তন, পারিভাষিক শব্দ, অনুবাদ, যতি বা ছেদচিহ্ন", "বানান শুদ্ধিকরণ, বাক্য শুদ্ধিকরণ, বাক্য ও বাক্য পরিবর্তন, পারিভাষিক শব্দ, অনুবাদ, যতি বা ছেদচিহ্ন"),
    10: ("লেকচার-১০. কারক ও বিভক্তি, বাক্য সংকোচন, বাগ্‌ধারা", "কারক ও বিভক্তি, বাক্য সংকোচন, বাগ্‌ধারা"),
    11: ("লেকচার-১১. সমাস, চিঠিপত্র", "সমাস, চিঠিপত্র"),
    12: ("লেকচার-১২. বাংলা সাহিত্যের প্রাচীন যুগ ও মধ্যযুগ (চর্যাপদ, শ্রীকৃষ্ণকীর্তন, মঙ্গলকাব্য)", "বাংলা সাহিত্যের প্রাচীন যুগ (চর্যাপদ), বাংলা সাহিত্যের মধ্যযুগ, শ্রীকৃষ্ণকীর্তন, বৈষ্ণব পদাবলি, মঙ্গলকাব্য, রোমান্সধর্মী প্রণয়োপাখ্যান, রোসাঙ্গ রাজসভায় বাংলা সাহিত্য"),
    13: ("লেকচার-১৩. বাংলা সাহিত্যের আধুনিক যুগ (ফোর্ট উইলিয়াম কলেজ থেকে আধুনিক সাহিত্যিকগণ)", "বাংলা সাহিত্যের আধুনিক যুগ, ফোর্ট উইলিয়াম কলেজ, মাইকেল মধুসূদন দত্ত, বঙ্কিমচন্দ্র চট্টোপাধ্যায়, রবীন্দ্রনাথ ঠাকুর, শরৎচন্দ্র চট্টোপাধ্যায়, মানিক বন্দ্যোপাধ্যায়, শওকত ওসমান, শামসুর রাহমান, জহির রায়হান"),
    14: ("লেকচার-১৪. সাহিত্যিকদের পরিচিতি, বিখ্যাত গ্রন্থ, উপন্যাস, নাটক, মুক্তিযুদ্ধ ও ভাষা আন্দোলনভিত্তিক সাহিত্য", "কাজী নজরুল ইসলাম, জসীমউদ্‌দীন, ঈশ্বরচন্দ্র বিদ্যাসাগর ও অন্যান্য সাহিত্যিক, বিখ্যাত উপন্যাস, নাটক, বিখ্যাত সাহিত্য বিষয়ক গ্রন্থ, সাহিত্যিকদের উপাধি, ছদ্মনাম, বিখ্যাত পঙ্‌ক্তি, গান, ভাষা আন্দোলন ও মুক্তিযুদ্ধভিত্তিক সাহিত্য")
}

def cluster_spans_into_lines(spans, y_threshold=4.0):
    lines = []
    for s in spans:
        y_center = (s[0][1] + s[0][3]) / 2
        matched = False
        for line in lines:
            if abs(line['y_center'] - y_center) < y_threshold:
                line['spans'].append(s)
                matched = True
                break
        if not matched:
            lines.append({'y_center': y_center, 'spans': [s]})
    lines.sort(key=lambda l: l['y_center'])
    for l in lines:
        l['spans'].sort(key=lambda s: s[0][0])
    return lines

def parse_line_stream(lines, sec_name):
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

        if m_q is not None and not any('ProshnaP' in s[1] and s[2] in ['K', 'L', 'M', 'N'] for s in spans_in_line):
            if cur_q and len(cur_q['options']) == 4:
                questions.append(cur_q)
            cur_q = {
                'source_id': m_q,
                'section': sec_name,
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

        has_opt = any('ProshnaP' in s[1] and s[2] in ['K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S'] for s in spans_in_line)
        if has_opt:
            i = 0
            while i < len(spans_in_line):
                s = spans_in_line[i]
                if 'ProshnaP' in s[1]:
                    if s[2] in ['K', 'L', 'M', 'N']:
                        opt_parts = []
                        i += 1
                        while i < len(spans_in_line) and 'ProshnaP' not in spans_in_line[i][1]:
                            opt_parts.append(bijoy_to_unicode(spans_in_line[i][2]))
                            i += 1
                        cur_q['options'].append(' '.join(opt_parts).strip())
                        continue
                    elif s[2] in ['P', 'Q', 'R', 'S']:
                        cur_q['ans'] = ANSWER_KEY_MAP.get(s[2])
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
        questions.append(cur_q)
    return questions

def process_bangla_pdf(lec_num):
    fname = f"Lecture Sheet-{lec_num:02d}.pdf"
    fpath = os.path.join(r"PDF/Biddabari-NTRCA/Bangla", fname)
    if not os.path.exists(fpath):
        print(f"File not found: {fpath}")
        return None

    doc = pymupdf.open(fpath)
    file_title, full_topic = BANGLA_TOPICS.get(lec_num, (f"লেকচার-{lec_num:02d}", f"লেকচার-{lec_num:02d}"))

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

    all_questions = []
    global_id = 1
    sec_counts = {'Teacher’s Work': 0, 'Student Practice': 0, 'Home Work': 0, 'Class Test': 0}

    for pno in range(len(doc)):
        page = doc[pno]
        # determine section
        sec = 'Teacher’s Work'
        if pno == len(doc) - 1:
            sec = 'Class Test'
        elif pno >= len(doc) - 4:
            sec = 'Home Work'
        elif pno >= len(doc) - 6:
            sec = 'Student Practice'

        spans = []
        for b in page.get_text('dict')['blocks']:
            if 'lines' in b:
                for l in b['lines']:
                    for s in l['spans']:
                        if s['text'].strip() and 85 <= s['bbox'][1] <= 735:
                            # skip DËigvjv table area on last page
                            if pno == len(doc)-1 and s['bbox'][0] > 490 and s['bbox'][1] > 380:
                                continue
                            spans.append((s['bbox'], s['font'], s['text'].strip()))

        if not spans: continue

        left = [s for s in spans if s[0][0] < 305]
        right = [s for s in spans if s[0][0] >= 305]
        qs_2col = parse_line_stream(cluster_spans_into_lines(left), sec) + parse_line_stream(cluster_spans_into_lines(right), sec)
        qs_1col = parse_line_stream(cluster_spans_into_lines(spans), sec)

        chosen_qs = qs_2col if len(qs_2col) >= len(qs_1col) else qs_1col

        # If on last page, assign CT answers from DËigvjv
        if pno == len(doc) - 1 and ct_answers:
            for q in chosen_qs:
                if not q.get('ans'):
                    q['ans'] = ct_answers.get(q['source_id'], 'ক')

        for q in chosen_qs:
            q_clean = {
                "id": global_id,
                "section": q['section'],
                "question": q['q_text'].strip(),
                "options": [opt.strip() for opt in q['options']],
                "answer": q.get('ans') or "ক",
                "explanation": ""
            }
            all_questions.append(q_clean)
            sec_counts[q['section']] = sec_counts.get(q['section'], 0) + 1
            global_id += 1

    payload = {
        "title": full_topic,
        "lecture_sheet": fname,
        "subject": "Bangla",
        "total_questions": len(all_questions),
        "sections_breakdown": sec_counts,
        "questions": all_questions
    }

    out_dir = r"JSON Data/Biddabari-NTRCA/Bangla"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, f"{file_title}.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"[{fname}] -> {len(all_questions)} MCQs saved to {os.path.basename(out_file)}")
    return payload

if __name__ == '__main__':
    print("Starting extraction for all 14 Bangla lectures...")
    summary = []
    for num in range(1, 15):
        res = process_bangla_pdf(num)
        if res:
            summary.append((res['lecture_sheet'], res['title'][:40], res['total_questions']))
    print("\n=== Bangla Summary ===")
    for s in summary:
        print(f"{s[0]}: {s[2]} MCQs ({s[1]}...)")
