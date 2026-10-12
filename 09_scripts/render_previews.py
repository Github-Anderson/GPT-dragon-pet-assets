"""Render motion evidence from the exact final encoded atlas."""
from pathlib import Path
import importlib.util
import json
import subprocess
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / '09_scripts/pipeline'
spec = importlib.util.spec_from_file_location('bundled_preview', SKILL / 'render_animation_previews.py')
preview = importlib.util.module_from_spec(spec)
spec.loader.exec_module(preview)
atlas = Image.open(ROOT / '02_final/spritesheet-extended.png').convert('RGBA')
out = ROOT / '03_previews'
frames_root = out / 'encoded-frames'
for row, (state, durations) in enumerate(preview.ROW_DURATIONS.items()):
    folder = frames_root / state
    folder.mkdir(parents=True, exist_ok=True)
    for col in range(len(durations)):
        atlas.crop((col*192,row*208,(col+1)*192,(row+1)*208)).save(folder/f'{col:02}.png')
subprocess.run(['python3', str(SKILL/'render_animation_previews.py'), '--frames-root', str(frames_root), '--output-dir', str(out)], check=True)

def card(frame, label):
    canvas = Image.new('RGB',(320,260),'#f3f0fa')
    canvas.paste(frame,((320-192)//2,20),frame)
    ImageDraw.Draw(canvas).text((12,236),label,fill='#32264d')
    return canvas

all_frames, all_times = [], []
stills = []
for row, (state, durations) in enumerate(preview.ROW_DURATIONS.items()):
    for col, duration in enumerate(durations):
        cell = atlas.crop((col*192,row*208,(col+1)*192,(row+1)*208))
        all_frames.append(card(cell,state))
        all_times.append(duration)
    stills.append(card(atlas.crop((0,row*208,192,(row+1)*208)),state))
preview.save_preview(all_frames,all_times,out/'all-states.gif')
subprocess.run(['ffmpeg','-y','-i',str(out/'all-states.gif'),'-movflags','+faststart','-pix_fmt','yuv420p',str(out/'all-states.mp4')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
transition=[]
dur=[]
for row, durations in [(0,preview.ROW_DURATIONS['idle']),(4,preview.ROW_DURATIONS['jumping']),(0,preview.ROW_DURATIONS['idle'])]:
    for col,duration in enumerate(durations):
        transition.append(atlas.crop((col*192,row*208,(col+1)*192,(row+1)*208)))
        dur.append(duration)
preview.save_preview(transition,dur,out/'idle-jump-idle.gif')
look=[]
for i in range(16):
    row,col=9+i//8,i%8
    look.append(atlas.crop((col*192,row*208,(col+1)*192,(row+1)*208)))
preview.save_preview(look,[150]*16,out/'look-loop.gif')
sheet=Image.new('RGB',(320*3,260*3),'#f3f0fa')
for i,still in enumerate(stills):sheet.paste(still,((i%3)*320,(i//3)*260))
sheet.save(out/'motion-stills.png')
(out/'preview-manifest.json').write_text(json.dumps({'source':str(ROOT/'02_final/spritesheet-extended.png'),'states':list(preview.ROW_DURATIONS),'look_frames':16,'transition':'idle-jump-idle.gif'},indent=2))
print('Rendered final previews from encoded atlas')
