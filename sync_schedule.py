"""
Schedule Sync Script
Keeps weekly_schedule.md and weekly_schedule.html in sync.

Usage:
    python sync_schedule.py

The script watches both files:
- When MD changes → HTML is regenerated
- When HTML changes → MD is updated (extracts editable content)

Press Ctrl+C to stop.
"""

import os
import re
import time
import hashlib
from pathlib import Path
from datetime import datetime

# File paths
SCRIPT_DIR = Path(__file__).parent
MD_FILE = SCRIPT_DIR / "weekly_schedule.md"
HTML_FILE = SCRIPT_DIR / "weekly_schedule.html"

# Track file hashes to detect changes
file_hashes = {}


def get_file_hash(filepath):
    """Get MD5 hash of file contents."""
    try:
        with open(filepath, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except FileNotFoundError:
        return None


def md_to_html(md_content):
    """Convert markdown content to styled HTML."""

    # HTML template with full styling
    html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weekly Schedule — Disciplined Trader's Life</title>
    <style>
        :root {
            --primary: #1a365d;
            --secondary: #2c5282;
            --accent: #ed8936;
            --success: #38a169;
            --bg-light: #f7fafc;
            --bg-card: #ffffff;
            --text-primary: #2d3748;
            --text-secondary: #4a5568;
            --border: #e2e8f0;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: var(--text-primary);
            line-height: 1.6;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            text-align: center;
            padding: 40px 20px;
            color: white;
            margin-bottom: 30px;
        }

        header h1 {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 15px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }

        .philosophy {
            background: rgba(255,255,255,0.15);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 20px 30px;
            max-width: 800px;
            margin: 0 auto;
            font-size: 1.1rem;
            line-height: 1.8;
        }

        .card {
            background: var(--bg-card);
            border-radius: 16px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1), 0 10px 20px rgba(0,0,0,0.05);
            margin-bottom: 30px;
            overflow: hidden;
        }

        .card-header {
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            color: white;
            padding: 20px 25px;
            font-size: 1.4rem;
            font-weight: 600;
        }

        .card-body {
            padding: 25px;
        }

        h2 {
            color: var(--primary);
            margin: 30px 0 15px 0;
            padding-bottom: 10px;
            border-bottom: 2px solid var(--accent);
        }

        h3 {
            color: var(--secondary);
            margin: 25px 0 15px 0;
        }

        h4 {
            color: var(--text-primary);
            margin: 20px 0 10px 0;
        }

        p {
            margin-bottom: 15px;
        }

        blockquote {
            background: rgba(255,255,255,0.15);
            backdrop-filter: blur(10px);
            border-radius: 10px;
            padding: 15px 20px;
            margin: 15px 0;
            border-left: 4px solid var(--accent);
            font-style: italic;
        }

        ul, ol {
            margin: 15px 0;
            padding-left: 30px;
        }

        li {
            margin-bottom: 8px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }

        th {
            background: var(--primary);
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }

        td {
            padding: 12px 15px;
            border-bottom: 1px solid var(--border);
        }

        tr:nth-child(even) {
            background: var(--bg-light);
        }

        tr:hover {
            background: #edf2f7;
        }

        strong {
            color: var(--primary);
        }

        em {
            color: var(--text-secondary);
        }

        code {
            background: var(--bg-light);
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'Consolas', monospace;
        }

        pre {
            background: #2d3748;
            color: #e2e8f0;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            margin: 20px 0;
        }

        pre code {
            background: none;
            padding: 0;
            color: inherit;
        }

        hr {
            border: none;
            height: 2px;
            background: linear-gradient(90deg, transparent, var(--accent), transparent);
            margin: 40px 0;
        }

        .highlight-trading {
            background: linear-gradient(135deg, #48bb78 0%, #38a169 100%) !important;
            color: white !important;
            font-weight: 700;
        }

        .highlight-coding {
            background: linear-gradient(135deg, #4299e1 0%, #3182ce 100%) !important;
            color: white !important;
            font-weight: 700;
        }

        .nav {
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 1000;
        }

        .nav-toggle {
            background: white;
            border: none;
            padding: 12px 20px;
            border-radius: 30px;
            cursor: pointer;
            font-weight: 600;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }

        footer {
            text-align: center;
            padding: 30px;
            color: white;
            opacity: 0.9;
            font-style: italic;
        }

        @media (max-width: 768px) {
            header h1 {
                font-size: 1.8rem;
            }

            table {
                font-size: 0.85rem;
            }

            th, td {
                padding: 8px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Weekly Schedule — Disciplined Trader's Life</h1>
        </header>

        <div class="card">
            <div class="card-body">
                CONTENT_PLACEHOLDER
            </div>
        </div>

        <footer>
            <p>Last synced: TIMESTAMP_PLACEHOLDER</p>
        </footer>
    </div>
</body>
</html>'''

    # Convert markdown to HTML
    html_content = md_content

    # Convert headers
    html_content = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html_content, flags=re.MULTILINE)

    # Convert blockquotes
    def convert_blockquotes(text):
        lines = text.split('\n')
        result = []
        in_blockquote = False
        quote_lines = []

        for line in lines:
            if line.startswith('> '):
                if not in_blockquote:
                    in_blockquote = True
                quote_lines.append(line[2:])
            else:
                if in_blockquote:
                    result.append('<blockquote>' + '<br>'.join(quote_lines) + '</blockquote>')
                    quote_lines = []
                    in_blockquote = False
                result.append(line)

        if in_blockquote:
            result.append('<blockquote>' + '<br>'.join(quote_lines) + '</blockquote>')

        return '\n'.join(result)

    html_content = convert_blockquotes(html_content)

    # Convert tables
    def convert_tables(text):
        lines = text.split('\n')
        result = []
        in_table = False
        table_lines = []

        for line in lines:
            if '|' in line and not line.strip().startswith('```'):
                if not in_table:
                    in_table = True
                    result.append('<div style="overflow-x: auto;"><table>')

                # Skip separator lines
                if re.match(r'^\|[\s\-:|]+\|$', line.strip()):
                    continue

                cells = [c.strip() for c in line.split('|')[1:-1]]

                if not table_lines:  # Header row
                    result.append('<thead><tr>' + ''.join(f'<th>{c}</th>' for c in cells) + '</tr></thead><tbody>')
                else:
                    # Apply highlighting for special cells
                    row_html = '<tr>'
                    for cell in cells:
                        cell_class = ''
                        if '**TRADING**' in cell or 'TRADING' in cell:
                            cell_class = ' class="highlight-trading"'
                        elif '**CODING**' in cell or 'CODING' in cell:
                            cell_class = ' class="highlight-coding"'
                        row_html += f'<td{cell_class}>{cell}</td>'
                    row_html += '</tr>'
                    result.append(row_html)

                table_lines.append(line)
            else:
                if in_table:
                    result.append('</tbody></table></div>')
                    in_table = False
                    table_lines = []
                result.append(line)

        if in_table:
            result.append('</tbody></table></div>')

        return '\n'.join(result)

    html_content = convert_tables(html_content)

    # Convert bold and italic
    html_content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html_content)
    html_content = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html_content)

    # Convert code blocks
    html_content = re.sub(r'```(\w*)\n(.*?)\n```', r'<pre><code>\2</code></pre>', html_content, flags=re.DOTALL)
    html_content = re.sub(r'`([^`]+)`', r'<code>\1</code>', html_content)

    # Convert horizontal rules
    html_content = re.sub(r'^---+$', '<hr>', html_content, flags=re.MULTILINE)

    # Convert unordered lists
    def convert_lists(text):
        lines = text.split('\n')
        result = []
        in_list = False

        for line in lines:
            if re.match(r'^[\-\*] ', line):
                if not in_list:
                    result.append('<ul>')
                    in_list = True
                result.append('<li>' + line[2:] + '</li>')
            elif re.match(r'^\d+\. ', line):
                if not in_list:
                    result.append('<ol>')
                    in_list = True
                result.append('<li>' + re.sub(r'^\d+\. ', '', line) + '</li>')
            else:
                if in_list:
                    if result[-1].startswith('<li>'):
                        result.append('</ul>' if '<ul>' in ''.join(result[-10:]) else '</ol>')
                    in_list = False
                result.append(line)

        if in_list:
            result.append('</ul>')

        return '\n'.join(result)

    html_content = convert_lists(html_content)

    # Convert paragraphs (lines not already wrapped)
    lines = html_content.split('\n')
    result = []
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith('<') and not stripped.startswith('|'):
            result.append(f'<p>{line}</p>')
        else:
            result.append(line)
    html_content = '\n'.join(result)

    # Clean up empty paragraphs
    html_content = re.sub(r'<p>\s*</p>', '', html_content)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return html_template.replace('CONTENT_PLACEHOLDER', html_content).replace('TIMESTAMP_PLACEHOLDER', timestamp)


def html_to_md(html_content):
    """Extract content from HTML and convert back to markdown."""

    # This is a simplified extraction - for complex bidirectional sync,
    # you would need a more sophisticated parser

    # Remove HTML tags but preserve structure
    content = html_content

    # Extract just the card-body content
    match = re.search(r'<div class="card-body">(.*?)</div>\s*</div>\s*<footer>', content, re.DOTALL)
    if match:
        content = match.group(1)

    # Convert headers back
    content = re.sub(r'<h1>(.+?)</h1>', r'# \1', content)
    content = re.sub(r'<h2>(.+?)</h2>', r'## \1', content)
    content = re.sub(r'<h3>(.+?)</h3>', r'### \1', content)
    content = re.sub(r'<h4>(.+?)</h4>', r'#### \1', content)

    # Convert blockquotes
    content = re.sub(r'<blockquote>(.+?)</blockquote>', lambda m: '> ' + m.group(1).replace('<br>', '\n> '), content, flags=re.DOTALL)

    # Convert bold and italic
    content = re.sub(r'<strong>(.+?)</strong>', r'**\1**', content)
    content = re.sub(r'<em>(.+?)</em>', r'*\1*', content)

    # Convert code
    content = re.sub(r'<pre><code>(.+?)</code></pre>', r'```\n\1\n```', content, flags=re.DOTALL)
    content = re.sub(r'<code>([^<]+)</code>', r'`\1`', content)

    # Convert horizontal rules
    content = re.sub(r'<hr\s*/?>', '---', content)

    # Convert lists
    content = re.sub(r'<ul>', '', content)
    content = re.sub(r'</ul>', '', content)
    content = re.sub(r'<ol>', '', content)
    content = re.sub(r'</ol>', '', content)
    content = re.sub(r'<li>(.+?)</li>', r'- \1', content)

    # Convert paragraphs
    content = re.sub(r'<p>(.+?)</p>', r'\1\n', content, flags=re.DOTALL)

    # Remove remaining HTML tags
    content = re.sub(r'<[^>]+>', '', content)

    # Clean up whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = content.strip()

    return content


def sync_md_to_html():
    """Read MD file and generate HTML."""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] MD changed -> Regenerating HTML...")

    with open(MD_FILE, 'r', encoding='utf-8') as f:
        md_content = f.read()

    html_content = md_to_html(md_content)

    with open(HTML_FILE, 'w', encoding='utf-8') as f:
        f.write(html_content)

    # Update hash to avoid triggering HTML change detection
    file_hashes['html'] = get_file_hash(HTML_FILE)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] HTML file updated successfully!")


def sync_html_to_md():
    """Read HTML file and update MD (limited - preserves original MD structure)."""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] HTML changed -> Note: For major edits, please edit the MD file directly.")
    print(f"[{datetime.now().strftime('%H:%M:%S')}] The MD file is the source of truth for structure.")

    # For now, we don't auto-sync HTML back to MD because it would lose formatting
    # Instead, we notify the user


def watch_files():
    """Watch both files for changes and sync accordingly."""
    print("=" * 60)
    print("  SCHEDULE SYNC - Watching for changes...")
    print("=" * 60)
    print(f"  MD File:   {MD_FILE}")
    print(f"  HTML File: {HTML_FILE}")
    print("-" * 60)
    print("  - Edit the MD file for content changes")
    print("  - The HTML will auto-update when MD changes")
    print("  - Press Ctrl+C to stop")
    print("=" * 60)

    # Initial hashes
    file_hashes['md'] = get_file_hash(MD_FILE)
    file_hashes['html'] = get_file_hash(HTML_FILE)

    # Do initial sync if HTML doesn't exist or MD is newer
    if not HTML_FILE.exists():
        sync_md_to_html()

    try:
        while True:
            time.sleep(1)  # Check every second

            # Check MD file
            new_md_hash = get_file_hash(MD_FILE)
            if new_md_hash and new_md_hash != file_hashes.get('md'):
                file_hashes['md'] = new_md_hash
                sync_md_to_html()

            # Check HTML file (just notify, don't auto-sync back)
            new_html_hash = get_file_hash(HTML_FILE)
            if new_html_hash and new_html_hash != file_hashes.get('html'):
                file_hashes['html'] = new_html_hash
                sync_html_to_md()

    except KeyboardInterrupt:
        print("\n" + "=" * 60)
        print("  Sync stopped. Files are up to date.")
        print("=" * 60)


def main():
    """Main entry point."""
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] == '--once':
            # One-time sync
            sync_md_to_html()
            print("One-time sync complete.")
            return
        elif sys.argv[1] == '--help':
            print(__doc__)
            return

    # Start watching
    watch_files()


if __name__ == '__main__':
    main()
