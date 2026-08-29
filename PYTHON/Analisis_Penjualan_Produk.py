sales_data = [
    ["Laptop", 12000000],
    ["Mouse", 750000],
    ["Keyboard", 1500000],
    ["Monitor", 4500000],
    ["Headset", 900000],
    ["Printer", 6000000],
    ["Webcam", 1200000]
]

total_penjualan = 0
jumlah_produk_sangat_tinggi = 0
jumlah_produk_tinggi = 0
jumlah_produk_sedang = 0
jumlah_produk_rendah = 0
jumlah_produk_dengan_penjualan_di_atas_limajuta = 0

for produk, harga in sales_data:

    if harga >= 10_000_000:
        kategori = "Sangat Tinggi"
        jumlah_produk_sangat_tinggi += 1
    elif harga >= 5_000_000:
        kategori = "Tinggi"
        jumlah_produk_tinggi += 1
        jumlah_produk_dengan_penjualan_di_atas_limajuta += 1
    elif harga >= 1_000_000:
        kategori = "Sedang"
        jumlah_produk_sedang += 1
    else:
        kategori = "Rendah"
        jumlah_produk_rendah += 1

    total_penjualan += harga

    print(f"Produk : {produk} | Penjualan : {harga:,.2f} | Kategori : {kategori}")

print()
print(f"Total Penjualan : Rp{total_penjualan:,.2f}")
print(f"Jumlah Sangat Tinggi : {jumlah_produk_sangat_tinggi}")
print(f"Jumlah Tinggi : {jumlah_produk_tinggi}")
print(f"Jumlah Sedang : {jumlah_produk_sedang}")
print(f"Jumlah Rendah : {jumlah_produk_rendah}")
print(f"Produk di atas 5 juta : {jumlah_produk_dengan_penjualan_di_atas_limajuta}")