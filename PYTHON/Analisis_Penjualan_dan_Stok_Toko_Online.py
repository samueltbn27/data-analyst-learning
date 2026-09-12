penjualan = {
    "Laptop": {
        "kategori": "Elektronik",
        "harga": 7000000,
        "jumlah_terjual": 5,
        "stok": 10
    },
    "Headset": {
        "kategori": "Aksesoris",
        "harga": 500000,
        "jumlah_terjual": 12,
        "stok": 20
    },
    "Mouse": {
        "kategori": "Aksesoris",
        "harga": 350000,
        "jumlah_terjual": 8,
        "stok": 15
    },
    "Keyboard": {
        "kategori": "Aksesoris",
        "harga": 600000,
        "jumlah_terjual": 6,
        "stok": 8
    }
}


# 1. Tampilkan nama produk yang memiliki harga 350000
for produk, detail in penjualan.items():
    if detail["harga"] == 350000:
        print(f"Produk dengan harga Rp350.000 : {produk}")


# 2. Ubah stok Keyboard dari 8 menjadi 5
penjualan["Keyboard"]["stok"] = 5


# 3. Tambahkan key baru "rating" untuk setiap produk
data_rating = {
    "Laptop": 4.8,
    "Headset": 4.5,
    "Mouse": 4.7,
    "Keyboard": 4.6
}

for produk, rating in data_rating.items():
    penjualan[produk]["rating"] = rating

print()

for produk, detail in penjualan.items():
    print(f"{produk} : Rating {detail['rating']}")


# 4. Hitung total pendapatan masing-masing produk
print()

for produk, detail in penjualan.items():
    total = detail["harga"] * detail["jumlah_terjual"]
    print(f"{produk} : Rp{total:,.0f}")


# 5. Hitung total seluruh pendapatan toko
print()

total_pendapatan = 0

for produk, detail in penjualan.items():
    total = detail["harga"] * detail["jumlah_terjual"]
    total_pendapatan += total

print(f"Total Pendapatan Toko : Rp{total_pendapatan:,.0f}")


# 6. Cari produk dengan pendapatan tertinggi
print()

pendapatan_tertinggi = 0
produk_tertinggi = ""

for produk, detail in penjualan.items():
    total = detail["harga"] * detail["jumlah_terjual"]

    if total > pendapatan_tertinggi:
        pendapatan_tertinggi = total
        produk_tertinggi = produk

print(f"Produk dengan Pendapatan Tertinggi : {produk_tertinggi}")
print(f"Pendapatan : Rp{pendapatan_tertinggi:,.0f}")


# 7. Cari produk dengan stok paling sedikit
print()

stok_terendah = float("inf")
produk_stok_terendah = ""

for produk, detail in penjualan.items():
    if detail["stok"] < stok_terendah:
        stok_terendah = detail["stok"]
        produk_stok_terendah = produk

print(f"Produk dengan Stok Paling Sedikit : {produk_stok_terendah}")
print(f"Stok : {stok_terendah}")