sales_data = [
    ["Bandung", [3000000, 4500000, 2000000]],
    ["Jakarta", [5000000, 7000000, 6500000]],
    ["Surabaya", [4000000, 3000000, 8000000]]
]

target = 25000000

i = 0
total_penjualan = 0
jumlah_cabang_diproses = 0
jumlah_transaksi_sangat_tinggi = 0

while total_penjualan < target and i < len(sales_data):

    cabang = sales_data[i][0]
    daftar_penjualan = sales_data[i][1]

    total_penjualan_cabang = 0

    print(f"\nCabang : {cabang}")

    for penjualan in daftar_penjualan:

        if penjualan >= 7000000:
            kategori = "Sangat Tinggi"
            jumlah_transaksi_sangat_tinggi += 1

        elif penjualan >= 5000000:
            kategori = "Tinggi"

        elif penjualan >= 3000000:
            kategori = "Sedang"

        else:
            kategori = "Rendah"

        total_penjualan_cabang += penjualan
        total_penjualan += penjualan

        print(
            f"Penjualan : Rp{penjualan:,.0f} | "
            f"Kategori : {kategori}"
        )

    jumlah_cabang_diproses += 1

    print(f"Total {cabang} : Rp{total_penjualan_cabang:,.0f}")

    i += 1


if total_penjualan >= target:
    status_target = "Tercapai"
else:
    status_target = "Belum Tercapai"


print()
print(f"Total Seluruh Penjualan : Rp{total_penjualan:,.0f}")
print(f"Jumlah Cabang Diproses : {jumlah_cabang_diproses}")
print(f"Jumlah Transaksi Sangat Tinggi : {jumlah_transaksi_sangat_tinggi}")
print(f"Status Target : {status_target}")