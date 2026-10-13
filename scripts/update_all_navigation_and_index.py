import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Add CSS for card-saif and card-ampibian if not present
new_card_css = """    .card-saif::before {
      background: linear-gradient(90deg, #4338ca 0%, #6366f1 100%);
    }
    .card-saif .card-icon-wrap {
      background: linear-gradient(135deg, #4338ca 0%, #4f46e5 55%, #6366f1 100%);
      box-shadow: 0 6px 18px rgba(79, 70, 229, 0.3);
    }
    .card-saif .card-cta-btn {
      background: linear-gradient(135deg, #4338ca, #4f46e5);
    }
    .card-saif .card-cta-btn:hover {
      background: linear-gradient(135deg, #3730a3, #4338ca);
    }

    .card-ampibian::before {
      background: linear-gradient(90deg, #0f766e 0%, #14b8a6 100%);
    }
    .card-ampibian .card-icon-wrap {
      background: linear-gradient(135deg, #0f766e 0%, #0d9488 55%, #14b8a6 100%);
      box-shadow: 0 6px 18px rgba(13, 148, 136, 0.3);
    }
    .card-ampibian .card-cta-btn {
      background: linear-gradient(135deg, #0f766e, #0d9488);
    }
    .card-ampibian .card-cta-btn:hover {
      background: linear-gradient(135deg, #115e59, #0f766e);
    }
"""

if '.card-saif' not in idx_content:
    idx_content = idx_content.replace('.card-cgk .card-cta-btn {', new_card_css + '\n    .card-cgk .card-cta-btn {')

# Update header-nav-links in index.html
new_nav_links = """      <div class="header-nav-links">
        <a href="Biddabari-NTRCA.html" class="header-link-btn"><i class="fa-solid fa-graduation-cap" style="color: #059669;"></i> Biddabari-NTRCA</a>
        <a href="Eminent-Petro-Bangla.html" class="header-link-btn"><i class="fa-solid fa-fire-flame-curved" style="color: #ea580c;"></i> Petro Bangla</a>
        <a href="Ict-wizard-NTRCA-313-and-325.html" class="header-link-btn"><i class="fa-solid fa-laptop-code" style="color: #2563eb;"></i> ICT Wizard</a>
        <a href="class 9-10-Computer-GK.html" class="header-link-btn"><i class="fa-solid fa-desktop" style="color: #7c3aed;"></i> Computer GK</a>
        <a href="Saif-Sir-NTRCA-Suggestion.html" class="header-link-btn"><i class="fa-solid fa-award" style="color: #4f46e5;"></i> Saif Sir NTRCA</a>
        <a href="Ampibian-Suggestion.html" class="header-link-btn"><i class="fa-solid fa-book-bookmark" style="color: #0d9488;"></i> Ampibian</a>
      </div>"""

idx_content = re.sub(r'<div class="header-nav-links">[\s\S]*?</div>\s*</div>\s*</header>', new_nav_links + '\n    </div>\n  </header>', idx_content)

# Update Hero stats and pill in index.html
idx_content = re.sub(r'<div class="hero-pill">\s*<i class="fa-solid fa-sparkles"></i>\s*[\d\+\,\s]+প্রশ্নব্যাংক সংগ্রহশালা\s*</div>',
                     '<div class="hero-pill"><i class="fa-solid fa-sparkles"></i> ২৬,৯৮৬+ প্রশ্নব্যাংক সংগ্রহশালা</div>', idx_content)

idx_content = re.sub(r'<div class="stat-number">[\d\+\,\s]+</div>\s*<div class="stat-label"><i class="fa-solid fa-list-check"></i>\s*মোট প্রশ্ন \(MCQ\)</div>',
                     '<div class="stat-number">২৬,৯৮৬+</div>\n          <div class="stat-label"><i class="fa-solid fa-list-check"></i> মোট প্রশ্ন (MCQ)</div>', idx_content)

idx_content = re.sub(r'<div class="stat-number">[\d\+\,\s]+টি</div>\s*<div class="stat-label"><i class="fa-solid fa-book-open"></i>\s*মোট অধ্যায় ও পরীক্ষা</div>',
                     '<div class="stat-number">৫৫১টি</div>\n          <div class="stat-label"><i class="fa-solid fa-book-open"></i> মোট অধ্যায়, পরীক্ষা ও মডেল টেস্ট</div>', idx_content)

