#Membuat program sederhana user memasukkan angka ganjil/genap

user = int(input("Masukkan angka"))

#Output Program

print("Angka yang lu kasih termasuk ke dalam bilangan ", "Genap" if (user % 2 == 0) else "Ganjil")

#Advanced mode

x = int(input("Masukkan angkanya: "))

print("""\nTampilkan Bilangan
1. Ganjil
2. Genap""")

pilihan = int(input("Pilihan: "))


if pilihan not in [1, 2]:
	print("Pilihan Salah")

else:
	for x in range (x + 1):
		if pilihan == 1 and x % 2 == 1:
			print(x, end=', ')
		elif pilihan == 2 and x % 2 == 0:
			print(x, end=', ')

	else:
		print(" ")
#allready fixed

#Password benar/Salah
usr = input("Masukkan username kamu: ")
ps = input("Masukkan Password kamu: ")
ver = "rahasia123"

if ps == ver:
    print("Logging in process...")
else:
    print("Password kamu salah!")