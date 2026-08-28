sales = [3000000, 4500000, 2000000, 6500000, 8000000, 5000000, 9000000]

target = 20000000
i = 0

total_penjualan = 0
jumlah_transaksi_diproses = 0
jumlah_transaksi_sangat_tinggi = 0

while total_penjualan < target and i < len(sales):

    penjualan = sales[i]

    if penjualan >= 8000000:
        kategori = "Sangat Tinggi"
        jumlah_transaksi_sangat_tinggi += 1
    elif penjualan >= 5000000:
        kategori = "Tinggi"
    elif penjualan >= 3000000:
        kategori = "Sedang"
    else:
        kategori = "Rendah"

    total_penjualan += penjualan
    jumlah_transaksi_diproses += 1

    print(f"Transaksi {jumlah_transaksi_diproses} | Penjualan : Rp{penjualan:,.2f} | Kategori : {kategori}")

    i += 1

if total_penjualan >= target:
    kondisi = "Target Tercapai"
else:
    kondisi = "Target Belum Tercapai"
    
print(f"Total Penjualan : Rp{total_penjualan:,.2f}")
print(f"Jumlah Transaksi Diproses : {jumlah_transaksi_diproses}")
print(f"Jumlah Transaksi Sangat Tinggi : {jumlah_transaksi_sangat_tinggi}")
print(f"Status Target : {kondisi}")