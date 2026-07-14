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
        
    import random
    
    spin_intros = [
        "<p>For many seniors, unlocking the equity in their homes is a powerful way to secure financial stability in retirement. In this comprehensive guide, we'll break down the specific rules and regulations that govern reverse mortgages in your area.</p>",
        "<p>Navigating the complex landscape of reverse mortgages can feel overwhelming. However, by understanding the localized laws and eligibility criteria, you can make an informed decision that protects your family's future.</p>",
        "<p>A reverse mortgage is not a one-size-fits-all solution. Depending on your home's value, your age, and local property laws, the benefits can vary drastically. Let's explore exactly what you need to know.</p>"
    ]
    
    spin_factors = [
        "<h3>Crucial Eligibility Factors</h3><ul><li><strong>Age Requirement:</strong> You typically must be at least 62 years old to qualify.</li><li><strong>Home Equity:</strong> You must own your home outright or have a significant amount of equity built up.</li><li><strong>Property Taxes & Insurance:</strong> Borrowers are still entirely responsible for ongoing property taxes, homeowners insurance, and general maintenance.</li></ul>",
        "<h3>How Your Loan Limit is Calculated</h3><p>Your maximum borrowing limit depends on the youngest borrower's age, the current interest rate, and the appraised value of your home (or the FHA lending limit, whichever is lower).</p>",
        "<h3>Counseling Requirements</h3><p>Before closing on a Home Equity Conversion Mortgage (HECM), you are required by law to attend an independent, HUD-approved counseling session to ensure you fully understand the loan's implications.</p>"
    ]
    
    spin_faqs = [
        "<h3>Frequently Asked Questions</h3><h4>Can the bank take my home?</h4><p>No. A reverse mortgage is a non-recourse loan. The lender cannot force you out of your home as long as you continue to pay property taxes, insurance, and maintain the home.</p>",
        "<h3>Frequently Asked Questions</h3><h4>What happens when I pass away?</h4><p>When the last surviving borrower permanently leaves the home, the loan becomes due. Your heirs can choose to sell the home to repay the loan, or refinance the home if they wish to keep it.</p>",
        "<h3>Frequently Asked Questions</h3><h4>Will a reverse mortgage affect my Social Security?</h4><p>Generally, reverse mortgage proceeds are considered loan advances, not income. Therefore, they typically do not affect regular Social Security or Medicare benefits (though they may impact needs-based programs like Medicaid).</p>"
    ]

    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = yaml.safe_load(parts[1])
            md_content = parts[2]
            raw_html = markdown.markdown(md_content, extensions=['toc', 'tables', 'fenced_code'])
            injected_content = random.choice(spin_intros) + raw_html + random.choice(spin_factors) + random.choice(spin_faqs)
            return frontmatter, injected_content
    
    raw_html = markdown.markdown(content, extensions=['toc', 'tables', 'fenced_code'])
    injected_content = random.choice(spin_intros) + raw_html + random.choice(spin_factors) + random.choice(spin_faqs)
    return {}, injected_content

def inject_inline_components(html_content):
    ad_html = '\n<div class="ad-slot" style="margin: 2rem 0;">\n    <!-- AdSense Mid Article -->\n    [ AdSense Ad Unit Placeholder - Mid Article ]\n</div>\n'
    newsletter_html = '\n<div class="inline-newsletter" style="margin: 2rem 0; padding: 1.5rem; background: #f0f7ff; border-left: 4px solid var(--primary-color); border-radius: 4px;">\n    <h3 style="margin-top: 0;">Stay Informed</h3>\n    <p style="font-size: 0.95rem;">Join thousands of seniors getting our free weekly reverse mortgage tips.</p>\n    <form style="display: flex; gap: 0.5rem;" onsubmit="event.preventDefault(); alert(\'Subscribed! (Placeholder)\');">\n        <input type="email" placeholder="Email address" required style="flex: 1; padding: 0.5rem; border: 1px solid #ccc; border-radius: 4px;">\n        <button type="submit" style="padding: 0.5rem 1rem; background: var(--primary-color); color: white; border: none; border-radius: 4px; cursor: pointer;">Subscribe</button>\n    </form>\n</div>\n'
    
    parts = html_content.split('</h2>')
    if len(parts) > 3:
        # Inject ad after 1st H2, newsletter after 2nd H2
        return parts[0] + '</h2>' + ad_html + parts[1] + '</h2>' + newsletter_html + '</h2>'.join(parts[2:])
    elif len(parts) > 2:
        # Just inject ad after 1st H2 if only 2 H2s exist
        return parts[0] + '</h2>' + ad_html + '</h2>'.join(parts[1:])
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
                meta['content'] = inject_inline_components(html_content)
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

    # Generate HTML Sitemap
    if os.path.exists(os.path.join(TEMPLATES_DIR, 'html_sitemap.html')):
        html_sitemap_template = env.get_template('html_sitemap.html')
        output_html_sitemap = html_sitemap_template.render(site=site_data, articles=articles)
        with open(os.path.join(PROJECT_ROOT, 'sitemap.html'), 'w', encoding='utf-8') as f:
            f.write(output_html_sitemap)
        print("Generated: /sitemap.html")

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
