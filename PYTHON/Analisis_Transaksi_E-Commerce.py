customer = "CUST-1025"
jumlah_produk = 7
harga_produk = 125000.50
diskon = 0.15
member = True
stok_tersedia = 5

total_harga_sebelum_diskon = harga_produk * jumlah_produk
nilai_diskon = total_harga_sebelum_diskon * diskon
total_harga_setelah_diskon = total_harga_sebelum_diskon - nilai_diskon

if member ==  True:
    diskon_tambahan = total_harga_setelah_diskon * 0.05
    total_akhir = total_harga_setelah_diskon - diskon_tambahan
else:
    diskon_tambahan = 0
    total_akhir = total_harga_setelah_diskon

if stok_tersedia >= jumlah_produk and member == True:
    proses = "Status Transaksi: BISA DIPROSES"
else:
    proses = "Status Transaksi: TIDAK BISA DIPROSES"



print(f"Customer : {customer}")
print(f"Total Awal : {total_harga_sebelum_diskon:,.2f}")
print(f"Diskon : {nilai_diskon:,.2f}")
print(f"Total Akhir : {total_harga_setelah_diskon:,.2f}")
print(f"Member : {total_akhir:,.2f}")
print(f"Stok Cukup : {proses}")