penjualan = {
    "produk": "Laptop",
    "kategori": "Elektronik",
    "harga": 7500000,
    "jumlah_terjual": 4
}

# 1. Tampilkan nama produk dan kategori
print(f"Produk : {penjualan['produk']}")
print(f"Kategori : {penjualan['kategori']}")

# 2. Hitung total pendapatan
total_pendapatan = penjualan["harga"] * penjualan["jumlah_terjual"]
print(f"Total Pendapatan : Rp{total_pendapatan:,.0f}")

# 3. Ubah harga laptop
penjualan["harga"] = 7000000

# 4. Tambahkan item baru
penjualan["stok"] = 10

# 5. Hitung kembali total pendapatan
total_pendapatan = penjualan["harga"] * penjualan["jumlah_terjual"]
print(f"Total Pendapatan : Rp{total_pendapatan:,.0f}")

print()

# 6. Loop menggunakan .items()
for key, value in penjualan.items():
    print(f"{key} : {value}")