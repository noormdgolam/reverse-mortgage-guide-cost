# Reverse Mortgage Guide - Documentation

This repository contains the source code and static site generator for the **Reverse Mortgage Guide** website.

## Architecture

This is a custom, ultra-fast Python static site generator designed specifically for SEO performance and Google AdSense compliance. It does not use heavy frameworks (like Next.js or Nuxt), ensuring minimal JavaScript payload, maximum Core Web Vitals scores, and easy Git-based deployment.

- **`_src/`**: Contains the site generator, data, raw markdown content, and Jinja2 templates.
- **Root Directory**: Contains the generated HTML, CSS, JS, `sitemap.xml`, and `rss.xml`. Your cPanel is configured to serve directly from this root directory.

## Deployment

Deployment is handled purely through Git. **Do not create a `.cpanel.yml` file.**

To deploy new changes to the live site:
1. Make your changes in the `_src` directory.
2. Run the site generator: `python _src/generate_site.py`
3. Commit all changes (including the generated HTML in the root).
4. Push to the main branch: `git push origin main`

cPanel Git Version Control will automatically detect the push and serve the updated files.

## Adding New Content

To maintain AdSense compliance, **never batch-generate hundreds of identical articles.**

1. Create a new python script (e.g., `seed_batch_3.py`) to generate a new batch of 10-15 unique, high-quality markdown files into `_src/_content/articles/`.
2. Ensure each article has proper YAML frontmatter (`title`, `description`, `slug`, `category`, `date`, `takeaways`).
3. Run `python _src/generate_site.py` to compile the new articles.

## Connecting Services

### Google AdSense
Currently, AdSense placeholders are marked in `_src/_templates/base.html` and injected via `_src/generate_site.py`.
- **Global Script:** Replace the `ca-pub-0000000000000000` client ID in `_src/_data/site.json` with your real Publisher ID.
- **Ad Slots:** To insert real ad units, open `_src/generate_site.py` and replace `[ AdSense Ad Unit Placeholder - Mid Article ]` with your real `<ins class="adsbygoogle"...>` code snippet.

### Newsletter Form
The newsletter opt-in forms are located in two places:
1. **Footer:** Open `_src/_templates/base.html`
2. **Inline (Mid-Article):** Open `_src/generate_site.py`
Change the `<form onsubmit="...">` `action` attribute to point to your email provider (e.g., Mailchimp, ConvertKit, MailerLite endpoint).

### Google Analytics
Replace the `G-XXXXXXXXXX` measurement ID in `_src/_data/site.json` with your real GA4 ID.
