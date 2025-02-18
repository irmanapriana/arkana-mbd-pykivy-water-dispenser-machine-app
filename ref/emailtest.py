import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

# Konfigurasi Email
EMAIL_SENDER = "irmanapriana01@gmail.com"  # Ganti dengan email pengirim
EMAIL_PASSWORD = "jlhw dzqr kvzr iwkk"  # Ganti dengan App Password dari Google
EMAIL_RECEIVER = "Irman_apriana11@yahoo.com"  # Ganti dengan email tujuan

# Buat pesan email
msg = MIMEMultipart()
msg["From"] = EMAIL_SENDER
msg["To"] = EMAIL_RECEIVER
msg["Subject"] = "Subject Email Anda"
body = "Halo! Ini adalah email otomatis yang dikirim menggunakan Python."
msg.attach(MIMEText(body, "plain"))

# Kirim Email via SMTP Gmail
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()  # Enkripsi koneksi
server.login(EMAIL_SENDER, EMAIL_PASSWORD)  # Login ke akun pengirim
while 1:
    time.sleep(1)
    try:
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())  # Kirim email
        print("Email berhasil dikirim!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
