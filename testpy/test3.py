# Minimal umur mengakses situs web ini
link = input("Copy your link here to download: ")
umur = int(input("Berapa umur mu? "))

if umur >= 18:
	print("Silahkan Menikmati")
else:
	print("Kamu belum cukup umur bung")

#  Menghitung 1 - 10 
for i in range(10):
	if i == 10:
		break
	if i % 2 == 0:
		continue
	print(i)

# While dari 10 - 1
counter = 10
while counter >= 1:
	print(counter)
	counter -= 1

# List nama buah  buat loop untnuk mencetak setiap nama buah
buah = ["apel", "pisang", "jeruk", "semangka"]

for item in buah:
	print(item)
