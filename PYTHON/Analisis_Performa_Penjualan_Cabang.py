sales_data = [
    ["Bandung", 12000000],
    ["Jakarta", 8500000],
    ["Bandung", 4500000],
    ["Surabaya", 15000000],
    ["Jakarta", 11000000],
    ["Surabaya", 6500000],
    ["Bandung", 9000000],
    ["Jakarta", 4000000]
]

total_penjualan = 0
jumlah_sangat_baik = 0
jumlah_baik = 0
jumlah_cukup = 0
jumlah_kurang = 0
transaksi_dibawah_5juta = 0

for kota, data in sales_data:

    if data >= 10000000:
        kategori = "Sangat Baik"
        jumlah_sangat_baik += 1

    elif data >= 7000000:
        kategori = "Baik"
        jumlah_baik += 1

    elif data >= 5000000:
        kategori = "Cukup"
        jumlah_cukup += 1

    else:
        kategori = "Kurang"
        jumlah_kurang += 1
        transaksi_dibawah_5juta += 1

    print(f"{kota} | Rp{data:,.2f} | {kategori}")

    total_penjualan += data

print()

print(f"Total Penjualan : Rp{total_penjualan:,.2f}")
print(f"Jumlah Sangat Baik : {jumlah_sangat_baik}")
print(f"Jumlah Baik : {jumlah_baik}")
print(f"Jumlah Cukup : {jumlah_cukup}")
print(f"Jumlah Kurang : {jumlah_kurang}")
print(f"Transaksi di bawah 5 juta : {transaksi_dibawah_5juta}")