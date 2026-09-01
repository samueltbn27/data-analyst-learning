produk = (
    ("Laptop", 35, 280000000),
    ("Smartphone", 50, 175000000),
    ("Tablet", 25, 100000000),
    ("Monitor", 40, 120000000)
)

total_penjualan = 0
penjualan_terbesar = 0
produk_terbesar = ""

for nama_produk, jumlah_terjual, penjualan in produk:
    print(f"{nama_produk} - {jumlah_terjual} - {penjualan:,.0f}")

    total_penjualan += penjualan

    if penjualan > penjualan_terbesar:
        penjualan_terbesar = penjualan
        produk_terbesar = nama_produk

print(f"\nTotal Penjualan : {total_penjualan:,.0f}")
print(f"Produk dengan penjualan terbesar : {produk_terbesar} - {penjualan_terbesar:,.0f}")
