import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

files = [
    'index.html',
    'Ict-wizard-NTRCA-313-and-325.html',
    'Biddabari-NTRCA.html',
    'Eminent-Petro-Bangla.html',
    'class 9-10-Computer-GK.html',
    'Saif-Sir-NTRCA-Suggestion.html',
    'Ampibian-Suggestion.html'
]

print(f"{'File Name':35s} | {'Size (Bytes)':14s} | {'Size (MB)':10s}")
print('-' * 65)
for f in files:
    sz = os.path.getsize(f)
    print(f"{f:35s} | {sz:14,d} | {sz/(1024*1024):8.2f} MB")
