# Daftar barang & harga
barang = [
    {"nama": "cushion OMG", "harga": 50000},
    {"nama": "rak sepatu", "harga": 55000},
    {"nama": "botol minum", "harga":60000},
    {"nama": "panci listrik", "harga": 65000},
    {"nama": "sandal jepit", "harga": 70000},
    {"nama": "cermin", "harga": 75000},
    {"nama": "baju kaos", "harga": 80000},
    {"nama": "ember cuci", "harga": 85000},
    {"nama": "ember  kamar mandi", "harga": 90000},
    {"nama": "lemari portebel", "harga": 100000},
]

# Menampilkan daftar barang
print("Daftar Barang:")
for i, item in enumerate(barang, start=1):
    print(f"{i}. {item['nama']} - Harga: {item['harga']}")

# Fungsi untuk menghitung total harga
def hitung_total(daftar_barang):
    total = 0
    for item in daftar_barang:
        total += item['harga'] * item['kuantitas']
    return total

# Memilih barang
daftar_pembelian = []
while True:
    index_barang = int(input("Pilih nomor barang yang ingin dibeli (0 untuk selesai): ")) - 1
    
    if index_barang == -1:
        break

    kuantitas = int(input("Masukkan jumlah yang ingin dibeli: "))
    daftar_pembelian.append({
        "nama": barang[index_barang]['nama'],
        "harga": barang[index_barang]['harga'],
        "kuantitas": kuantitas,
    })

# Menghitung harga total
total_harga = hitung_total(daftar_pembelian)

# Menghitung potongan harga
if total_harga < 1000000:
    potongan_harga = 0
elif 1000000 <= total_harga <= 1500000:
    potongan_harga = total_harga * 0.10
else:
    potongan_harga = total_harga * 0.15

# Menghitung total bayar setelah potongan
total_bayar = total_harga - potongan_harga

# Menampilkan hasil
print("\n--- Struk Belanja ---")
for item in daftar_pembelian:
    print(f"Nama Barang: {item['nama']}")
    print(f"Kuantitas: {item['kuantitas']}")
    print(f"Harga Satuan: {item['harga']}")
    print(f"Harga Total: {item['harga'] * item['kuantitas']}")
    print("-" * 20)

print(f"Total Harga Sebelum Potongan: {total_harga}")
print(f"Potongan Harga: {potongan_harga}")
print(f"Total Bayar: {total_bayar}")