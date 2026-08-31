penjualan_bandung = [4500000, 5200000, 4800000, 6100000, 5500000, 7000000, 6500000]

penjualan_jakarta = [6000000, 5800000, 7200000, 6500000, 5900000, 8000000, 7500000]

# 1. Gabungkan data
semua_penjualan = penjualan_bandung + penjualan_jakarta

# 2. Buat copy untuk sorting
penjualan_urut = semua_penjualan.copy()
penjualan_urut.sort(reverse=True)

# 3. Tampilkan penjualan > Rp6.000.000
print("Penjualan di atas Rp6.000.000:")
for penjualan in penjualan_urut:
    if penjualan > 6_000_000:
        print(f"Penjualan tinggi : Rp{penjualan:,.0f}")

# 4. Tambahkan transaksi baru
semua_penjualan.append(9_500_000)

# 5. Perhitungan
total_penjualan = sum(semua_penjualan)
jumlah_transaksi = len(semua_penjualan)

# 6. Hitung transaksi Rp6.500.000
nilai_transaksi = semua_penjualan.count(6_500_000)

# 7. Nilai tertinggi dan terendah
nilai_tertinggi = max(semua_penjualan)
nilai_terendah = min(semua_penjualan)

# 8. Output
print(f"\nTotal Penjualan        : Rp{total_penjualan:,.0f}")
print(f"Jumlah Transaksi       : {jumlah_transaksi}")
print(f"Transaksi > 6 juta     : {sum(1 for x in semua_penjualan if x > 6_000_000)}")
print(f"Transaksi Rp6,5 juta   : {nilai_transaksi}")
print(f"Penjualan Tertinggi    : Rp{nilai_tertinggi:,.0f}")
print(f"Penjualan Terendah     : Rp{nilai_terendah:,.0f}")