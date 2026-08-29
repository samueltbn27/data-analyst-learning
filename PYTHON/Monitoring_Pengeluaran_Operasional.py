pengeluaran = [1500000, 2500000, 1000000, 3000000, 4500000, 2000000, 3500000]

anggaran = 10000000
i = 0

total_pengeluaran = 0
jumlah_transaksi_kategori_sangat_besar = 0
jumlah_transaksi_kategori_besar = 0
jumlah_seluruh_transaksi_yang_diproses = 0

while total_pengeluaran < anggaran and i <len(pengeluaran):

    data_pengeluaran  = pengeluaran[i]

    if data_pengeluaran >= 4_000_000:
        kategori = "Sangat Besar"
        jumlah_transaksi_kategori_sangat_besar += 1
    elif data_pengeluaran >= 2_000_000:
        kategori = "Besar"
        jumlah_transaksi_kategori_besar += 1
    elif data_pengeluaran >= 1_000_000:
        kategori = "Sedang"
    else:
        kategori = "Kecil"

    jumlah_seluruh_transaksi_yang_diproses += 1
    total_pengeluaran += data_pengeluaran

    print(f"Transaksi {jumlah_seluruh_transaksi_yang_diproses} | Pengeluaran : Rp{data_pengeluaran} | Kategori : {kategori} | Total : {total_pengeluaran}")

    i += 1
    
if total_pengeluaran >= anggaran:
    kategori = "Anggaran Terlampaui"
else:
    kategori = "Anggaran Masih Tersedia"

print()
print(f"Total Pengeluaran : Rp{total_pengeluaran:,.2f}")
print(f"Jumlah Transaksi Diproses : {jumlah_seluruh_transaksi_yang_diproses}")
print(f"Jumlah Sangat Besar : {jumlah_transaksi_kategori_sangat_besar}")
print(f"Jumlah Besar : {jumlah_transaksi_kategori_besar}")
print(f"Status Anggaran : {kategori}")

    