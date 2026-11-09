import sys, os, cv2, numpy as np
# Xoá dấu sao Gemini: tự dò vùng sáng bất thường ở góc dưới phải, kết hợp mask cố định (ảnh 896x1200)
HERE = os.path.dirname(os.path.abspath(__file__))
def build_mask(im):
    h, w = im.shape[:2]
    base = cv2.imread(os.path.join(HERE, 'sparkle_mask.png'), 0)
    if (w, h) != (896, 1200): base = cv2.resize(base, (w, h), interpolation=cv2.INTER_NEAREST)
    x0, y0, x1, y1 = int(w*0.80), int(h*0.85), w, h
    g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    med = cv2.medianBlur(g, 51)
    d = g.astype(int) - med.astype(int)
    det = np.zeros_like(g)
    sub = (d[y0:y1, x0:x1] > 5).astype(np.uint8) * 255
    det[y0:y1, x0:x1] = sub
    det = cv2.morphologyEx(det, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    det = cv2.dilate(det, np.ones((7,7), np.uint8))
    return cv2.bitwise_or(det, base)
def clean(src, dst):
    im = cv2.imread(src)
    m = build_mask(im)
    out = cv2.inpaint(im, m, 4, cv2.INPAINT_TELEA)
    cv2.imwrite(dst, out, [cv2.IMWRITE_JPEG_QUALITY, 95])
if __name__ == '__main__':
    clean(sys.argv[1], sys.argv[2])
