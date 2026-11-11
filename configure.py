#!/usr/bin/env python3
"""Make human.txt portable to your own public website, keeping the source intact."""
import argparse
from pathlib import Path
from urllib.parse import urlsplit

root = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description='Set the public URL used for re-reading Human Scope.')
parser.add_argument('url', help='Published site URL, e.g. https://name.github.io/human-scope-site/')
args = parser.parse_args()
url = args.url.rstrip('/')
parts = urlsplit(url)
if parts.scheme != 'https' or not parts.netloc or parts.query or parts.fragment:
    parser.error('Provide a full HTTPS site URL without query or fragment.')
source = (root / 'human-original.txt').read_text(encoding='utf-8')
text = source.replace('https://truespaceai.ru/human.txt', url + '/human.txt')
text = text.replace('https://truespaceai.ru/human', url + '/')
(root / 'human.txt').write_text(text, encoding='utf-8')
assert text.count('CHECKPOINT 1 of 4.') == 1
assert text.count('CHECKPOINT 2 of 4.') == 1
assert text.count('CHECKPOINT 3 of 4.') == 1
assert text.count('CHECKPOINT 4 of 4.') == 1
assert text.endswith('Then wait for the writing task.\n')
print('Configured human.txt:', url + '/human.txt')
