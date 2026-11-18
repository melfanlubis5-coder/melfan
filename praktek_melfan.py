nama = input("Masukkan nama barang: ")
stok = int(input("Masukkan stok awal: "))

print()
print("Stok", nama, "sekarang:", stok)
print()

lanjut = "y"   

while lanjut == "y":          
    print("Pilih transaksi:")
    print("1. Barang Masuk")
    print("2. Barang Keluar")
    pilih = input("Masukkan pilihan (1/2): ")

    if pilih == "1":
        masuk = int(input("Jumlah barang masuk: "))
        stok = stok + masuk
        print("Stok bertambah. Stok sekarang:", stok)

    elif pilih == "2":
        keluar = int(input("Jumlah barang keluar: "))
        if keluar > stok:
            print("Stok Tidak Mencukupi")
        else:
            stok = stok - keluar
            print("Stok berkurang. Stok sekarang:", stok)
    else:
        print("Pilihan salah")

    print()
    lanjut = input("Mau transaksi lagi? (y/n): ")   
    print()

print("==============================")
print("Transaksi selesai")
print("Nama barang :", nama)
print("Stok akhir  :", stok)
print("==============================")