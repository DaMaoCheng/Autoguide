"""Check local document navigation, package completeness and public-only boundaries."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'autoguide'
EXPECTED = {
    'index', 'shared-preparation', 'shared-research', 'shared-changes',
    'project-initiation', 'project-work-breakdown', 'project-design',
    'project-node-design', 'project-execution', 'feature-initiation',
    'feature-work-breakdown', 'feature-design', 'feature-node-design',
    'feature-execution', 'installation',
}
LINK = re.compile(r'!?\[[^\]\n]*\]\(([^\n)]+)\)')
PRIVATE_LINK = re.compile(r'https?://[\w.-]+\.feishu\.cn/(?:wiki|docx)/[A-Za-z0-9]+')
PRIVATE_ID = re.compile(r'\b(?:ou|oc)_[a-f0-9]{20,}\b|\bdoxcn[A-Za-z0-9]{15,}\b')
CJK_TEXT = re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]')

def outside_fences(text):
    lines, fence = [], None
    for line in text.splitlines():
        match = re.match(r'^\s*(`{3,}|~{3,})', line)
        if match:
            marker = match.group(1)[0]
            if fence is None:
                fence = marker
            elif marker == fence:
                fence = None
            continue
        if fence is None:
            lines.append(line)
    if fence is not None:
        raise ValueError('Unclosed code fence')
    return '\n'.join(lines)

def anchors(path):
    used, result = {}, set()
    for line in outside_fences(path.read_text(encoding='utf-8')).splitlines():
        match = re.match(r'^#{1,6}\s+(.+?)\s*#*$', line)
        if not match:
            continue
        value = re.sub(r'[\[\]`*_~]', '', match.group(1)).lower()
        value = ''.join(char for char in value if char.isalnum() or char in ' -_')
        value = value.replace(' ', '-')
        count = used.get(value, 0)
        used[value] = count + 1
        result.add(value if count == 0 else value + '-' + str(count))
    return result

def check(require_license=False):
    errors, checked = [], 0
    docs = [path for path in ROOT.rglob('*.md') if 'dist' not in path.relative_to(ROOT).parts and '.git' not in path.relative_to(ROOT).parts]
    observed = {path.stem for path in (SKILL / 'references').glob('*.md')}
    if observed != EXPECTED:
        errors.append('Rule documents missing or unexpected: ' + str(observed ^ EXPECTED))
    version = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
    skill_text = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
    if not re.search(r'^\s+version:\s*[\"\']' + re.escape(version) + r'[\"\']\s*$', skill_text, re.M):
        errors.append('VERSION does not match Skill metadata')
    for path in docs:
        raw = path.read_text(encoding='utf-8')
        if CJK_TEXT.search(raw):
            errors.append(str(path.relative_to(ROOT)) + ': untranslated CJK text remains')
        if 'work-automation-guide' in raw:
            errors.append(str(path.relative_to(ROOT)) + ': obsolete Skill name remains')
        if PRIVATE_LINK.search(raw) or PRIVATE_ID.search(raw):
            errors.append(str(path.relative_to(ROOT)) + ': internal link or identity marker')
        if re.search(r'<(?:title|source|whiteboard|cite)\b', raw):
            errors.append(str(path.relative_to(ROOT)) + ': unconverted private document markup')
        try:
            text = outside_fences(raw)
        except ValueError as error:
            errors.append(str(path.relative_to(ROOT)) + ': ' + str(error))
            continue
        for match in LINK.finditer(text):
            destination = match.group(1).strip().split(' "', 1)[0].strip('<>')
            parsed = urlsplit(destination)
            if parsed.scheme or parsed.netloc:
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path.resolve()
            checked += 1
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(str(path.relative_to(ROOT)) + ': link escapes public repository: ' + destination)
                continue
            if not target.exists():
                errors.append(str(path.relative_to(ROOT)) + ': missing link: ' + destination)
            elif parsed.fragment and target.suffix == '.md' and unquote(parsed.fragment) not in anchors(target):
                errors.append(str(path.relative_to(ROOT)) + ': missing heading anchor: ' + destination)
    for path in (SKILL / 'agents').glob('*.yaml'):
        raw = path.read_text(encoding='utf-8')
        if CJK_TEXT.search(raw) or 'work-automation-guide' in raw or PRIVATE_LINK.search(raw) or PRIVATE_ID.search(raw):
            errors.append(str(path.relative_to(ROOT)) + ': untranslated, obsolete, or private metadata')
    if require_license and not (ROOT / 'LICENSE').is_file():
        errors.append('Choose and add LICENSE before publishing a release')
    if errors:
        for error in errors:
            print('ERROR:', error, file=sys.stderr)
        return False
    print('Verified', len(docs), 'Markdown files;', checked, 'local links; 15 rule documents; version', version)
    if not (ROOT / 'LICENSE').exists():
        print('Publication prerequisite: license and author attribution are not yet selected.')
    return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--release', action='store_true', help='Also require a selected LICENSE before public release')
    args = parser.parse_args()
    raise SystemExit(0 if check(args.release) else 1)
