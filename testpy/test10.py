a = int(input("Masukkan nilai a: "))
b = int(input("Nasukkan nilai b: "))

c = a & b
print("a & b = " + str(c))
# 0 sama 1 akan tetap 0 1 sama 1 akan tetap 1

c_or = a | b
print("a | b = " + str(c_or))
# 0 sama 1 menjadi 1 dan 0 sama 0 akan tetap 0

c_xor = a ^ b
print("a ^ b = " + str(c_xor))
# 1 sama 1 akan menjadi 0 dan 1 sama 0 akan menjadi 1 0 dan 0 akan tetap 0

c_not = ~a
print("~a = " + str(c_not))
# Dibalikkan

# Notasi bitwise menggunakan binner. tapi kita hanya dapat memasukkan input berupa integer, dan sistem akan menkonfersinya ke binner secara otomatis dan mengubah outputnya menjadi integer kembali supaya dapat dibaca oleh manusia.
#Operasi AND (a & b): Menghasilkan 1 pada bit hasil jika setidaknya satu dari kedua bit yang sesuai adalah 1. Jika kita masukkan a = 13 (biner: 1101) dan b = 9 (biner: 1001), maka hasilnya adalah 1101 & 1001 = 1001 yang setara dengan desimal 9.

#Operasi OR (a | b): Menghasilkan 1 pada bit hasil jika setidaknya satu dari kedua bit yang sesuai adalah 1. Hasilnya adalah 1101 | 1001 = 1101 yang setara dengan desimal 13.

#Operasi XOR (a ^ b): Menghasilkan 1 pada bit hasil jika hanya satu dari kedua bit yang sesuai adalah 1 (bukan keduanya). Hasilnya adalah 1101 ^ 1001 = 0100 yang setara dengan desimal 4.

#Operasi NOT (~a): Menghasilkan kebalikan dari setiap bit; 0 menjadi 1 dan 1 menjadi 0. Dalam kasus ini, karena Anda menggunakan bilangan bulat, hasilnya juga terpengaruh oleh representasi biner yang menggunakan bit sign. Sehingga, ~13 akan menghasilkan -14 dalam sebagian besar lingkungan karena -14 adalah hasil kebalikan dari 13 dalam representasi bit signed integer.