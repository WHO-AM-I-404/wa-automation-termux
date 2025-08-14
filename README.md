# WA Automation Termux

**Deskripsi:**
Script ini memungkinkan pengiriman pesan WhatsApp otomatis melalui Termux menggunakan Python, Selenium, dan Chromium. Script mendukung pengiriman ke banyak nomor sekaligus, pesan multi-baris, dan karakter khusus. Script ini dirancang untuk penggunaan pribadi dan edukasi.

Repo GitHub: [https://github.com/WHO-AM-I-404/wa-automation-termux](https://github.com/WHO-AM-I-404/wa-automation-termux/)

---

## **Fitur Utama**

1. Kirim pesan otomatis ke satu atau beberapa nomor.
2. Mendukung pesan panjang dan multi-baris.
3. Menggunakan Termux + Python + Selenium + Chromium.
4. Bisa dijalankan headless (tanpa membuka browser) atau visible.
5. Dapat diintegrasikan dengan cron di Termux untuk jadwal otomatis.

---

## **Prasyarat**

1. Termux terbaru.
2. Akses internet.
3. WhatsApp aktif pada nomor yang digunakan.
4. Chromium dan chromedriver kompatibel dengan versi Chromium di Termux.

---

## **Step-by-Step Setup di Termux**

### 1. Clone Repository

```bash
pkg install git -y
git clone https://github.com/WHO-AM-I-404/wa-automation-termux.git
cd wa-automation-termux
```

### 2. Install Dependencies

```bash
pkg update && pkg upgrade -y
pkg install python wget unzip chromium -y
pip install selenium
```

### 3. Download Chromedriver

1. Cek versi Chromium:

```bash
chromium --version
```

2. Download chromedriver sesuai versi Chromium:

```bash
wget https://chromedriver.storage.googleapis.com/<VERSI>/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver
mv chromedriver /data/data/com.termux/files/usr/bin/
```

> Ganti `<VERSI>` dengan versi chromedriver yang sesuai.

### 4. Jalankan Script Python

```bash
python wa_auto.py
```

* Script dapat mengirim pesan panjang dan multi-baris.
* Dapat mengirim ke beberapa nomor.
* Scan QR Code saat pertama kali dijalankan.

---

## **Tips & Catatan**

1. Jangan kirim spam atau pesan massal ke nomor tidak dikenal.
2. Jika pesan sangat panjang (>5000 karakter), pecah menjadi beberapa bagian.
3. Bisa dijadwalkan menggunakan cron di Termux untuk otomatisasi.
4. Headless mode membuat script lebih ringan, tapi untuk scan QR pertama kali bisa di non-headless.

---

## **Contoh Cron untuk Kirim Otomatis**

```bash
# Edit cron di Termux
crontab -e

# Tambahkan misal setiap jam 20:30
30 20 * * * python /path/ke/wa_auto.py
```

---

**Disclaimer:** Script ini untuk **penggunaan pribadi dan edukasi**. Jangan gunakan untuk spam atau pelanggaran Terms of Service WhatsApp. Risiko pemblokiran nomor bisa terjadi jika digunakan sembarangan.
