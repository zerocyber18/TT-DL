
# 🚀 TT DL - Ultimate TikTok Downloader

<p align="center">
  <img src="https://img.shields.io/badge/Version-2.0.0-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Dev-zeroXploit-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Platform-Termux-green?style=for-the-badge">
</p>

---

## ⚡ Overview
**TT DL** adalah alat canggih berbasis Command Line Interface (CLI) yang dirancang khusus untuk pengguna Termux. Dengan integrasi engine **yt-dlp**, tool ini memungkinkan Anda mengunduh konten TikTok dengan kualitas tertinggi tanpa watermark dan konversi MP3 instan.

> "Dibuat dengan presisi oleh **zeroXploit** untuk efisiensi dan estetika."

---

## 🎨 Main Features
- 💎 **No Watermark**: Unduhan video bersih 100% tanpa logo.
- 🎵 **HQ Audio Extraction**: Mengonversi video ke format MP3 192kbps.
- 🛡️ **Auto-Update Engine**: Menjamin tool tetap bekerja meskipun TikTok update sistem.
- 📺 **High Definition**: Mengambil resolusi tertinggi yang tersedia.
- 📂 **Direct Storage**: Otomatis tersimpan di folder `/sdcard/Download`.

---

## 🛠️ Installation Guide

Ikuti langkah-langkah di bawah ini untuk menginstal **TT DL** di Termux:

### 1. Update System & Package
```bash
pkg update && pkg upgrade -y
pkg install python ffmpeg git -y
git clone https://github.com/zerocyber18/TT-DL.git
cd TT-DL
PIP install -r requirements.txt
python tiktok.py