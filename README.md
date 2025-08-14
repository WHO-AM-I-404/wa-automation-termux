# WA Automation Termux

**Deskripsi:**
Script ini memungkinkan pengiriman pesan WhatsApp otomatis melalui Termux menggunakan Python, Selenium, dan Chromium. Script mendukung pengiriman ke banyak nomor sekaligus, pesan multi-baris, dan karakter khusus. Script ini dirancang untuk penggunaan pribadi dan edukasi.

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

### 1. Install Termux & Dependencies

```bash
pkg update && pkg upgrade -y
pkg install python git wget unzip -y
pkg install chromium -y
pip install selenium
```

### 2. Download Chromedriver

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

### 3. Buat Script Python

Buat file `wa_auto.py` dengan isi berikut:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.parse

# Path chromedriver
driver_path = "/data/data/com.termux/files/usr/bin/chromedriver"

# Pilihan headless agar ringan, ganti True/False sesuai kebutuhan
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Inisialisasi browser
driver = webdriver.Chrome(executable_path=driver_path, options=options)

# Buka WhatsApp Web
driver.get("https://web.whatsapp.com")
print("Scan QR Code WhatsApp Web di browser Termux jika diperlukan, tunggu 15 detik...")
time.sleep(15)  # Waktu scan QR

# Daftar nomor tujuan
nomor_list = ["+628123456789", "+628987654321"]  # ganti nomor tujuan
pesan = """Halo!
Ini pesan panjang yang bisa dikirim otomatis via Termux.
Bisa lebih dari satu baris, dan bisa pakai karakter khusus 
"""

for nomor in nomor_list:
    text = urllib.parse.quote(pesan)  # encode URL
    driver.get(f"https://web.whatsapp.com/send?phone={nomor}&text={text}")
    time.sleep(8)  # tunggu halaman load
    try:
        send_button = driver.find_element(By.XPATH, '//button[@data-testid="compose-btn-send"]')
        send_button.click()
        print(f"Pesan terkirim ke {nomor}")
    except:
        print(f"Gagal kirim ke {nomor}")
    time.sleep(3)

driver.quit()
print("Selesai semua!")
```

### 4. Jalankan Script

```bash
python wa_auto.py
```

* Script dapat mengirim pesan panjang dan multi-baris.
* Dapat mengirim ke beberapa nomor.

### 5. Upload ke GitHub (Opsional)

```bash
git init
git remote add origin https://github.com/<username>/wa-automation-termux.git
git add wa_auto.py
git commit -m "Add WhatsApp automation script"
git branch -M main
git push -u origin main
```

> Ganti `<username>` dengan username GitHub.

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
