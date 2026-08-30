gudang_data = [
    ["Bandung", [10, 15, 8]],
    ["Jakarta", [20, 12, 25]],
    ["Surabaya", [7, 18, 10]]
]

target_stok = 100

i = 0
total_stok_keluar_seluruh_gudang = 0
jumlah_transaksi_kategori_tinggi = 0
jumlah_gudang_yang_sudah_diproses = 0

while total_stok_keluar_seluruh_gudang < target_stok and i < len(gudang_data):

    kota = gudang_data[i][0]
    stok_keluar = gudang_data[i][1]

    total_gudang = 0

    print(f"\nKota : {kota}")

    for stok in stok_keluar:

        if stok >= 20:
            kategori = "Tinggi"
            jumlah_transaksi_kategori_tinggi += 1

        elif stok >= 10:
            kategori = "Sedang"

        else:
            kategori = "Rendah"

        total_gudang += stok
        total_stok_keluar_seluruh_gudang += stok

        print(f"Stok Keluar : {stok} | Kategori : {kategori}")

    jumlah_gudang_yang_sudah_diproses += 1

    print(f"Total {kota} : {total_gudang}")

    i += 1


if total_stok_keluar_seluruh_gudang >= target_stok:
    status = "Batas Tercapai"
else:
    status = "Batas Belum Tercapai"


print()
print(f"Total Stok Keluar : {total_stok_keluar_seluruh_gudang}")
print(f"Jumlah Gudang Diproses : {jumlah_gudang_yang_sudah_diproses}")
print(f"Jumlah Transaksi Tinggi : {jumlah_transaksi_kategori_tinggi}")
print(f"Status : {status}")