"""Transcribe the Master Filmmaker course videos locally with Whisper (GPU).

Run on the account owner's own computer, never in the cloud. Reads the course manifest
(made in the browser, kept OUT of this repo) and writes one .txt per lesson to
~/eric-course-transcripts, which is outside the repo. Transcripts are research material
only and must never be committed (AGENTS.md rule 1). Re-running skips finished lessons.

  python transcribe_course.py
"""
import csv, os, re, subprocess, site, glob, pathlib
HOME = pathlib.Path.home()
MANIFEST = HOME / 'Downloads' / 'eric-course-manifest.tsv'
OUT = HOME / 'eric-course-transcripts'
AUDIO = OUT / '_audio'
YTDLP = str(HOME / 'AppData/Local/Microsoft/WinGet/Packages/yt-dlp.yt-dlp_Microsoft.Winget.Source_8wekyb3d8bbwe/yt-dlp.exe')
if not os.path.exists(YTDLP):
    YTDLP = 'yt-dlp'
FIRST = ['Overcoming Objections Mastery', 'Discovery Call Workflow', 'Onboarding and Client Management', 'Facebook Ads Course']

# Make the graphics-card libraries installed by pip visible to Whisper.
for sp in site.getsitepackages() + [site.getusersitepackages()]:
    for d in glob.glob(os.path.join(sp, 'nvidia', '*', 'bin')):
        os.environ['PATH'] = d + os.pathsep + os.environ['PATH']
        os.add_dll_directory(d)
from faster_whisper import WhisperModel

# faster-whisper 1.2 passes metadata_errors= to av.open(); PyAV 15+ removed that option.
# Drop it so newer PyAV can be used without building an old version from source.
import av
_av_open = av.open
def _av_open_compat(*args, **kwargs):
    kwargs.pop('metadata_errors', None)
    return _av_open(*args, **kwargs)
av.open = _av_open_compat

rows = list(csv.DictReader(open(MANIFEST, encoding='utf-8-sig'), delimiter='\t'))
items = []
for n, r in enumerate(rows, 1):
    for vid in (r.get('wistia_ids') or '').split():
        items.append((n, r['section'], r['lesson'], vid))
def prio(it):
    for i, p in enumerate(FIRST):
        if it[1].startswith(p):
            return (i, it[0])
    return (len(FIRST), it[0])
items.sort(key=prio)

OUT.mkdir(exist_ok=True)
AUDIO.mkdir(exist_ok=True)
model = WhisperModel('large-v3-turbo', device='cuda', compute_type='float16')
safe = lambda s: re.sub(r'[^A-Za-z0-9 _.-]+', '', s).strip()[:60]
failed = []
for k, (n, sec, les, vid) in enumerate(items, 1):
    txt = OUT / f'{n:03d} - {safe(sec)} - {safe(les)} - {vid}.txt'
    if txt.exists():
        continue
    print(f'[{k}/{len(items)}] {sec} / {les}', flush=True)
    for f in AUDIO.glob(vid + '.*'):
        f.unlink()
    r = subprocess.run([YTDLP, '-q', '--no-warnings', '-f', 'ba/w', '--sleep-requests', '2',
                        '-o', str(AUDIO / f'{vid}.%(ext)s'), f'https://fast.wistia.net/embed/iframe/{vid}'])
    files = [f for f in AUDIO.glob(vid + '.*') if not f.name.endswith('.part')]
    if r.returncode or not files:
        failed.append(vid)
        print('  download failed')
        continue
    try:
        segs, info = model.transcribe(str(files[0]), language='en', vad_filter=True)
        text = '\n'.join(s.text.strip() for s in segs)
        txt.write_text(f'# {sec} / {les}\n# wistia {vid} - {info.duration:.0f}s\n\n{text}\n', encoding='utf-8')
    except Exception as e:
        failed.append(vid)
        print('  transcribe failed:', e)
    finally:
        for f in files:
            f.unlink(missing_ok=True)
print('Done:', len(items) - len(failed), 'ok,', len(failed), 'failed:', ' '.join(failed))
