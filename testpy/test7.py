##Fungsi Sapa user
#nama_pengguna = input("Siapa nama Anda? ")
#
#def sapa(nama):
#    print(f"Halo, {nama}")
#sapa(nama_pengguna)
#
##Fungsi Penjumlahan
#a = int(input("Masukkan angka: "))
#b = int(input("Masukkan angka: "))
##mendefinisikan fungsi tambah
#def tambah(a, b):
#    hasil = a + b
#    return hasil
##manggil fungsi penjumlahan memebrikan angka 1 dan 2 sbagai argumen
#hasil_penjumlahan = tambah(a, b)
##output penumlahan
#
#print(f"Hasil penjumlahan: {hasil_penjumlahan}")
#
#
## Meminta angka dan pangkat dari pengguna
#
#masukkan_angka = int(input("Masukkan angka berapa yang ingin di pangkatkan: "))
#
#angka_dua = int(input("Masukkan angka yang ingin dipangkatkan: "))
#
#
## Mendefinisikan fungsi kuadrat
#
#def kuadrat(angka, pangkat):
#
#    hasil = angka ** pangkat
#
#    return hasil
#
#
## Meminta pangkat dari pengguna
#
#pangkat = int(input("Masukkan mau pangkat berapa: "))
#
#
## Memanggil fungsi kuadrat dengan memberikan angka dan pangkat sebagai argumen
#
#hasil_kuadrat = kuadrat(masukkan_angka + angka_dua, pangkat)
#
#
## Mencetak hasil kuadrat
#
#print(f"Hasil kuadrat: {hasil_kuadrat}")

def penjumlahan(*args):
    total = sum(args)
    return total

def input_angka ():
    angka = []
    while True:
        try:
            nilai = int(input("Masukkan angka (atau ketik 'selesai untuk selesai): "))
            angka.append(nilai)
        except ValueError:
            if input("Ketik 'selesai' untuk mengakhiri input: ").lower() == "selesai":
                break
            else:
                print("Masukkan angka yang valid.")

    hasil = penjumlahan(*angka)
    print(f"Hasil penjumlahan: {hasil}")

input_angka()