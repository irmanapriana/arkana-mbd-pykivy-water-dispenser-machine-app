import threading
import time

# Fungsi yang dijalankan di thread
def print_in_thread():
    for i in range(5):
        print(f"Thread berjalan: {i}")
        time.sleep(1)

# Membuat dan memulai thread
thread = threading.Thread(target=print_in_thread)
thread.start()

# Menunggu thread selesai
thread.join()

print("Thread selesai.")
