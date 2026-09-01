performa_it = [85, 72, 90, 68, 95, 78]
performa_finance = [80, 88, 75, 92, 70, 85]

semua_performa = performa_it + performa_finance
performa_urut = semua_performa.copy()
performa_urut.sort(reverse=True)

for performa in performa_urut:
    if performa >= 80:
        print(f"Skor : {performa}")

performa_urut.append(98)
nilai_performa = performa_urut.count(85)

total_karyawan = len(performa_urut)
total_skor = sum(performa_urut)
rata_rata = total_skor / total_karyawan
skor_tertinggi  = max(performa_urut)
skor_terendah = min(performa_urut)


print()
print(f"Jumlah Karyawan : {total_karyawan}")
print(f"Total Skor : {total_skor}")
print(f"Rata-rata Performa : {rata_rata:.2f}")
print(f"Skor Tertinggi : {skor_tertinggi}")
print(f"Skor Terendah : {skor_terendah}")
print(f"Jumlah Skor 85 : {nilai_performa}")