# mochi-jobs

Trang duyệt ảnh Mochi Mây (GitHub Pages) + nơi trao đổi dữ liệu giữa task 5h và task 10h.

```
index.html                    # trang duyệt: lưới ảnh, tick, "Gửi duyệt"
days/index.json               # {"days": ["2026-11-09", ...]}
days/<ngày>/manifest.json     # task 5h ghi: danh sách ảnh + caption gợi ý
days/<ngày>/img/NN.jpg        # ảnh pose
days/<ngày>/approved.json     # trang ghi khi bạn bấm "Gửi duyệt"; task 10h đọc
state/used_refs.json          # ref đã dùng, tránh lặp
```

Token: fine-grained, chỉ repo này, quyền Contents: Read and write. Dán vào ⚙️ trên trang (lưu trong trình duyệt).
