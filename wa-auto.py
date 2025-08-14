```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.parse

# Path chromedriver
driver_path = "/data/data/com.termux/files/usr/bin/chromedriver"

# Pilihan headless agar ringan, True = tanpa buka browser, False = visible
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Inisialisasi browser
driver = webdriver.Chrome(executable_path=driver_path, options=options)

# Buka WhatsApp Web
print("Membuka WhatsApp Web, silakan scan QR Code jika diperlukan...")
driver.get("https://web.whatsapp.com")
time.sleep(15)  # waktu scan QR

# Daftar nomor tujuan
nomor_list = ["+628123456789", "+628987654321"]  # ganti nomor tujuan

# Pesan yang akan dikirim (bisa multi-baris dan karakter khusus)
pesan = """Halo!
Ini pesan panjang yang bisa dikirim otomatis via Termux.
Bisa lebih dari satu baris, dan bisa pakai karakter khusus 
"""

# Loop untuk mengirim ke semua nomor
for nomor in nomor_list:
    text = urllib.parse.quote(pesan)  # encode URL
    driver.get(f"https://web.whatsapp.com/send?phone={nomor}&text={text}")
    time.sleep(8)  # tunggu halaman load
    try:
        send_button = driver.find_element(By.XPATH, '//button[@data-testid="compose-btn-send"]')
        send_button.click()
        print(f"Pesan terkirim ke {nomor}")
    except Exception as e:
        print(f"Gagal kirim ke {nomor}: {e}")
    time.sleep(3)  # delay antar nomor

# Tutup browser setelah selesai
driver.quit()
print("S
```
