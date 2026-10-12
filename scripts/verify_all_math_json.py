import os
import json

math_dir = 'JSON Data/Saif Sir NTRCA Suggestion/Math'
files = sorted(os.listdir(math_dir))
print(f'Total Math JSON files: {len(files)}')

total_mcqs = 0
errors = []

for f in files:
    if not f.endswith('.json'):
        continue
    path = os.path.join(math_dir, f)
    with open(path, 'r', encoding='utf-8') as fp:
        try:
            data = json.load(fp)
        except Exception as e:
            errors.append(f'{f}: JSON decode error: {e}')
            continue
    
    # check keys
    for k in ['title', 'subject', 'model_test', 'total_questions', 'questions']:
        if k not in data:
            errors.append(f'{f}: missing key {k}')
    
    if data.get('subject') != 'Math':
        errors.append(f"{f}: subject is {data.get('subject')}")
        
    qs = data.get('questions', [])
    if len(qs) != data.get('total_questions'):
        errors.append(f"{f}: question count mismatch: {len(qs)} vs {data.get('total_questions')}")
    
    total_mcqs += len(qs)
    
    for i, q in enumerate(qs, 1):
        if q.get('id') != i:
            errors.append(f"{f} Q{i}: id is {q.get('id')}")
        if not q.get('question'):
            errors.append(f"{f} Q{i}: empty question")
        opts = q.get('options', {})
        for opt_key in ['ক', 'খ', 'গ', 'ঘ']:
            if opt_key not in opts or not str(opts[opt_key]).strip():
                errors.append(f"{f} Q{i}: missing option {opt_key}")
        ans = q.get('answer')
        if ans not in ['ক', 'খ', 'গ', 'ঘ', '-']:
            errors.append(f"{f} Q{i}: invalid answer {ans}")
        if not q.get('explanation'):
            errors.append(f"{f} Q{i}: empty explanation")

print(f'Total MCQs across all Math files: {total_mcqs}')
if errors:
    print(f'ERRORS FOUND ({len(errors)}):')
    for err in errors[:20]:
        print('  -', err)
else:
    print('ALL 26 MATH JSON FILES VALIDATED PERFECTLY! ZERO ERRORS!')
