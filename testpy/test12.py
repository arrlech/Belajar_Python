import sys
import os

# Nama file untuk menyimpan username
nama_file = 'usernames.txt'

def tampilkan_license():
    # Isi dengan teks lisensi atau perjanjian Anda
    license_text = """
    Lisensi Pengguna Akhir

Harap dibaca dengan seksama sebelum menggunakan program ini.

1. Hak Cipta
Program ini dilindungi oleh hak cipta dan merupakan milik dari [Nama Perusahaan atau Pengembang]. Setiap distribusi, reproduksi, atau penggunaan tanpa izin tertulis dilarang.

2. Keterbatasan Tanggung Jawab
Pengembang tidak bertanggung jawab atas kerugian atau kerusakan yang diakibatkan oleh penggunaan program ini. Pengguna bertanggung jawab penuh atas risiko penggunaan program.

3. Lisensi Penggunaan
Dengan menggunakan program ini, pengguna setuju untuk mematuhi semua ketentuan lisensi dan persyaratan yang tercantum di sini. Pengguna tidak diizinkan untuk mengubah, mendistribusikan, atau menjual program ini tanpa izin tertulis dari pengembang.

4. Privasi
Program ini mungkin mengumpulkan beberapa informasi pribadi pengguna untuk keperluan tertentu. Informasi ini akan dijaga kerahasiaannya sesuai dengan kebijakan privasi yang berlaku.

5. Ketentuan Lainnya
[Tambahkan ketentuan lain yang relevan sesuai kebutuhan.]

Dengan melanjutkan penggunaan program ini, pengguna dianggap telah membaca, memahami, dan menyetujui semua ketentuan dan persyaratan dalam lisensi ini.

Terima kasih atas perhatiannya.


    """

    print(license_text)

def tampilkan_username(username):
    print("Selamat datang di Program Anda!")
    print("Nama : " + username)
    print("Status : Hacker")
    print("-" * 28)

def simpan_username(username):
    with open(nama_file, 'a') as file:
        file.write(username + '\n')

def baca_usernames():
    if os.path.exists(nama_file):
        with open(nama_file, 'r') as file:
            usernames_tersimpan = file.read().splitlines()
            return usernames_tersimpan
    else:
        return []

def main_program():
    opsi = input("Apakah Anda setuju dengan perjanjian lisensi? (ya/mungkin/tidak): ").lower()

    if opsi == 'ya':
        username = input("Masukkan username anda: ")
        tampilkan_username(username)
        simpan_username(username)
    elif opsi == 'mungkin':
        usernames_tersimpan = baca_usernames()
        print("Username yang tersimpan:")
        for username in usernames_tersimpan:
            print(username)
    else:
        print("Program tidak dihentikan karena Anda tidak setuju dengan perjanjian lisensi.")
        sys.exit()

tampilkan_license()
main_program()
