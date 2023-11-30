# Episode input data user

#data = input("Masukkan data: ")

#print("data = ", "type = ", type(data))
#data_float = float(input("Masukkan angka: "))
#
#print("data = ", "type = ", type(data_float))
#
# Bagaimana dengna boolean?
#data_bool = bool (int(input("Masukkan nilai boolean: ")))
#
#print("data = ", "type = ", type(data_bool))

# Operasi Aritmetika

a = 10
b = 3

# Operasi tambah 
hasil = a + b
print(a, '+', b, '=', hasil)

# Operasi perkalian
hasil = a * b
print(a, '*', b, '=', hasil)

# Operasi pengurangan
hasil = a - b
print(a, '-', b, '=', hasil)

# Operasi pembagian
hasil = a / b
print(a, '/', b, '=', hasil)

# Operasi Eksponen (pangkat)
hasil = a ** b
print(a, '**', b, '=', hasil)

# Operasi modulus (sisa pembagian)
hasil = a % b
print(a, '%', b, '=', hasil)

# Operasi floor devision //
hasil = a // b
print(a, '//', b, '=', hasil)

# Prioritas Operasi, Operational precedence

'''
1. ()
2. Eksponen **
3. Perkalian dkk * / ** % //
4. Pertambahan dan pengurangan +  -
'''

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x, '=', hasil)
# Kurung akan mengambil langkah aplikng pertama

