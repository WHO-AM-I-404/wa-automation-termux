import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Konfigurasi
DELAY_BETWEEN_CONTACTS = 30  # Detik (sesuai kebijakan WhatsApp)
WAIT_TIME = 45  # Maksimal waktu tunggu elemen (detik)
MESSAGE_FILE = "message.txt"
CONTACTS_FILE = "contacts.txt"

class WhatsAppSender:
    def __init__(self):
        self.driver = self.setup_driver()
        
    def setup_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        return webdriver.Chrome(options=options)
    
    def load_content(self):
        """Membaca pesan dan kontak dari file"""
        try:
            with open(MESSAGE_FILE, 'r', encoding='utf-8') as file:
                message = file.read().strip()
                
            with open(CONTACTS_FILE, 'r') as file:
                contacts = [line.strip() for line in file if line.strip()]
                
            return message, contacts
        except Exception as e:
            print(f"Error loading files: {str(e)}")
            return None, None
    
    def wait_for_login(self):
        """Menunggu user login WhatsApp Web"""
        self.driver.get('https://web.whatsapp.com')
        print("Silakan scan QR code di WhatsApp Web...")
        
        # Tunggu sampai login berhasil
        try:
            WebDriverWait(self.driver, WAIT_TIME).until(
                EC.presence_of_element_located((By.XPATH, '//div[@title="Menu"]'))
            )
            print("Login berhasil!")
            return True
        except TimeoutException:
            print("Login timeout. Silakan coba lagi.")
            return False
    
    def send_to_contact(self, phone, message):
        """Mengirim pesan ke satu nomor"""
        try:
            # Buka chat
            self.driver.get(f'https://web.whatsapp.com/send?phone={phone}&text&app_absent=1')
            
            # Tunggu input pesan muncul
            input_box = WebDriverWait(self.driver, WAIT_TIME).until(
                EC.presence_of_element_located((By.XPATH, '//div[@title="Ketikan pesan"]'))
            )
            
            # Masukkan pesan per baris untuk menghindari error
            for line in message.split('\n'):
                input_box.send_keys(line)
                input_box.send_keys(Keys.SHIFT + Keys.ENTER)
                time.sleep(0.5)
            
            # Kirim pesan
            input_box.send_keys(Keys.ENTER)
            time.sleep(3)
            return True
        except Exception as e:
            print(f"Error: {str(e)}")
            return False
    
    def run(self):
        """Menjalankan proses pengiriman utama"""
        if not self.wait_for_login():
            return
        
        message, contacts = self.load_content()
        if not message or not contacts:
            print("Pastikan message.txt dan contacts.txt sudah diisi!")
            return
        
        print(f"\nAkan mengirim ke {len(contacts)} kontak")
        print("Tekan Ctrl+C untuk berhenti kapan saja\n")
        
        try:
            for i, phone in enumerate(contacts):
                print(f"[{i+1}/{len(contacts)}] Mengirim ke {phone}...", end=' ', flush=True)
                
                if self.send_to_contact(phone, message):
                    print("✓ Berhasil")
                else:
                    print("✘ Gagal")
                
                # Delay antara kontak
                if i < len(contacts) - 1:
                    print(f"Menunggu {DELAY_BETWEEN_CONTACTS} detik...")
                    time.sleep(DELAY_BETWEEN_CONTACTS)
                    
            print("\nPengiriman selesai!")
        except KeyboardInterrupt:
            print("\nDihentikan oleh pengguna")
        finally:
            self.driver.quit()

if __name__ == "__main__":
    sender = WhatsAppSender()
    sender.run()
