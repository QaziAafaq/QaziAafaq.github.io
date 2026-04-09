import glob
import os

folder = r'c:\Users\it\OneDrive\Desktop\CV\FolioOne'
html_files = glob.glob(os.path.join(folder, '*.html'))

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements for header-social-links
    content = content.replace('<a href="#" class="github">', '<a href="https://github.com/QaziAafaq" target="_blank" class="github">')
    content = content.replace('<a href="#" class="linkedin">', '<a href="https://www.linkedin.com/in/qazi-muhammad-aafaq-a581773a0" target="_blank" class="linkedin">')

    # Replacements for footer/hero social-links
    content = content.replace('<a href="#"><i class="bi bi-github"></i></a>', '<a href="https://github.com/QaziAafaq" target="_blank"><i class="bi bi-github"></i></a>')
    content = content.replace('<a href="#"><i class="bi bi-linkedin"></i></a>', '<a href="https://www.linkedin.com/in/qazi-muhammad-aafaq-a581773a0" target="_blank"><i class="bi bi-linkedin"></i></a>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f'Updated {len(html_files)} files.')
