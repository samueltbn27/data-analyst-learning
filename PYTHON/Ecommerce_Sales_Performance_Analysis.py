penjualan_barat = [12500000, 8500000, 15000000, 7200000, 9800000, 15000000]
penjualan_tengah = [6500000, 11200000, 8900000, 13400000, 7600000, 11200000]
penjualan_timur = [9200000, 5800000, 14500000, 8300000, 10500000, 6800000]

# Gabungkan data
semua_penjualan = penjualan_barat + penjualan_tengah + penjualan_timur

# Copy untuk sorting
penjualan_urut = semua_penjualan.copy()
penjualan_urut.sort(reverse=True)

# Copy untuk mencari 5 transaksi terbesar
penjualan_tertinggi = semua_penjualan.copy()
penjualan_tertinggi.sort(reverse=True)
penjualan_tertinggi = penjualan_tertinggi[:5]

# Transaksi > 10 juta
transaksi_besar = [x for x in semua_penjualan if x > 10_000_000]
jumlah_transaksi_besar = len(transaksi_besar)

# Count transaksi tertentu
transaksi_15jt = semua_penjualan.count(15_000_000)
transaksi_11_2jt = semua_penjualan.count(11_200_000)

# Tambah transaksi baru
semua_penjualan.append(17_500_000)

# Filtering Rp8 juta - Rp12 juta
print("Transaksi Rp8 juta - Rp12 juta:")
for transaksi in penjualan_urut:
    if 8_000_000 <= transaksi <= 12_000_000:
        print(f"Rp{transaksi:,.0f}")

# Analisis
total_penjualan = sum(semua_penjualan)
jumlah_transaksi = len(semua_penjualan)
rata_rata = total_penjualan / jumlah_transaksi
nilai_tertinggi = max(semua_penjualan)
nilai_terendah = min(semua_penjualan)

# Output
print("\n===== SALES ANALYSIS =====")
print(f"Jumlah Transaksi       : {jumlah_transaksi}")
print(f"Total Penjualan        : Rp{total_penjualan:,.0f}")
print(f"Rata-rata Penjualan    : Rp{rata_rata:,.0f}")
print(f"Penjualan Tertinggi    : Rp{nilai_tertinggi:,.0f}")
print(f"Penjualan Terendah     : Rp{nilai_terendah:,.0f}")

print(f"\nTransaksi > 10 Juta    : {jumlah_transaksi_besar}")
print(f"Transaksi Rp15 Juta    : {transaksi_15jt} kali")
print(f"Transaksi Rp11,2 Juta  : {transaksi_11_2jt} kali")

print("\n5 Transaksi Tertinggi:")
for transaksi in penjualan_tertinggi:
    print(f"Rp{transaksi:,.0f}")