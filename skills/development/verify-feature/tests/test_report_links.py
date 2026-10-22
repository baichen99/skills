import contextlib
import io
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from check_report_links import anchors, check, links


class ReportLinksTest(unittest.TestCase):
    def run_report(self, body, files=None):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            report = root / 'report.md'
            report.write_text(body, encoding='utf-8')
            for name, content in (files or {}).items():
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content, encoding='utf-8')
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                status = check(report)
            return status, output.getvalue()

    def test_relative_evidence_and_encoded_spaces(self):
        status, _ = self.run_report(
            '![Screenshot](evidence/screen%20one.png) [Log](<log one.txt>)',
            {'evidence/screen one.png': 'image fixture', 'log one.txt': 'ok'},
        )
        self.assertEqual(status, 0)

    def test_missing_evidence_fails(self):
        status, output = self.run_report('[Screenshot](missing.png)')
        self.assertEqual(status, 1)
        self.assertIn('Missing file: missing.png', output)

    def test_missing_anchor_fails(self):
        status, output = self.run_report('[Case](case.md#missing)', {'case.md': '# Actual'})
        self.assertEqual(status, 1)
        self.assertIn('Missing Markdown anchor', output)

    def test_same_document_and_duplicate_heading_anchors(self):
        body = '# Result\n# Result\n[First](#result) [Second](#result-1)'
        self.assertEqual(self.run_report(body)[0], 0)

    def test_unicode_and_explicit_anchors(self):
        body = '# 验证结果\n<a id="custom"></a>\n[结果](#%E9%AA%8C%E8%AF%81%E7%BB%93%E6%9E%9C) [Custom](#custom)'
        self.assertEqual(self.run_report(body)[0], 0)

    def test_reference_links(self):
        body = '[log][output]\n![screen][]\n\n[output]: log.txt\n[screen]: screen.png'
        self.assertEqual(self.run_report(body, {'log.txt': 'ok', 'screen.png': 'image fixture'})[0], 0)

    def test_undefined_reference_fails(self):
        status, output = self.run_report('[Log][unknown]')
        self.assertEqual(status, 1)
        self.assertIn('Unsupported or undefined link', output)

    def test_code_examples_are_ignored(self):
        body = '```md\n[bad](missing.md)\n```\n~~~\n[bad](other.md)\n~~~\n`[bad](third.md)`\n[good](log.txt)'
        self.assertEqual(self.run_report(body, {'log.txt': 'ok'})[0], 0)

    def test_parentheses_in_path(self):
        self.assertEqual(self.run_report('[Trace](trace(1).txt)', {'trace(1).txt': 'ok'})[0], 0)

    def test_remote_links_are_reported_unchecked(self):
        status, output = self.run_report('[Source](https://example.invalid/evidence)')
        self.assertEqual(status, 0)
        self.assertIn('Remote links not checked: 1', output)
        self.assertIn('Local links checked: 0', output)

    def test_empty_report_fails(self):
        self.assertEqual(self.run_report('Nothing attached')[0], 1)

    def test_fenced_headings_are_not_anchors(self):
        self.assertEqual(anchors('# Actual\n```md\n# Fake\n```'), {'actual'})

    def test_escaped_parentheses(self):
        self.assertEqual(links(r'[Trace](trace\(1\).txt)'), ['trace(1).txt'])


class PackageCheckTest(unittest.TestCase):
    def test_package_check_from_another_working_directory(self):
        script = Path(__file__).resolve().parents[1] / 'scripts/check_package.py'
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run([sys.executable, str(script)], cwd=directory, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_package_check_rejects_broken_published_reference(self):
        source = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / source.name
            shutil.copytree(source, root, ignore=shutil.ignore_patterns('__pycache__'))
            with (root / 'README.md').open('a', encoding='utf-8') as document:
                document.write('\n[Missing evidence](does-not-exist.png)\n')
            result = subprocess.run([sys.executable, str(root / 'scripts/check_package.py')], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('unresolved link does-not-exist.png', result.stdout)


if __name__ == '__main__':
    unittest.main()
