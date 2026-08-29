sales_data = [
    ["Laptop", 12000000],
    ["Mouse", 750000],
    ["Keyboard", 1500000],
    ["Monitor", 4500000],
    ["Headset", 900000],
    ["Printer", 6000000],
    ["Webcam", 1200000],
    ["Camera", 8500000]
]

daftar_harga = []
total_penjualan = 0

for i in range(len(sales_data)):

    produk = sales_data[i][0]
    harga = sales_data[i][1]

    daftar_harga.append(harga)

    if harga >= 10_000_000:
        kategori = "Sangat Tinggi"
    elif harga >= 5_000_000:
        kategori = "Tinggi"
    elif harga >= 1_000_000:
        kategori = "Sedang"
    else:
        kategori = "Rendah"

    total_penjualan += harga

    print(
        f"Produk : {produk} | "
        f"Penjualan : Rp{harga:,.0f} | "
        f"Kategori : {kategori}"
    )


penjualan_tertinggi = max(daftar_harga)
penjualan_terendah = min(daftar_harga)
jumlah_produk = len(sales_data)
rata_rata = total_penjualan / jumlah_produk

print()

print(f"Total Penjualan : Rp{total_penjualan:,.0f}")
print(f"Penjualan Tertinggi : Rp{penjualan_tertinggi:,.0f}")
print(f"Penjualan Terendah : Rp{penjualan_terendah:,.0f}")
print(f"Jumlah Produk : {jumlah_produk}")
print(f"Rata-rata Penjualan : Rp{rata_rata:,.0f}")