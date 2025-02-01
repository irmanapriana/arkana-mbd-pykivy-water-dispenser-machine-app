from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusIOException
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder
from pymodbus.constants import Endian
import time


def connect_modbus(port, baudrate, parity, stopbits, bytesize, timeout):
    """
    Fungsi untuk mencoba koneksi Modbus RTU.
    """
    try:
        print(f"Mencoba terhubung ke Modbus RTU di port {port} dengan baudrate {baudrate}...")
        client = ModbusSerialClient(
            port=port,
            baudrate=baudrate,
            parity=parity,
            stopbits=stopbits,
            bytesize=bytesize,
            timeout=timeout,
            framer="rtu",  # Gunakan framer RTU
        )

        connection = client.connect()  # Mencoba koneksi
        if connection:
            print(f"Berhasil terhubung ke perangkat Modbus dengan baudrate {baudrate}.")
            return client, True
        else:
            print(f"Gagal terhubung ke perangkat Modbus dengan baudrate {baudrate}.")
            return None, False

    except ModbusIOException as e:
        print(f"Kesalahan ModbusIOException: {e}")
        return None, False
    except Exception as e:
        print(f"Kesalahan umum: {e}")
        return None, False


def read_holding_registers(client, address, count):
    """
    Membaca holding register pada alamat tertentu.
    """
    try:
        response = client.read_holding_registers(address, count, unit=1)
        if response.isError():
            print(f"Kesalahan membaca holding register di alamat {address}: {response}")
        else:
            print(f"Holding register dari alamat {address} hingga {address + count - 1}: {response.registers}")
            return response.registers
    except Exception as e:
        print(f"Kesalahan membaca holding register: {e}")


def write_holding_registers(client, address, values):
    """
    Menulis nilai ke holding register pada alamat tertentu.
    """
    try:
        for i, value in enumerate(values):
            response = client.write_register(address + i, value, unit=1)
            if response.isError():
                print(f"Kesalahan menulis ke holding register di alamat {address + i}: {response}")
            else:
                print(f"Berhasil menulis {value} ke holding register di alamat {address + i}")
    except Exception as e:
        print(f"Kesalahan menulis holding register: {e}")


def read_coils(client, address, count):
    """
    Membaca coil pada alamat tertentu.
    """
    try:
        response = client.read_coils(address, count, unit=1)
        if response.isError():
            print(f"Kesalahan membaca coil di alamat {address}: {response}")
        else:
            print(f"Coil dari alamat {address} hingga {address + count - 1}: {response.bits}")
            return response.bits
    except Exception as e:
        print(f"Kesalahan membaca coil: {e}")


# Parameter koneksi Modbus
port = "COM8"        # Ganti dengan port perangkat Anda
baudrates = [9600, 19200, 38400]  # Daftar baudrate yang akan dicoba
default_baudrate = 9600  # Baudrate default
parity = "N"         # Parity: 'N' (None), 'E' (Even), atau 'O' (Odd)
stopbits = 1         # Stop bits: 1 atau 2
bytesize = 8         # Byte size: 7 atau 8
timeout = 0.5        # Timeout dalam detik

# Loop untuk mencoba koneksi
client = None
connected = False

while not connected:
    for baudrate in baudrates:
        client, connected = connect_modbus(port, baudrate, parity, stopbits, bytesize, timeout)
        if connected:
            break
        else:
            time.sleep(1)  # Tunggu sebelum mencoba lagi

    # Jika tidak berhasil setelah semua baudrate, coba kembali ke default
    if not connected:
        print("Koneksi gagal dengan semua baudrate. Mencoba lagi dengan baudrate default...")
        client, connected = connect_modbus(port, default_baudrate, parity, stopbits, bytesize, timeout)

# Jika koneksi berhasil, jalankan program utama
if connected:
    print("Koneksi berhasil! Melanjutkan program utama...")

    # Membaca holding register dari alamat 0 hingga 11
    registers = read_holding_registers(client, 0, 12)

    # Jika berhasil membaca holding register, menulis nilai baru ke holding register
    if registers is not None:
        new_values = [x + 1 for x in registers]  # Misalnya, tambahkan 1 ke setiap nilai
        write_holding_registers(client, 0, new_values)

    # Membaca coil dari alamat 0 hingga 11
    coils = read_coils(client, 0, 12)

    # Tutup koneksi setelah selesai
    client.close()
