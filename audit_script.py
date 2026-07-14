import os
import re
from collections import defaultdict

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
valid_urls = set(['/', '/index.html', 'index.html', ''])
for f in html_files:
    valid_urls.add('/' + f)
    valid_urls.add(f)
    if f.endswith('index.html'):
        valid_urls.add('/' + os.path.dirname(f))
valid_urls.add('/search/index.html')

broken_links = defaultdict(list)
missing_titles = []
missing_descriptions = []

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # Check SEO
        if not re.search(r'<title>.*?</title>', content, re.IGNORECASE | re.DOTALL):
            missing_titles.append(f)
        if not re.search(r'<meta\s+name=[\"\'\']description[\"\'\']\s+content=[\"\'\'].*?[\"\'\']', content, re.IGNORECASE):
            missing_descriptions.append(f)
            
        # Check Links
        links = re.findall(r'<a\s+[^>]*href=[\"\'](.*?)[\"\']', content, re.IGNORECASE)
        for link in links:
            if link.startswith('http') or link.startswith('mailto:') or link.startswith('#'):
                continue
            
            # Remove query params or hash for internal links check
            clean_link = link.split('#')[0].split('?')[0]
            
            if clean_link not in valid_urls and clean_link != "":
                broken_links[f].append(link)

print('--- SEO AUDIT ---')
print(f'Total HTML pages scanned: {len(html_files)}')
print(f'Pages missing <title>: {len(missing_titles)}')
print(f'Pages missing meta description: {len(missing_descriptions)}')
if missing_descriptions:
    print('Sample missing descriptions:', missing_descriptions[:5])

print('\\n--- LINK AUDIT ---')
total_broken = sum(len(links) for links in broken_links.values())
print(f'Total broken internal links found: {total_broken}')
if total_broken > 0:
    for page, links in list(broken_links.items())[:5]:
        print(f'On page {page}: {links}')

print('\\n--- SITEMAP & ROBOTS ---')
print('sitemap.xml exists:', os.path.exists('sitemap.xml'))
print('robots.txt exists:', os.path.exists('robots.txt'))
