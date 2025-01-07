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

| Video    | Modal R | I-Drop Dist | Bead R | Bead $\theta$ |
|----------|---------|-------------|--------|---------------|
| 1.0.mp4  | 14px    | 1.3R        | 13px   | 22.6°         |
| 2.0.mp4  | 12px    | 2.0R        | 2.0px  | 270.0°        |
| 2.67.mp4 | 11px    | 4.0R        | 5.1px  | 281.3°        |
| 3.33.mp4 | 10px    | 4.3R        | 5.4px  | 158.2°        |
| 4.0.mp4  | 14px    | 4.6R        | 6.7px  | 153.4°        |
| 5.33.mp4|8px | 3.8R | 3.6px | 236.3° |
| 6.67.mp4|7px | 3.4R | 2.2px | 63.4° |

Radius,Theta,Bead Section,Droplet radius
32.1,28.1,TL,51.8
9.6,258.7,BC,45.4
43.2,208.8,BR,42.6
33.0,193.2,CR,38.7
20.5,146.3,TR,35.3
13.4,261.9,BC,32.0
8.5,63.4,TL,26.7

Result for 2.67 has higher error, as the bead is not obvious to eye also.