idx_content = re.sub(r'<div class="stat-number">[\d\+\,\s]+টি</div>\s*<div class="stat-label"><i class="fa-solid fa-shapes"></i>\s*বিশেষায়িত প্রশ্নব্যাংক</div>',
                     '<div class="stat-number">৬টি</div>\n          <div class="stat-label"><i class="fa-solid fa-shapes"></i> বিশেষায়িত প্রশ্নব্যাংক</div>', idx_content)

# Add Card 5 and Card 6 into cards-grid in index.html if not present
cards_to_add = """
      <!-- Card 5: Saif Sir NTRCA Suggestion -->
      <a href="Saif-Sir-NTRCA-Suggestion.html" class="qb-card card-saif" title="Saif Sir NTRCA Suggestion প্রশ্নব্যাংক খুলুন">
        <div>
          <div class="card-header-row">
            <div class="card-icon-wrap">
              <i class="fa-solid fa-award"></i>
            </div>
            <span class="card-tag"><i class="fa-solid fa-star"></i> ৩৩৮টি মডেল টেস্ট • স্পেশাল</span>
          </div>

          <div class="card-title-area">
            <h4 class="card-title">Saif Sir NTRCA Suggestion</h4>
            <p class="card-subtitle">বাংলা, ইংরেজি, সাধারণ জ্ঞান ও গণিতের ৩৩৮টি পূর্ণাঙ্গ মডেল টেস্টভিত্তিক বিশেষ প্রশ্নব্যাংক</p>
          </div>

          <div class="card-specs-row">
            <span class="spec-item"><i class="fa-solid fa-layer-group" style="color: #4f46e5;"></i> বিষয়: <strong>৪টি বিষয়</strong></span>
            <span class="spec-item"><i class="fa-solid fa-file-signature" style="color: #4f46e5;"></i> মডেল টেস্ট: <strong>৩৩৮টি টেস্ট</strong></span>
            <span class="spec-item"><i class="fa-solid fa-circle-question" style="color: #4f46e5;"></i> মোট প্রশ্ন: <strong>৭,২২৫টি MCQ</strong></span>
          </div>

          <div class="card-topics">
            <span class="topic-pill">বাংলা (২,২৩১টি)</span>
            <span class="topic-pill">সাধারণ জ্ঞান (২,২১১টি)</span>
            <span class="topic-pill">ইংরেজি (২,০৩৪টি)</span>
            <span class="topic-pill">গণিত (৭৪৯টি)</span>
            <span class="topic-pill">মডেল টেস্ট ১-১১১</span>
            <span class="topic-pill">স্টেপ-বাই-স্টেপ সমাধান</span>
          </div>
        </div>

        <div class="card-footer">
          <span class="card-footer-info"><i class="fa-solid fa-square-root-variable"></i> KaTeX গণিত সমীকরণ সমর্থিত</span>
          <span class="card-cta-btn">অনুশীলন করুন <i class="fa-solid fa-arrow-right"></i></span>
        </div>
      </a>

      <!-- Card 6: Ampibian Suggestion -->
      <a href="Ampibian-Suggestion.html" class="qb-card card-ampibian" title="Ampibian Suggestion প্রশ্নব্যাংক খুলুন">
        <div>
          <div class="card-header-row">
            <div class="card-icon-wrap">
              <i class="fa-solid fa-book-bookmark"></i>
            </div>
            <span class="card-tag"><i class="fa-solid fa-bullseye"></i> অধ্যায় ও টপিকভিত্তিক সাজেশন</span>
          </div>

          <div class="card-title-area">
            <h4 class="card-title">Ampibian Suggestion (অ্যাম্ফিবিয়ান সাজেশন)</h4>
            <p class="card-subtitle">বাংলা ব্যাকরণ, ইংরেজি গ্রামার, সাধারণ জ্ঞান ও পাটিগণিত/বীজগণিতের ৮৪টি উচ্চগুরুত্বপূর্ণ টপিক</p>
          </div>

          <div class="card-specs-row">
            <span class="spec-item"><i class="fa-solid fa-layer-group" style="color: #0d9488;"></i> বিষয়: <strong>৪টি বিষয়</strong></span>
            <span class="spec-item"><i class="fa-solid fa-folder-tree" style="color: #0d9488;"></i> টপিক: <strong>৮৪টি টপিক</strong></span>
            <span class="spec-item"><i class="fa-solid fa-circle-question" style="color: #0d9488;"></i> মোট প্রশ্ন: <strong>৬,১৫৭টি MCQ</strong></span>
          </div>

          <div class="card-topics">
            <span class="topic-pill">সাধারণ জ্ঞান (২,২৭৬টি)</span>
            <span class="topic-pill">বাংলা (১,৬৬২টি)</span>
            <span class="topic-pill">ইংরেজি (১,৫৭৪টি)</span>
            <span class="topic-pill">গণিত (৬৪৫টি)</span>
            <span class="topic-pill">কারক ও সমাস</span>
            <span class="topic-pill">মুক্তিযুদ্ধ ও সংবিধান</span>
          </div>
        </div>

        <div class="card-footer">
          <span class="card-footer-info"><i class="fa-solid fa-circle-check"></i> ৮৪টি পূর্ণাঙ্গ টপিক</span>
          <span class="card-cta-btn">অনুশীলন করুন <i class="fa-solid fa-arrow-right"></i></span>
        </div>
      </a>
"""

