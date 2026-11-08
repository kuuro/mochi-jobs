import sys, cv2, numpy as np
# Gemini sparkle remover: finds the translucent bright star near the bottom-right corner and inpaints it.
def clean(src, dst):
    im = cv2.imread(src); h, w = im.shape[:2]; s = w/896
    reg = np.zeros((h, w), np.uint8)
    for cx, cy, r in ((796,1100,40),(838,1141,20)):
        cv2.circle(reg, (int(cx*s), int(cy*s)), int(r*s), 255, -1)
    g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY).astype(np.float32)
    bg = cv2.medianBlur(im, int(61*s)//2*2+1); bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY).astype(np.float32)
    star = ((g - bg) > 6).astype(np.uint8) * 255
    mask = cv2.bitwise_and(star, reg)
    mask = cv2.dilate(mask, np.ones((int(7*s)|1, int(7*s)|1), np.uint8))
    mask = cv2.bitwise_and(mask, reg)
    out = cv2.inpaint(im, mask, 3, cv2.INPAINT_TELEA)
    cv2.imwrite(dst, out, [cv2.IMWRITE_JPEG_QUALITY, 95])
if __name__ == '__main__':
    clean(sys.argv[1], sys.argv[2])
