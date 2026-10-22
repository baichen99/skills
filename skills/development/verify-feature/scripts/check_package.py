#!/usr/bin/env python3
"""Check this skill's metadata, published references, and SVG assets (stdlib only)."""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit

from check_report_links import anchors, links


def main():
    root = Path(__file__).resolve().parents[1]
    errors = []
    text = (root / 'SKILL.md').read_text(encoding='utf-8')
    frontmatter = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    fields = dict(re.findall(r'^(name|description|license): (.+)$', frontmatter[1], re.M)) if frontmatter else {}
    if fields.get('name') != root.name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', fields.get('name', '')):
        errors.append('Skill name must be valid and match its directory')
    if not 1 <= len(fields.get('description', '')) <= 1024:
        errors.append('Description must contain 1–1024 characters')
    if fields.get('license') != 'MIT' or not (root / 'LICENSE').is_file():
        errors.append('Missing or inconsistent skill license')
    documents = list(root.glob('*.md')) + list((root / 'references').glob('*.md')) + list((root / 'docs').glob('*.md'))
    for document in documents:
        body = document.read_text(encoding='utf-8')
        destinations = links(body) + re.findall(r'<(?:img|a)\b[^>]*?(?:src|href)="([^"]+)"', body)
        for destination in destinations:
            target = urlsplit(destination)
            if target.scheme in ('http', 'https', 'mailto'):
                continue
            path = document.parent / unquote(target.path) if target.path else document
            if target.scheme or target.netloc or not path.is_file():
                errors.append(str(document.relative_to(root)) + ': unresolved link ' + destination)
            elif target.fragment and path.suffix == '.md' and unquote(target.fragment) not in anchors(path.read_text(encoding='utf-8')):
                errors.append(str(document.relative_to(root)) + ': missing anchor ' + destination)
    for svg in root.rglob('*.svg'):
        try:
            ET.parse(svg)
        except ET.ParseError as error:
            errors.append(str(svg.relative_to(root)) + ': ' + str(error))
    for error in errors:
        print('FAIL ' + error)
    if not errors:
        print('Package metadata, local document links, and SVG XML passed.')
    return int(bool(errors))


if __name__ == '__main__':
    sys.exit(main())
