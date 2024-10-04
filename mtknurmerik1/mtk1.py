def tentukan_nilai():
    nilai = float(input("Masukkan nilai mahasiswa: "))
    if nilai >= 81 and nilai <= 100:
        return "Nilai: A"
    elif nilai >= 69 and nilai <= 80.9:
        return "Nilai: B"
    elif nilai <= 68.9:
        return "Nilai: C"
    else:
        return "Nilai tidak valid. Harap masukkan nilai antara 0 hingga 100."
print(tentukan_nilai())
