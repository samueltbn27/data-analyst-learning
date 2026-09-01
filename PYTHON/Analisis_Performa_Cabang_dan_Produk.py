penjualan = (
    ("Bandung", "Laptop", 25, 200000000),
    ("Jakarta", "Smartphone", 40, 180000000),
    ("Surabaya", "Laptop", 30, 240000000),
    ("Medan", "Monitor", 20, 90000000),
    ("Bandung", "Smartphone", 35, 157500000),
    ("Jakarta", "Laptop", 15, 120000000),
)

# Variabel perhitungan
total_seluruh_penjualan = 0
penjualan_terbesar = 0
penjualan_kota_terbesar = ""
penjualan_produk_terbesar = ""

target_produk = "Laptop"
total_khusus_laptop = 0

total_unit = 0

# Menyimpan total unit berdasarkan produk
total_produk = {}

for kota, produk, terjual, total_penjualan in penjualan:

    # Menampilkan data
    print(f"{kota} - {produk} - {terjual} unit - Rp{total_penjualan:,.0f}")

    # 1. Total seluruh penjualan
    total_seluruh_penjualan += total_penjualan

    # 2. Mencari penjualan terbesar
    if total_penjualan > penjualan_terbesar:
        penjualan_terbesar = total_penjualan
        penjualan_kota_terbesar = kota
        penjualan_produk_terbesar = produk

    # 3. Total khusus Laptop
    if produk == target_produk:
        total_khusus_laptop += total_penjualan

    # 4. Total seluruh unit
    total_unit += terjual

    # 5. Menghitung total unit berdasarkan produk
    if produk in total_produk:
        total_produk[produk] += terjual
    else:
        total_produk[produk] = terjual


# Mencari produk dengan jumlah unit terbanyak
unit_terbesar = 0
produk_unit_terbesar = ""

for produk, unit in total_produk.items():
    if unit > unit_terbesar:
        unit_terbesar = unit
        produk_unit_terbesar = produk


# Output
print(f"\nTotal Seluruh Penjualan : Rp{total_seluruh_penjualan:,.0f}")

print(
    f"Penjualan Terbesar : "
    f"{penjualan_kota_terbesar} - "
    f"{penjualan_produk_terbesar} - "
    f"Rp{penjualan_terbesar:,.0f}"
)

print(
    f"Total Penjualan Khusus Produk Laptop : "
    f"Rp{total_khusus_laptop:,.0f}"
)

print(f"Jumlah Seluruh Unit Yang Terjual : {total_unit}")

print(
    f"Produk dengan jumlah unit terjual terbanyak : "
    f"{produk_unit_terbesar} - {unit_terbesar} unit"
)