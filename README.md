## circle detection

## Conversions
- Set 1: 100µm = 12px [0.036 * width of frame]
- Set 2: 100µm = 14px [0.040 * width of frame]

## Usage

**Extract frames & boxes**:
```bash
fmpeg -i ./test.mp4 './in_dir/%03d.png'
python3 scripts/extract.py in_dir out_dir
```

## Todos
- Add tunable param to convert pixels &rarr; µm
- Do for all 7 videos $(r, \theta)$
- Make PPT

## Set 1

cx, cy = round(width * 0.485), round(height * 0.75)
cx, cy = round(width * 0.485), round(height * 0.843)
cx, cy = round(width * 0.43), round(height * 0.82)