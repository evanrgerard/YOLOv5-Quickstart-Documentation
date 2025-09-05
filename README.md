# 📘 Panduan Sederhana Menjalankan YOLOv5
Dokumen ini berfungsi sebagai panduan singkat untuk menjalankan YOLOv5. 

> [!WARNING]
> Mohon perhatian bahwa dokumuentasi ini merupakan ringkasan dari dokumentasi yang di-publish sebetulnya. Jika ingin belajar lebih lanjut mohon baca dan pelajari pada bagian referensi

## 1️⃣ Clone Repository
Unduh repo dari GitHub:

```
git clone https://github.com/evanrgerard/YOLOv5-Quickstart-Documentation.git
```

## 2️⃣ Masuk ke Direktori Repo
Pindah ke folder:

```
cd YOLOv5-Quickstart-Documentation
```

## 3️⃣ Install Dependencies
Install semua kebutuhan dengan:

```
pip install -r requirements.txt
```

🔎 Apa saja yang ada di requirements.txt?
- torch & torchvision   → Framework utama deep learning untuk inference.
- ultralytics           → Paket resmi YOLOv5/YOLOv8.
- opencv-python         → Menangani gambar & visualisasi (membaca, menampilkan, menggambar bounding box).
- numpy                 → Operasi array & numerik.
- pandas                → Mengolah hasil deteksi dalam bentuk tabel.
- matplotlib, seaborn   → Visualisasi data hasil deteksi (opsional).
- pillow                → Manipulasi gambar.

## 4️⃣ Jalankan Inference Sederhana
Gunakan script bawaan:

```
python simple_inference.py
```

## 🔎 Ringkasan isi simple_inference.py
Script ini terdiri dari beberapa bagian:

1. Import Library :
```
Import Library
import torch, cv2, numpy as np
```
torch                 → Memuat model YOLOv5 dari torch.hub.
cv2                   → Menampilkan gambar & menggambar bounding box.
numpy                 → Operasi array untuk manipulasi data koordinat.

2. Load Model & Gambar :
```
model = torch.hub.load("ultralytics/yolov5", "yolov5s")
img_path = "test1.jpg"
results = model(img_path)
```

3. Mengambil model YOLOv5s (pretrained).
Menjalankan deteksi pada test1.jpg dan mengammbil Hasil dalam Bentuk DataFrame
```
df = results.pandas().xyxy[0]
```
Hasil deteksi disimpan dalam format tabel (bounding box, confidence, label).

4. Render Hasil Deteksi
```
img = results.render()[0]
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
```

5. Memberi hasil gambar dengan bounding box otomatis.
```
for _, row in df.iterrows():
    cv2.rectangle(...)
    cv2.putText(...)
```

6. Tampilkan Gambar Hasil Deteksi
```
cv2.imshow("YOLOv5 Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## 5️⃣ Hasil
Setelah menjalankan script, Anda akan melihat jendela menampilkan gambar test1.jpg dengan bounding box dan label hasil deteksi.

## 6️⃣ Referensi
- https://docs.ultralytics.com/yolov5/quickstart_tutorial
- https://youtu.be/fu2tfOV9vbY?si=b6_Vc3pbC6hWoaY9
