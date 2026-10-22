#!/usr/bin/env python3
"""Check local Markdown links and heading anchors; remote links need separate verification."""
import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


def without_fences(text):
    output = []
    fence = None
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}(" + chr(96) + r"{3,}|~{3,})", line)
        if match:
            marker = match[1]
            if fence is None:
                fence = marker
                output.append("")
                continue
            if marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
                output.append("")
                continue
        output.append("" if fence else line)
    return "\n".join(output)


def anchors(text):
    result = set()
    counts = {}
    clean = without_fences(text)
    for match in re.finditer(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", clean, re.M):
        title = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", match[1])
        slug = re.sub(r"[^\w\s-]", "", title.lower())
        slug = re.sub(r"\s", "-", slug.strip())
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(slug if count == 0 else slug + "-" + str(count))
    result.update(re.findall(r'<a\s+[^>]*(?:id|name)=["\x27]([^"\x27]+)', clean, re.I))
    return result


def links(text):
    clean = without_fences(text)
    # Inline code often demonstrates links that should not be followed.
    clean = re.sub(r"(`+)(.*?)\1(?!`)", "", clean, flags=re.S)
    # Destinations with spaces use CommonMark angle brackets.
    destination = r'(<[^>\n]+>|[^\s)]+)(?:\s+(?:"[^"\n]*"|' + "'" + r"[^'\n]*'" + r'))?'
    found = []
    for match in re.finditer(r'!?\[[^\]\n]*\]\(\s*', clean):
        start = match.end()
        if start >= len(clean):
            continue
        if clean[start] == "<":
            end = clean.find(">", start + 1)
            if end != -1:
                found.append(clean[start + 1:end])
            continue
        # Bare destinations can contain balanced or escaped parentheses.
        cursor, depth, value = start, 0, []
        while cursor < len(clean):
            char = clean[cursor]
            if char == "\\" and cursor + 1 < len(clean):
                value.append(clean[cursor + 1])
                cursor += 2
                continue
            if char.isspace() or (char == ")" and depth == 0):
                break
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
            value.append(char)
            cursor += 1
        if value:
            found.append("".join(value))
    definitions = {
        match[1].strip().lower(): match[2].strip("<>")
        for match in re.finditer(r'^\s{0,3}\[([^\]]+)\]:\s*' + destination + r'\s*$', clean, re.M)
    }
    for match in re.finditer(r'!?\[([^\]\n]+)\]\[([^\]\n]*)\]', clean):
        key = (match[2] or match[1]).strip().lower()
        found.append(definitions.get(key, "missing-reference:" + key))
    return found


def check(report):
    errors = []
    remote = []
    checked = 0
    targets = links(report.read_text(encoding="utf-8"))
    if not targets:
        errors.append("No evidence/source links found")
    for target in targets:
        parsed = urlsplit(target)
        if parsed.scheme in ("http", "https", "mailto"):
            remote.append(target)
            continue
        if parsed.scheme or parsed.netloc:
            errors.append("Unsupported or undefined link: " + target)
            continue
        path = report.parent / unquote(parsed.path) if parsed.path else report
        if not path.is_file():
            errors.append("Missing file: " + target)
            continue
        if parsed.fragment and path.suffix.lower() in (".md", ".markdown"):
            fragment = unquote(parsed.fragment)
            if fragment not in anchors(path.read_text(encoding="utf-8")):
                errors.append("Missing Markdown anchor: " + target)
                continue
        checked += 1
    for error in errors:
        print("FAIL " + error)
    print("Local links checked: " + str(checked))
    print("Remote links not checked: " + str(len(remote)))
    if errors:
        return 1
    print("Local link check passed; this does not validate test results or remote access.")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    if not args.report.is_file():
        parser.error("Report must be an existing Markdown file")
    return check(args.report.resolve())


if __name__ == "__main__":
    sys.exit(main())
