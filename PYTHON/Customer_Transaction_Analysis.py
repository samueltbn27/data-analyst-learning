pelanggan_januari = {
    "Samuel",
    "Budi",
    "Andi",
    "Siti",
    "Rina",
    "Budi"
}

pelanggan_februari = {
    "Samuel",
    "Andi",
    "Dina",
    "Siti",
    "Kevin"
}

# 1. Semua pelanggan unik dari Januari dan Februari
pelanggan_unik_kedua_bulan = pelanggan_januari | pelanggan_februari

print("Daftar Pelanggan:")
for nama in pelanggan_unik_kedua_bulan:
    print(f"- {nama}")

# 2. Pelanggan yang hanya melakukan transaksi pada Januari
pelanggan_hanya_januari = pelanggan_januari - pelanggan_februari

print("\nPelanggan yang hanya melakukan transaksi pada Januari:")
for nama in pelanggan_hanya_januari:
    print(f"- {nama}")

# 3. Tambahkan pelanggan baru ke Februari
pelanggan_februari.add("Joko")

print("\nData pelanggan Februari setelah ditambahkan Joko:")
for nama in pelanggan_februari:
    print(f"- {nama}")