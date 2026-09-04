pelanggan_maret = {
    "Andi",
    "Budi",
    "Citra",
    "Dina",
    "Eko"
}

pelanggan_april = {
    "Budi",
    "Citra",
    "Fajar",
    "Gita",
    "Dina"
}

pelanggan_unik_maret_april = pelanggan_maret | pelanggan_april
print("Pelanggan seluruh dari Maret dan April :")
for index, nama in enumerate(pelanggan_unik_maret_april, start=1):
    print(f"{index}. {nama}")

pelanggan_hanya_maret = pelanggan_maret - pelanggan_april
print("\nPelanggan yang hanya melakukan transaksi pada Maret :")
for index, nama in enumerate(pelanggan_hanya_maret, start=1):
    print(f"{index}. {nama}")

pelanggan_hanya_april = pelanggan_april - pelanggan_maret
print("\nPelanggan yang hanya melakukan transaksi pada April :")
for index, nama in enumerate(pelanggan_hanya_april, start=1):
    print(f"{index}. {nama}")

pelanggan_april.add("Hendra")

pelanggan_april.discard("Fajar")

print("\nHasil Akhir April :")
for index, nama in enumerate(pelanggan_april, start=1):
    print(f"{index}. {nama}")