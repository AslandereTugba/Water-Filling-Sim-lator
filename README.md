# Water Filling Simulator (ASCII) — Python

A Python console program that simulates filling a glass step-by-step and visualizes the result using ASCII characters. After each pour, the program prints the current fill level inside the glass; if the total amount exceeds capacity, overflow is displayed to the right.

## Features
- User-defined glass dimensions (width/height)
- Multiple pour steps (incremental filling)
- ASCII visualization of:
  - glass borders
  - water level
  - overflow when capacity is exceeded

## How It Works
1. The program reads `glass_width`, `glass_height`, and `fill_count`.
2. It then reads `fill_count` pour amounts.
3. After each pour, it prints the updated glass with the new water level and possible overflow.

## Input Format
Enter values in this order:
1. `glass_width` (int)
2. `glass_height` (int)
3. `fill_count` (int)
4. `fill_count` lines of pour amounts (int)

## Run
```bash
python WaterFillingSimulatorProject.py
