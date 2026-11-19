# POSTING.md — paket posting X (BELUM DIPOSTING)

> JANGAN posting sendiri dari file ini tanpa perintah user. File ini adalah
> paket siap posting: gambar + caption + langkah persis. Setelah posting,
> isi `POST.json` dengan alamat post, lalu submit sebelum deadline
> **23 Nov 2026 21:00 WIB** (23 Nov 14:00 UTC).

## 1. Aset

- Gambar: **`meme.png`** di repo ini (1024x1024 PNG) — SATU-SATUNYA gambar
  yang dilampirkan, sebagai gambar pertama/utama post.
  - Preview 480px (`meme-480-preview.png`) sudah dicek: semua caption dan
    ghost make.fun tetap terbaca di ukuran yang dilihat juri.
- Akun: akun X **publik** (bukan protected) milik user. Post dan akun harus
  tetap publik sampai hasil keluar.

## 2. Caption (salin persis, jangan diedit)

```
waited 13 years for GTA 6 just to stare at a download bar stuck at 99% 😭

meanwhile my AI agent made this meme and entered it in a $500 bounty on make.fun — where people and their agents win real money building things. put yours to work: https://make.fun/bounty/gta6-meme-x-01 @makefunai

makefun-walnut-statue-footpath
```

Ceklis isi caption:
- [x] make.fun sebagai link (https://make.fun/bounty/gta6-meme-x-01) + tag @makefunai
- [x] Play code akun: `makefun-walnut-statue-footpath` (code 0 dari 4, diambil via API 19 Nov 2026)
- [x] Pitch: orang + AI agent bisa dapat uang beneran di make.fun (bounty $500 ini)
- [x] Pendek — teks post tetap utuh di dossier juri (batas ~1.100 byte teks post)

## 3. Langkah posting (persis)

1. Buka X di akun publik user (web atau aplikasi).
2. Buat post baru (tombol Post / +).
3. Lampirkan **`meme.png`** sebagai gambar pertama dan satu-satunya.
   Jangan tambah GIF/video — post tanpa gambar, atau hanya GIF/video,
   ditolak.
4. Tempel caption di atas **persis** (termasuk link, tag, dan play code).
5. Pastikan post bersifat publik, lalu tekan **Post**.
6. Setelah terbit, buka post itu → tombol Share → Copy link.
   Alamat harus berbentuk `https://x.com/<handle>/status/<id>`.
7. Tulis alamat itu ke `POST.json` di repo ini:
   `{"url": "https://x.com/<handle>/status/<id>"}`.
8. Jalankan ulang kit check dan submit sebelum deadline 23 Nov 2026 21:00 WIB.
9. Jangan hapus post, jangan protect akun, sampai hasil keluar.

## 4. Yang TIDAK boleh

- Jangan posting dari akun protected — house tidak bisa membaca post-nya.
- Jangan edit teks post setelah terbit (X tidak bisa edit teks) — kalau ada
  yang salah (link/tag/play code hilang), hapus dan posting ulang yang baru.
- Jangan pakai post orang lain / post yang sudah di-entry akun lain.
