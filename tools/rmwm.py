import sys, os, cv2, numpy as np
# Xoá dấu sao Gemini ở góc dưới phải (ảnh 896x1200; ảnh khác kích thước thì mask được scale theo)
MASK = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sparkle_mask.png')
def clean(src, dst):
    im = cv2.imread(src); h, w = im.shape[:2]
    m = cv2.imread(MASK, 0)
    if (w, h) != (896, 1200): m = cv2.resize(m, (w, h), interpolation=cv2.INTER_NEAREST)
    out = cv2.inpaint(im, m, 3, cv2.INPAINT_TELEA)
    cv2.imwrite(dst, out, [cv2.IMWRITE_JPEG_QUALITY, 95])
if __name__ == '__main__':
    clean(sys.argv[1], sys.argv[2])
