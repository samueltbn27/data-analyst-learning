branch_data = [
    ["Bandung", [4000000, 6500000, 3000000]],
    ["Jakarta", [8000000, 4500000, 7000000]],
    ["Surabaya", [2500000, 9000000, 5500000]],
    ["Medan", [3500000, 6000000, 2000000]]
]

target = 30000000

i = 0
jumlah_transaksi_kategori_sangat_tinggi = 0
jumlah_transaksi_kategori_rendah = 0
total_seluruh_penjualan_yang_telah_diproses = 0
jumlah_cabang_yang_telah_diproses = 0

while total_seluruh_penjualan_yang_telah_diproses < target and i < len(branch_data):

    cabang = branch_data[i][0]
    transaksi = branch_data[i][1]

    total_transaksi_cabang = 0

    print(f"\nCabang : {cabang}")

    for transaksi_cabang in transaksi:

        if transaksi_cabang >= 8_000_000:
            kategori = "Sangat Tinggi"
            jumlah_transaksi_kategori_sangat_tinggi += 1

        elif transaksi_cabang >= 5_000_000:
            kategori = "Tinggi"

        elif transaksi_cabang >= 3_000_000:
            kategori = "Sedang"

        else:
            kategori = "Rendah"
            jumlah_transaksi_kategori_rendah += 1

        total_transaksi_cabang += transaksi_cabang
        total_seluruh_penjualan_yang_telah_diproses += transaksi_cabang

        print(f"Transaksi : Rp{transaksi_cabang:,.0f} | Kategori : {kategori}")

    jumlah_cabang_yang_telah_diproses += 1

    print(f"Total Cabang {cabang} : Rp{total_transaksi_cabang:,.0f}")

    i += 1


if total_seluruh_penjualan_yang_telah_diproses >= target:
    status = "Target Tercapai"
else:
    status = "Target Belum Tercapai"


print()
print(f"Total Seluruh Penjualan : Rp{total_seluruh_penjualan_yang_telah_diproses:,.0f}")
print(f"Jumlah Cabang Diproses : {jumlah_cabang_yang_telah_diproses}")
print(f"Jumlah Transaksi Sangat Tinggi : {jumlah_transaksi_kategori_sangat_tinggi}")
print(f"Jumlah Transaksi Rendah : {jumlah_transaksi_kategori_rendah}")
print(f"Status Target : {status}")  