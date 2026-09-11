penjualan = {
    "produk": "Laptop",
    "kategori": "Elektronik",
    "harga": 7500000,
    "jumlah_terjual": 4
}

# 1. Tampilkan nama produk dan kategori
print(f"Produk : {penjualan["produk"]}")
print(f"Kategori : {penjualan["kategori"]}")

# 2. Hitung total pendapatan    
total_pendapatan = penjualan["harga"] * penjualan["jumlah_terjual"]
print(f"Total Pendapatan : Rp{total_pendapatan:,.0f}")

# 3. Ubah harga laptop dari 7.500.000 menjadi 7.000.000
penjualan["harga"] = 7000000

# 4. Tambahkan item baru
penjualan["jumlah_terjual"] = 4

# 5. Karena harga sudah berubah, hitung kembali total_pendapatan
total_pendapatan = penjualan["harga"] * penjualan["jumlah_terjual"]
print(f"Total Pendapatan : Rp{total_pendapatan:,.0f}")

print()

# 6. Gunakan .items() untuk melakukan looping
for key, value in penjualan.items():
    print(f"{key} : {value}")