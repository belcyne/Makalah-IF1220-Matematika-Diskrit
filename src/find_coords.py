import cv2

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"sx = {y}, sy = {x}")

img = cv2.imread('assets/raw_saxophone.png')

cv2.imshow('Click the brightest part of the curve', img)
cv2.setMouseCallback('Click the brightest part of the curve', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()