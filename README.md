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

## Data

| Video | Model R | Drop Dist | Bead R | Bead $\theta$ |
| --- | --- | --- | --- | --- |
| A.mp4 | 10px | 2.0R | 1.5px | 135° |
| B.mp4 | 10px | 2.0R | 5.1px | 191° |
| C.mp4 |  9px | 2.2R | 5.7px | 225° |
| D.mp4 |  7px | 1.7R | 1.5px | 135° |