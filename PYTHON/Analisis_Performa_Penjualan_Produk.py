penjualan = {
    "Laptop": {
        "kategori": "Elektronik",
        "harga": 7000000,
        "jumlah_terjual": 5
    },
    "Headset": {
        "kategori": "Aksesoris",
        "harga": 500000,
        "jumlah_terjual": 12
    },
    "Mouse": {
        "kategori": "Aksesoris",
        "harga": 300000,
        "jumlah_terjual": 8
    }
}

# 1. Tampilkan harga Laptop
print(f"Harga Laptop : {penjualan["Laptop"]["harga"]:,.0f}")

# 2. Tampilkan jumlah Headset yang terjual
print(f"Headset Terjual : {penjualan["Headset"]["jumlah_terjual"]}")

# 3. Ternyata harga Mouse berubah dari 300000 menjadi 350000
penjualan["Mouse"]["harga"] = 350000

# 4. Tambahkan informasi "stok" untuk setiap produk
penjualan["Laptop"]["stok"] = 10
penjualan["Headset"]["stok"] = 20
penjualan["Mouse"]["stok"] = 15

print()
# 5. Gunakan looping untuk menampilkan seluruh data produk
for produk, detail in penjualan.items():
    print(f"\n{produk}")
    for key, value in detail.items():
        print(f"{key} : {value}")

print()
# 6. Untuk setiap produk, hitung
for produk, detail in penjualan.items():
    total = detail["harga"] * detail["jumlah_terjual"]
    print(f"{produk} : {total:,.0f}")

print()
# 7. Hitung total seluruh pendapatan toko dari semua produk
total_pendapatan = 0
for produk, detail in penjualan.items():
    total = detail["harga"] * detail["jumlah_terjual"]
    total_pendapatan += total
print(f"Total Pendapatan : {total_pendapatan:,.0f}")

