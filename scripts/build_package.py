"""Build a standalone Skill ZIP from public files, without internal source backups."""
from pathlib import Path
import argparse
import importlib.util
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'autoguide'

def build(require_license=False):
    spec = importlib.util.spec_from_file_location('guide_checks', ROOT / 'scripts' / 'check_links.py')
    checks = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checks)
    if not checks.check(require_license):
        raise SystemExit(1)
    version = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
    files = sorted(path for path in SKILL.rglob('*') if path.is_file())
    assert {path.suffix for path in files} <= {'.md', '.yaml'}, 'Unexpected file type in Skill package'
    entries = [(path, Path('autoguide') / path.relative_to(SKILL)) for path in files]
    if (ROOT / 'LICENSE').exists():
        entries.append((ROOT / 'LICENSE', Path('autoguide/LICENSE')))
    output = ROOT / 'dist'
    output.mkdir(exist_ok=True)
    archive_path = output / ('autoguide-v' + version + '.zip')
    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as archive:
        for path, relative in entries:
            archive.write(path, str(relative))
    with zipfile.ZipFile(archive_path) as archive:
        assert archive.testzip() is None
        assert set(archive.namelist()) == {str(relative) for _, relative in entries}
        for path, relative in entries:
            assert archive.read(str(relative)) == path.read_bytes(), relative
        for relative in archive.namelist():
            assert not relative.startswith('/') and '..' not in Path(relative).parts
    (output / 'package-files.json').write_text(json.dumps({'version': version, 'files': [str(relative) for _, relative in entries], 'license_included': (ROOT / 'LICENSE').exists()}, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Built and verified:', archive_path)
    return archive_path

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--release', action='store_true', help='Require a selected LICENSE for the distributable release')
    args = parser.parse_args()
    build(args.release)
