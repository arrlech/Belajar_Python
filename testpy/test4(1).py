angka = int(input("Masukkan angka yang ingin dibuatkan tabel perkaliannya!:  "))

for a in range(1, 10 + 1):
    print(angka, "X", a, "=", a * angka)

n = int(input("Masukkan jumlah angka dalam deret Fibonacci: "))

a, b = 0, 1
print("Deret Fibonacci:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

angka = int(input("Masukkan angka untuk menghitung faktorial: "))

faktorial = 1
for i in range(1, angka + 1):
    faktorial *= i
    
print(f"Faktorial dari {angka} adalah {faktorial}")

kalimat = input("Masukkan sebuah kalimat: ")

jumlah_a = kalimat.lower().count('a')
print(f"Jumlah huruf 'a' dalam kalimat tersebut adalah: {jumlah_a}")
