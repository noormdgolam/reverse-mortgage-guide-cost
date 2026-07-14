import os
import json
import shutil
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import markdown
import yaml

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SRC_DIR)

TEMPLATES_DIR = os.path.join(SRC_DIR, "_templates")
DATA_DIR = os.path.join(SRC_DIR, "_data")
CONTENT_DIR = os.path.join(SRC_DIR, "_content")
ASSETS_DIR = os.path.join(SRC_DIR, "_assets")

env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

# Custom Jinja2 filter to format dates
def format_date(value, format="%B %d, %Y"):
    if not value:
        return ""
    try:
        dt = datetime.strptime(str(value), "%Y-%m-%d")
        return dt.strftime(format)
    except ValueError:
        return str(value)

env.filters['format_date'] = format_date

def parse_markdown_file(filepath):
    """Parses a markdown file with YAML frontmatter."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = yaml.safe_load(parts[1])
            md_content = parts[2]
            return frontmatter, markdown.markdown(md_content, extensions=['toc', 'tables', 'fenced_code'])
    
    return {}, markdown.markdown(content, extensions=['toc', 'tables', 'fenced_code'])

def inject_mid_article_ad(html_content):
    ad_html = '\n<div class="ad-slot" style="margin: 2rem 0;">\n    <!-- AdSense Mid Article -->\n    [ AdSense Ad Unit Placeholder - Mid Article ]\n</div>\n'
    parts = html_content.split('</h2>')
    if len(parts) > 2:
        return parts[0] + '</h2>' + parts[1] + '</h2>' + ad_html + '</h2>'.join(parts[2:])
    return html_content

def main():
    print("Starting static site generation...")
    
    # 1. Load Site Data
    with open(os.path.join(DATA_DIR, "site.json"), 'r', encoding='utf-8') as f:
        site_data = json.load(f)
        
    site_data['current_year'] = datetime.now().year

    # 2. Gather Articles
    articles = []
    articles_dir = os.path.join(CONTENT_DIR, "articles")
    if os.path.exists(articles_dir):
        for filename in os.listdir(articles_dir):
            if filename.endswith(".md"):
                filepath = os.path.join(articles_dir, filename)
                meta, html_content = parse_markdown_file(filepath)
                meta['slug'] = meta.get('slug', filename[:-3])
                meta['url'] = f"/{meta['slug']}.html"
                meta['content'] = inject_mid_article_ad(html_content)
                # default updated date
                if 'updated' not in meta:
                    meta['updated'] = meta.get('date', datetime.now().strftime("%Y-%m-%d"))
                articles.append(meta)

    # Sort articles by date descending
    articles.sort(key=lambda x: x.get('date', '1970-01-01'), reverse=True)

    # 3. Gather Pages
    pages = []
    pages_dir = os.path.join(CONTENT_DIR, "pages")
    if os.path.exists(pages_dir):
        for filename in os.listdir(pages_dir):
            if filename.endswith(".md"):
                filepath = os.path.join(pages_dir, filename)
                meta, html_content = parse_markdown_file(filepath)
                meta['slug'] = meta.get('slug', filename[:-3])
                meta['url'] = f"/{meta['slug']}.html"
                meta['content'] = html_content
                pages.append(meta)

    # 4. Generate Pages
    page_template = env.get_template('page.html')
    for page in pages:
        output_html = page_template.render(site=site_data, page=page, articles=articles)
        output_path = os.path.join(PROJECT_ROOT, f"{page['slug']}.html")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output_html)
        print(f"Generated: {page['url']}")

    # 5. Generate Articles
    article_template = env.get_template('article.html')
    for article in articles:
        # Determine related articles (same category, exclude self)
        related = [a for a in articles if a.get('category') == article.get('category') and a['slug'] != article['slug']][:3]
        
        output_html = article_template.render(site=site_data, article=article, related_articles=related)
        output_path = os.path.join(PROJECT_ROOT, f"{article['slug']}.html")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output_html)
        print(f"Generated: {article['url']}")

    # 6. Generate Index
    index_template = env.get_template('index.html')
    output_html = index_template.render(site=site_data, articles=articles)
    with open(os.path.join(PROJECT_ROOT, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(output_html)
    print("Generated: /index.html")
    
    # 7. Generate 404
    if os.path.exists(os.path.join(TEMPLATES_DIR, '404.html')):
        template_404 = env.get_template('404.html')
        output_html = template_404.render(site=site_data)
        with open(os.path.join(PROJECT_ROOT, '404.html'), 'w', encoding='utf-8') as f:
            f.write(output_html)
        print("Generated: /404.html")

    # 8. Copy Assets
    if os.path.exists(ASSETS_DIR):
        for item in os.listdir(ASSETS_DIR):
            s = os.path.join(ASSETS_DIR, item)
            d = os.path.join(PROJECT_ROOT, item)
            if os.path.isdir(s):
                if os.path.exists(d):
                    shutil.rmtree(d)
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)
        print("Copied assets to root.")

    # 9. Generate Sitemap
    sitemap_template = env.get_template('sitemap.xml')
    sitemap_xml = sitemap_template.render(site=site_data, articles=articles, pages=pages)
    with open(os.path.join(PROJECT_ROOT, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(sitemap_xml)
    print("Generated: /sitemap.xml")

    # 10. Generate RSS
    rss_template = env.get_template('rss.xml')
    rss_xml = rss_template.render(site=site_data, articles=articles)
    with open(os.path.join(PROJECT_ROOT, 'rss.xml'), 'w', encoding='utf-8') as f:
        f.write(rss_xml)
    print("Generated: /rss.xml")

    # 11. Generate Search Index and Page
    search_index = []
    for article in articles:
        search_index.append({
            'title': article.get('title', ''),
            'description': article.get('description', ''),
            'url': article.get('url', ''),
            'category': article.get('category', '')
        })
    with open(os.path.join(PROJECT_ROOT, 'search_index.json'), 'w', encoding='utf-8') as f:
        json.dump(search_index, f, separators=(',', ':'))
    print("Generated: /search_index.json")

    if os.path.exists(os.path.join(TEMPLATES_DIR, 'search.html')):
        search_template = env.get_template('search.html')
        output_html = search_template.render(site=site_data)
        os.makedirs(os.path.join(PROJECT_ROOT, 'search'), exist_ok=True)
        with open(os.path.join(PROJECT_ROOT, 'search', 'index.html'), 'w', encoding='utf-8') as f:
            f.write(output_html)
        print("Generated: /search/index.html")

    print("Site generation complete!")

if __name__ == "__main__":
    main()
