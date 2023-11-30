import sys
import math

print("""  ____      _            _       _                  
 / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __      
| |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|     
| |__| (_| | | (__| |_| | | (_| | || (_) | |        
 \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|        
/ ___|  ___  __| | ___ _ __| |__   __ _ _ __   __ _ 
\___ \ / _ \/ _` |/ _ \ '__| '_ \ / _` | '_ \ / _` |
 ___) |  __/ (_| |  __/ |  | | | | (_| | | | | (_| |
|____/ \___|\__,_|\___|_|  |_| |_|\__,_|_| |_|\__,_|""")


def penjumlahan(angka_1, angka_2):
    return angka_1 + angka_2

def pengurangan(angka_1, angka_2):
    return angka_1 - angka_2

def perkalian(angka_1, angka_2):
    return angka_1 * angka_2

def pembagian(angka_1, angka_2):
    return angka_1 / angka_2

def perpangkatan(angka_1, angka_2):
    return angka_1 ** angka_2

def pemfaktoran_menu():
    bilangan = int(input("Masukkan bilangan untuk difaktorkan: "))
    faktor = 2
    faktorisasi = []

    while faktor <= bilangan:
        if bilangan % faktor == 0:
            faktorisasi.append(faktor)
            bilangan //= faktor
        else:
            faktor += 1

    print(f"Faktorisasi dari {bilangan} adalah: {faktorisasi}")

def bangun_datar_menu():
    print_menu(["Persegi", "Persegi Panjang", "Segitiga", "Lingkaran", "Segiempat", "Layang Layang"])
    user_choice = input("Pilih Pilihan berikut (1-6): ")

    if user_choice == '1':
        persegi_menu()
    elif user_choice == '2':
        persegi_panjang_menu()
    elif user_choice == '3':
        segitiga_menu()
    elif user_choice == '4':
        lingkaran_menu()
    elif user_choice == '5':
        segiempat_menu()
    elif user_choice == '6':
        layang_layang_menu()

def persegi_menu():
    sisi = float(input("Masukkan panjang sisi: "))
    luas = sisi * sisi
    print(f"Luas Persegi dengan sisi {sisi} adalah {luas}")

def persegi_panjang_menu():
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas = panjang * lebar
    print(f"Luas Persegi Panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}")

def segitiga_menu():
    alas = float(input("Masukkan panjang alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    luas = 0.5 * alas * tinggi
    print(f"Luas Segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas}")

def lingkaran_menu():
    jari_jari = float(input("Masukkan panjang jari-jari: "))
    luas = math.pi * jari_jari ** 2
    print(f"Luas Lingkaran dengan jari-jari {jari_jari} adalah {luas}")

def segiempat_menu():
    # Implement segiempat_menu logic here
    pass

def layang_layang_menu():
    # Implement layang_layang_menu logic here
    pass

def print_menu(options):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

def kalkulator():

    print("""\nMasukan Input
============================
1. Penjumlahan
2. Pengurangan
3. Perkalian
4. Pembagian
5. Bangun Datar
6. Perpangkatan
7. Pemfaktoran
8. FizzBuzz
=============================\n""")

    usr_int = int(input("Masukkan Pilihan: "))
    angka_1 = float(input("Masukkan angka pertama : "))
    angka_2 = float(input("Masukkan angka kedua : "))

    if usr_int in (1, 2, 3, 4, 5, 6, 7):
        print(f"Memilih Opsi {usr_int}")
        if usr_int == 1:
            print(f"{angka_1} + {angka_2} = {penjumlahan(angka_1, angka_2)}")
        elif usr_int == 2:
            print(f"{angka_1} - {angka_2} = {pengurangan(angka_1, angka_2)}")
        elif usr_int == 3:
            print(f"{angka_1} * {angka_2} = {perkalian(angka_1, angka_2)}")
        elif usr_int == 4:
            print(f"{angka_1} / {angka_2} = {pembagian(angka_1, angka_2)}")
        elif usr_int == 5:
            print("Memilih Opsi 5 Bangun Datar")
            bangun_datar_menu()
        elif usr_int == 6:
            print(f"{angka_1} ** {angka_2} = {perpangkatan(angka_1, angka_2)}")
        elif usr_int == 7:
            print("Memilih Opsi 7 Pemfaktoran")
            pemfaktoran_menu()

    if usr_int not in (1, 8):
        print("Invalid (Masukkan angka yang tertera dalam Menu)")
        sys.exit()

if __name__ == "__main__":
    kalkulator()