nama = "Samuel"
jabatan = "Data Analyst"
gaji_pokok = 8500000.50
bonus = 1250000.75
kehadiran = 22
target_kehadiran = 20
status_karyawan = True

total_pendapatan = gaji_pokok + bonus

if kehadiran >= target_kehadiran and status_karyawan == True:
    diskon_tambahan = total_pendapatan * 0.10
    total_akhir = total_pendapatan - diskon_tambahan

if kehadiran >= target_kehadiran and status_karyawan == True:
    status_karyawan = "LAYAK BONUS"
else:
    status_karyawan = "TIDAK LAYAK BONUS"

if total_akhir >= 10000000:
    kondisi = "TINGGI"
else:
    kondisi = "RENDAH"

print(f"Nama : {nama}")
print(f"Jabatan : {jabatan}")
print(f"Gaji Pokok : {gaji_pokok:,.2f}")
print(f"Bonus : {bonus:,.2f}")
print(f"Total Pendapatan : {total_pendapatan:,.2f}")
print(f"Bonus Tambahan : {diskon_tambahan:,.2f}")
print(f"Total Akhir : {total_akhir:,.2f}")
print(f"Status Karyawan : {status_karyawan}")
print(f"High Income ? {kondisi}")