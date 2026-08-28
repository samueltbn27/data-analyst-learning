sales_harian = [3000000, 4500000, 7000000, 2500000, 9000000, 12000000]

target = 30000000

total_penjualan = 0
jumlah_transaksi_diproses = 0
jumlah_transaksi_tinggi = 0 

i = 0

while total_penjualan < target and i < len(sales_harian):

    penjualan = sales_harian[i]

    if penjualan >= 10000000:
        kategori = "Tinggi"
        jumlah_transaksi_tinggi += 1

    elif penjualan >= 5000000:
        kategori = "Sedang"

    else:
        kategori = "Rendah"

    total_penjualan += penjualan
    jumlah_transaksi_diproses += 1

    print(f"Transaksi {jumlah_transaksi_diproses} | "
          f"Penjualan : Rp{penjualan:,.0f} | "
          f"Kategori : {kategori} | "
          f"Total : Rp{total_penjualan:,.0f}")

    i += 1


if total_penjualan >= target:
    status_target = "Tercapai"
else:
    status_target = "Belum Tercapai"

print()
print(f"Total Penjualan : Rp{total_penjualan:,.0f}")
print(f"Jumlah Transaksi Diproses : {jumlah_transaksi_diproses}")
print(f"Jumlah Transaksi Tinggi : {jumlah_transaksi_tinggi}")
print(f"Status Target : {status_target}")   