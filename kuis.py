
print("=" * 50)
print("PROGRAM CEK KELULUSAN UJIAN MATEMATIKA")
print("=" * 50)

# Input nama mahasiswa
nama = input("Masukkan nama mahasiswa: ").strip().title()

# Tentukan target berdasarkan nama
if nama == "Andi":
    target = 70
elif nama == "Budi":
    target = 75
elif nama == "Citra":
    target = 80
else:
    print("Nama tidak terdaftar. Hanya tersedia: Andi, Budi, Citra")
    exit()

print(f"\nHalo {nama}!")
print(f"Target nilai minimal kamu: {target}")
print("-" * 50)

# Inisialisasi variabel
percobaan = 0
lulus = False
maksimal_percobaan = 3

# Perulangan while maksimal 3 kali
while percobaan < maksimal_percobaan:
    percobaan += 1
    nilai = float(input(f"Masukkan nilai ujian ke-{percobaan}: "))
    
    if nilai >= target:
        lulus = True
        print(f"\n{nama} berhasil lulus setelah {percobaan} kali percobaan!")
        break
    else:
        sisa = maksimal_percobaan - percobaan
        if sisa > 0:
            print(f"Nilai {nilai} masih kurang dari target {target}. Sisa kesempatan: {sisa}")
        else:
            print(f"Nilai {nilai} masih kurang dari target {target}.")

# Hasil akhir
print("-" * 50)
if not lulus:
    print(f"{nama} tidak lulus setelah {maksimal_percobaan} kali percobaan!")
print("=" * 50)