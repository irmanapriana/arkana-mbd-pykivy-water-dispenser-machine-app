import time
import requests

def check_internet():
    url = "https://www.google.com"
    timeout = 100
    try:
        requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False

# Tunggu hingga koneksi internet tersedia
while not check_internet():
    print("Menunggu koneksi internet...")
    time.sleep(5)

print("Koneksi internet tersedia. Menjalankan program utama...")
# Tambahkan kode program utama di sini
