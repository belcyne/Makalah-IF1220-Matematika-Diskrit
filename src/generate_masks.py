import cv2
import numpy as np
from collections import deque

def generate_mask(image, sx, sy, threshold, is_8_conn=True):
    h, w, _ = image.shape
    mask = np.zeros((h, w), dtype=np.uint8)
    queue = deque([(sx, sy)])
    mask[sx, sy] = 1
    seed = image[sx, sy].astype(np.float32)
    
    dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)] if is_8_conn else [(-1,0), (1,0), (0,-1), (0,1)]
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < h and 0 <= ny < w and not mask[nx, ny]:
                if np.linalg.norm(seed - image[nx, ny].astype(np.float32)) <= threshold:
                    mask[nx, ny] = 1
                    queue.append((nx, ny))
    return mask

def export_overlay(img, mask, filename):
    overlay = img.copy()
    overlay[mask == 1] = [0, 0, 255]
    cv2.imwrite(filename, cv2.addWeighted(overlay, 0.5, img, 0.5, 0))

img = cv2.imread('assets/raw_saxophone.png')

sx, sy, thresh = 552, 312, 40

export_overlay(img, generate_mask(img, sx, sy, thresh, False), 'assets/mask_4conn.png')
export_overlay(img, generate_mask(img, sx, sy, thresh, True),  'assets/mask_8conn.png')

print("Masks successfully generated!")