# IF1220 Matematika Diskrit Final Project
> **8-Connectivity Grid Graph Modeling for Lightroom-Inspired Color-Space Mask Segmentation**

## Project Description
This paper was prepared as part of the final assignment for the IF1220 Discrete Mathematics course. This project implements a Region Growing algorithm based on Breadth-First Search (BFS) to perform image segmentation on a saxophone brass object.

The primary goal of this research is to perform a comparative analysis between the 4-connectivity (Von Neumann neighborhood) and 8-connectivity (Moore neighborhood) models. The focus is on observing how these different graph theory traversal models affect morphological fidelity and how they handle the "staircase effect" on diagonal curves.

## How to Run
Ensure you have **Python** installed on your device.
If you are ready, follow these steps:
1. Clone this GitHub repository to your local computer:
```bash
git clone https://github.com/belcyne/Makalah-IF1220-Matematika-Diskrit.git
cd Makalah-IF1220-Matematika-Diskrit
```
2. Install the required libraries:
```bash
pip install opencv-python numpy
```
3. Run the main script to generate the segmentation masks:
```bash
python generate_masks.py
```

## Methodology
1. Using `find_coords.py` to determine optimal seed coordinates on the target area.
2. The BFS algorithm performs graph traversal with a Euclidean distance threshold in color space as the growth criterion.
3. Running the algorithm with two different neighborhood types to produce two mask models, which are then visually compared.

## Repository Structure
```text
├── assets/
│   ├── raw_saxophone.jpg
│   ├── mask_4conn.png
│   └── mask_8conn.png
│
├── src/
│   ├── generate_masks.py
│   └── find_coords.py
│
└── README.md
```

## Analysis Results
Based on the testing, the 8-connectivity model proves to provide more accurate segmentation results on diagonal curves. This is due to the inclusion of diagonal neighbors, which allows the algorithm to traverse pixels more continuously, thereby reducing the fragmentation often seen in the 4-connectivity model.

## About 
Author:
| Name | NIM |
|---|---|
| Christabelcyne Costan | 13525141 |
