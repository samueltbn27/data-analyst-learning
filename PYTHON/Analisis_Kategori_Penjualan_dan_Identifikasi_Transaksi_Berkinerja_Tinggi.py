sales = [4500000, 7200000, 15000000, 3200000, 9800000, 12500000, 5500000]

jumlah_transaksi_kategori_tinggi = 0

for sales_transaksi in sales:

    if sales_transaksi >= 10000000:
        kategori = "Tinggi"
        jumlah_transaksi_kategori_tinggi += 1
    elif sales_transaksi >= 5000000:
        kategori = "Sedang"
    else:
        kategori = "Rendah"

    print(f"Penjualan : {sales_transaksi} | Kategori : {kategori}")

print(f"Jumlah Transaksi Kategori Tinggi : {jumlah_transaksi_kategori_tinggi}")