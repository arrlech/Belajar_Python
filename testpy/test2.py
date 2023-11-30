import test1

test1.my_function()

#variabel soal 1 true/false
nama = input("Siapa nama anda? ")
nama_belakang = input("Apa nama belakang anda? ")
usia = int(input("berapakah usia anda saat ini? "))
hasil = int(input("Berapakah hasil ujian bahasa inggris kamu? "))
#meminta user memasukkan 2 angka, hitung jumlah pengurangan perkalian dan pembagian tampilkan hasillnya
a = int(input("nilai a: "))
b = int(input("nilai b: "))

c = a + b 
print("Hasil ", (c))
c = a - b
print("hasil ", (c))
c = a * b
print("Hasil ", (c))
c = a / b
print("Hasil ", (c))

print(f"Hallo, " + nama + nama_belakang)


#pernyataan lulus atau tidak 
if 70 > hasil:
	print("Maaf kamu tidak lulus, coba lagi ya jangan patah semangat!")
else:
	print("Selamat kamu Lulus jangan berhenti belajar ya tetap pertahankan")

#pernyataan diskon pelajar 80%
if 18 > usia:
	print("Selamat, kamu mendapatkan diskon pelajar!")
else:
	print("Maaf kamu terlalu tua untuk mendapatkan diskon!")

#Luas persegi panjang
a = int(input("panjang: "))
b = int(input("Lebar: "))

c = a * b
print("Hasil: ", (c))
