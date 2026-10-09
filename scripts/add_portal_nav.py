import os

portal_css = """
    /* Top Navigation Portal Bar */
    .portal-nav {
      background: #0f172a;
      color: #94a3b8;
      font-size: 12px;
      border-bottom: 1px solid #1e293b;
    }
    .portal-nav-inner {
      max-width: 1300px;
      margin: 0 auto;
      padding: 6px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }
    .portal-links {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }
    .portal-link {
      color: #cbd5e1;
      text-decoration: none;
      font-weight: 500;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 3px 8px;
      border-radius: 4px;
      transition: all 0.15s ease;
    }
    .portal-link:hover {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.08);
    }
    .portal-link.active {
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.15);
      font-weight: 700;
    }
"""

def update_file(filename, active_page, count_text):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    if '.portal-nav' not in content:
        content = content.replace('  </style>', portal_css + '  </style>')

    nav_html = f"""  <!-- Top Navigation Portal Bar -->
  <nav class="portal-nav">
    <div class="portal-nav-inner">
      <div class="portal-links">
        <span style="font-weight: 700; color: #f1f5f9; display: flex; align-items: center; gap: 6px;">
          <i class="fa-solid fa-shapes"></i> সকল প্রশ্নব্যাংক:
        </span>
        <a href="Ict-wizard-NTRCA-313-and-325.html" class="portal-link{' active' if active_page == 'ict' else ''}"><i class="fa-solid fa-laptop-code"></i> ICT Wizard NTRCA</a>
        <a href="Biddabari-NTRCA.html" class="portal-link{' active' if active_page == 'bidyabari' else ''}"><i class="fa-solid fa-graduation-cap"></i> Biddabari-NTRCA (১৯তম)</a>
        <a href="Eminent-Petro-Bangla.html" class="portal-link{' active' if active_page == 'epb' else ''}"><i class="fa-solid fa-fire-flame-curved"></i> Eminent Petro Bangla</a>
        <a href="class 9-10-Computer-GK.html" class="portal-link{' active' if active_page == 'cgk' else ''}"><i class="fa-solid fa-desktop"></i> Class 9-10 Computer GK</a>
      </div>
      <div>
        <span style="opacity: 0.85;"><i class="fa-solid fa-file-circle-check"></i> {count_text}</span>
      </div>
    </div>
  </nav>
"""
    if '<nav class="portal-nav">' not in content:
        content = content.replace('<body class="show-explanations">', '<body class="show-explanations">\n\n' + nav_html)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {filename}')

update_file('Ict-wizard-NTRCA-313-and-325.html', 'ict', 'মোট ৫৯৪টি এমসিকিউ')
update_file('index.html', 'ict', 'মোট ৫৯৪টি এমসিকিউ')
update_file('class 9-10-Computer-GK.html', 'cgk', 'মোট ১,১৬৪টি এমসিকিউ')
