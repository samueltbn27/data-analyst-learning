employee_data = [
    ["Andi", 85],
    ["Budi", 72],
    ["Citra", 95],
    ["Dedi", 60],
    ["Eka", 78],
    ["Fajar", 88],
    ["Gina", 65],
    ["Hadi", 92]
]

daftar_nilai = []
daftar_karyawan = []
total_skor = 0
jumlah_sangat_baik = 0
jumlah_baik = 0
jumlah_cukup = 0 
jumlah_kurang = 0
jumlah_di_atas_rata_rata = 0

for i in range(len(employee_data)):

    karyawan = employee_data[i][0]
    skor = employee_data[i][1]

    daftar_nilai.append(skor)
    daftar_karyawan.append(karyawan)

    if skor >= 90:
        kategori = "Sangat Baik"
        jumlah_sangat_baik += 1
    elif skor >= 80:
        kategori = "Baik"
        jumlah_baik += 1
    elif skor >= 70:
        kategori = "Cukup"
        jumlah_cukup += 1
    else:
        kategori = "Kurang"
        jumlah_kurang += 1

    total_skor += skor

    print(f"Karyawan : {karyawan} | Skor : {skor} |  Kategori : {kategori}")

skor_tertinggi = max(daftar_nilai)
skor_terendah = min(daftar_nilai)
jumlah_karyawan = len(daftar_karyawan)
rata_rata_skor = total_skor / jumlah_karyawan


for karyawan, skor in employee_data:
    if skor > rata_rata_skor:
        jumlah_di_atas_rata_rata += 1

print()
print(f"Total Skor : {total_skor}")
print(f"Skor Tertinggi : {skor_tertinggi}")
print(f"Skor Terendah : {skor_terendah}")
print(f"Jumlah Karyawan : {jumlah_karyawan}")
print(f"Rata-rata Skor : {rata_rata_skor}")
print(f"Jumlah Skor Di Atas Rata-rata : {jumlah_di_atas_rata_rata}")
print(f"Jumlah Sangat Baik : {jumlah_sangat_baik}")
print(f"Jumlah Baik : {jumlah_baik}")
print(f"Jumlah Cukup : {jumlah_cukup}")
print(f"Jumlah Kurang : {jumlah_kurang}")