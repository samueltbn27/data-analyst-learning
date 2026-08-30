customer_data = [
    ["Andi", [250000, 500000, 750000]],
    ["Budi", [1000000, 1500000, 500000]],
    ["Citra", [300000, 800000, 1200000]],
    ["Dedi", [400000, 600000, 900000]]
]

target_penjualan = 5000000

i = 0
total_seluruh_transaksi_yang_sudah_diproses = 0
jumlah_transaksi_kategori_sangat_besar = 0
jumlah_pelanggan_yang_sudah_diproses = 0

while total_seluruh_transaksi_yang_sudah_diproses < target_penjualan and i < len(customer_data):

    nama = customer_data[i][0]
    harga = customer_data[i][1]

    total_pelanggan = 0

    print(f"\nPelanggan : {nama}")

    for harga_customer in harga:

        if harga_customer >= 1_000_000:
            kategori = "Sangat Besar"
            jumlah_transaksi_kategori_sangat_besar += 1

        elif harga_customer >= 750_000:
            kategori = "Besar"

        elif harga_customer >= 500_000:
            kategori = "Sedang"

        else:
            kategori = "Kecil"

        total_pelanggan += harga_customer
        total_seluruh_transaksi_yang_sudah_diproses += harga_customer

        print(
            f"Transaksi : Rp{harga_customer:,.0f} | "
            f"Kategori : {kategori}"
        )

    jumlah_pelanggan_yang_sudah_diproses += 1

    print(f"Total {nama} : Rp{total_pelanggan:,.0f}")

    i += 1


if total_seluruh_transaksi_yang_sudah_diproses >= target_penjualan:
    status = "Target Tercapai"
else:
    status = "Target Belum Tercapai"


print()
print(f"Total Seluruh Transaksi : Rp{total_seluruh_transaksi_yang_sudah_diproses:,.0f}")
print(f"Jumlah Pelanggan Diproses : {jumlah_pelanggan_yang_sudah_diproses}")
print(f"Jumlah Transaksi Sangat Besar : {jumlah_transaksi_kategori_sangat_besar}")
print(f"Status Target : {status}")