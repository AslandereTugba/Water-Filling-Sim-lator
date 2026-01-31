# Water Filling Simulator (ASCII) — Python

A small Python console project that visualizes filling a glass step-by-step using ASCII characters.  
After each pour, the program prints the current water level inside the glass; if the glass overflows, the overflow is shown extending to the right.

## What it does
- Takes **glass width**, **glass height**, and **how many pours** will be made.
- After each pour, prints an ASCII glass:
  - `|` and `-` form the glass borders
  - `*` shows filled water inside the glass
  - Overflow is displayed to the **right side** when total water exceeds capacity

## Input format
The program reads inputs from standard input in this order:

1. `glass_width` (integer)
2. `glass_height` (integer)
3. `fill_count` (integer)
4. `fill_count` lines of poured water amounts (integers)

## How to run
```bash
python WaterFillingSimulatorProject.py
Then enter the values line by line (or redirect from a file).

Example
Input

4
3
3
5
4
10
Output (excerpt)

|    |
|*   |
|****|
------
######

|*   |
|****|
|****|
------
######
...
Tech
Python 3

Notes
This is a console/ASCII visualization project (no GUI).

Designed as a practice exercise for loops, integer arithmetic, and output formatting.


İstersen README’ye en üste bir de **“Live demo”** gibi küçük bir GIF/ekran görüntüsü eklemek için (ör. terminal çıktısı) mini bir “Screenshots” bölümü de yazabilirim.
