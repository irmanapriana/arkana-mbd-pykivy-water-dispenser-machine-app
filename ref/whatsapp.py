import pywhatkit as kit

# Nomor tujuan dengan kode negara (contoh: +62 untuk Indonesia)
# nomor = "+6285659109070"
# nomor = "+6281212678942"
nomor = "+6287752652291"
pesan = "Halo! Ini pesan otomatis dari Python."
# pesan = "Halo! Ini pesan otomatis dari Python."

# Kirim pesan secara langsung
kit.sendwhatmsg_instantly(nomor, pesan)
print("Pesan berhasil dijadwalkan!")
