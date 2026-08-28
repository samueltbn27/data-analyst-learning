pengeluaran = [500000, 1200000, 750000, 2000000, 450000, 1500000]

saldo_awal = 7000000
i = 0

jumlah_transaksi_kategori_besar = 0
jumlah_transaksi_diproses = 0

while saldo_awal > 2000000 and i < len(pengeluaran):

    pengeluaran_transaksi = pengeluaran[i]

    if pengeluaran_transaksi >= 1500000:
        kategori = "Besar"
        jumlah_transaksi_kategori_besar += 1

    elif pengeluaran_transaksi >= 750000:
        kategori = "Sedang"

    else:
        kategori = "Kecil"

    saldo_awal -= pengeluaran_transaksi
    jumlah_transaksi_diproses += 1

    print(
        f"Transaksi {jumlah_transaksi_diproses} | "
        f"Pengeluaran : Rp{pengeluaran_transaksi:,.0f} | "
        f"Kategori : {kategori} | "
        f"Sisa Saldo : Rp{saldo_awal:,.0f}"
    )

    i += 1


if saldo_awal > 2000000:
    status_saldo = "Aman"
else:
    status_saldo = "Waspada"

print()
print(f"Saldo Akhir : Rp{saldo_awal:,.0f}")
print(f"Jumlah Transaksi Diproses : {jumlah_transaksi_diproses}")
print(f"Jumlah Transaksi Besar : {jumlah_transaksi_kategori_besar}")
print(f"Status Saldo : {status_saldo}")