if 'card-saif' not in idx_content:
    # Insert before </main> or after Card 4
    idx_content = idx_content.replace('    </div>\n  </main>', cards_to_add + '\n    </div>\n  </main>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)
print('Updated index.html successfully!')

# 2. Update portal-nav in all 6 question bank HTML files
def get_portal_nav(active_id, count_text):
    return f"""  <!-- Top Navigation Portal Bar -->
  <nav class="portal-nav">
    <div class="portal-nav-inner">
      <div class="portal-links">
        <span style="font-weight: 700; color: #f1f5f9; display: flex; align-items: center; gap: 6px;">
          <i class="fa-solid fa-shapes"></i> সকল প্রশ্নব্যাংক:
        </span>
        <a href="Ict-wizard-NTRCA-313-and-325.html" class="portal-link{' active' if active_id == 'ict' else ''}"><i class="fa-solid fa-laptop-code"></i> ICT Wizard NTRCA</a>
        <a href="Biddabari-NTRCA.html" class="portal-link{' active' if active_id == 'bidyabari' else ''}"><i class="fa-solid fa-graduation-cap"></i> Biddabari-NTRCA (১৯তম)</a>
        <a href="Eminent-Petro-Bangla.html" class="portal-link{' active' if active_id == 'epb' else ''}"><i class="fa-solid fa-fire-flame-curved"></i> Eminent Petro Bangla</a>
        <a href="class 9-10-Computer-GK.html" class="portal-link{' active' if active_id == 'cgk' else ''}"><i class="fa-solid fa-desktop"></i> Class 9-10 Computer GK</a>
        <a href="Saif-Sir-NTRCA-Suggestion.html" class="portal-link{' active' if active_id == 'saif' else ''}"><i class="fa-solid fa-award"></i> Saif Sir NTRCA</a>
        <a href="Ampibian-Suggestion.html" class="portal-link{' active' if active_id == 'ampibian' else ''}"><i class="fa-solid fa-book-bookmark"></i> Ampibian Suggestion</a>
      </div>
      <div>
        <span style="opacity: 0.85;"><i class="fa-solid fa-file-circle-check"></i> {count_text}</span>
      </div>
    </div>
  </nav>"""

pages = [
    ('Ict-wizard-NTRCA-313-and-325.html', 'ict', '৭টি অধ্যায় (৫৯৪টি প্রশ্ন)'),
    ('Biddabari-NTRCA.html', 'bidyabari', '৬৭টি লেকচার শিট (৯,৯৭৪টি প্রশ্ন)'),
    ('Eminent-Petro-Bangla.html', 'epb', '৪৩টি পরীক্ষা (১,৯২২টি প্রশ্ন)'),
    ('class 9-10-Computer-GK.html', 'cgk', '১০টি অধ্যায় (১,১১৪টি প্রশ্ন)'),
    ('Saif-Sir-NTRCA-Suggestion.html', 'saif', '৩৩৮টি মডেল টেস্ট (৭,২২৫টি প্রশ্ন)'),
    ('Ampibian-Suggestion.html', 'ampibian', '৮৪টি টপিক (৬,১৫৭টি প্রশ্ন)')
]

for filename, active_id, count_txt in pages:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        nav_block = get_portal_nav(active_id, count_txt)

        # Replace existing portal-nav if present
        if '<nav class="portal-nav">' in content:
            content = re.sub(r'<!-- Top Navigation Portal Bar -->\s*<nav class="portal-nav">[\s\S]*?</nav>', nav_block, content)
            if '<nav class="portal-nav">' not in content:
                # If regex didn't catch due to comments
                content = re.sub(r'<nav class="portal-nav">[\s\S]*?</nav>', nav_block, content)
        else:
            # Insert after <body> or <body ...>
            content = re.sub(r'(<body[^>]*>)', r'\1\n\n' + nav_block, content)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated portal nav in {filename}")

print("\nAll files successfully updated with synchronized portal navigation!")
