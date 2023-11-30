# Episode Latihan logika dan komparasi

# Membuat gabungan are rentang dari angka

inputUser = float(input("Masukkan angka yang bernilai kurang dari 3 atau lebih besar dari 10 : "))

# Daerah 3 Periksa angka jurang dari 3
isKurangdari = (inputUser <= 3)

# Daerah leboh besar dari 10
isLebihDari = (inputUser >= 10)

isCorrect = isKurangdari or isLebihDari
print(isCorrect)

inputUser = float(input("Masukkan angka yang bernilai kurang dari 3 dan lebih besar dari 10 : "))

#Lebih dari 3
isLebihDari = inputUser > 3
print(f"Lebih dari 3 = {isLebihDari}")

#Kurang dari 10
isKurangdari = inputUser < 10
print(f"Kurang dari 10 = {isKurangdari}")

isAnd = isLebihDari and isKurangdari
print(isAnd)

