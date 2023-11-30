import math
# X adalah variabel | dan nilai nya (2) adalah value | = adalah assignment
# Variabel adalah tempat menyimpan data
# Operasi matematika bangun datar Persegi
# Memebuat Pilihan
print("""\nTampilkan Bilangan
1. Luas
2. Keliling
3. Panjang Luas""")
("\n")
# Memberikan user untuk menginput Pilihan yang diberikan
pilihan = int(input("Pilihan: "))
# Jika tidak ada dalam daftar piihan maka dainggap tidak valid
if pilihan not in [1, 2, 3]:
    print("Pilihan anda salah")
# Memberikan opsi jika user memilih 1, 2 ,3 apa yang akan di tampilkan
else:
# Jika user menginput opsi 1 ini yang akan ditampilkan
    if pilihan == 1:
        print("Anda mencari luas Persegi")
        sisi = float(input("Masukkan panjang sisi \t: "))
        print(f"Apakah yang anda masukkan sudah benar Panjang sisi dari persegi adalah: {sisi}")
        luas_persegi = sisi**2
        print("\nLuas Persegi \t\t:",luas_persegi)
# Ending dari Opsi 1
# Jika user menginput opsi 2 ini yang akan ditampilkan
    if pilihan == 2:
        print("Anda Mencari Keliling Persegi")
        sisi = float(input("Masukkan panjang sisi \t: "))
        print(f"Apakah yang anda masukkan sudah benar Panjang sisi dari persegi adalah: {sisi}")
        keliling_persegi = 4 * sisi
        print("Keliling Persegi\t:",keliling_persegi)
# Ending dari Opsi 2

    if pilihan == 3:
        print("Anda Mencari Panjang sisi Persegi")
        luas_persegi = float(input("Masukkan panjang sisi persegi \t: "))
        print(f"Apakah yang anda masukkan sudah benar Panjang sisi dari persegi adalah: {luas_persegi}")
        sisi = math.sqrt(luas_persegi)
        print("\nSisi persegi \t\t:", sisi)