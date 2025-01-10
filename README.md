## circle detection

First take out 1 frame to run _The Algorithm_ on.

Algorithm
- Run sobel edge detection
- Run hough transform with initial params
- Calculate `R` mode radius
- Run hough transform with $(R-\epsilon, R+\epsilon)$ with line scan size $<2(R+\epsilon)$
- Bin results into groups of bin-width $R$

Then use the max_y and circle distance to use later with beat frequency.

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