# Operasi komparasi

# Setiap hasil dari operasi komparasi adalah boolean

# > < >= <= != is is not

a = 4
b = 2
print("===Ini A===")
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = a >= 3
print(a, '>=', 3, '=', hasil)
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = a != 3
print(a, '!=', 3, '=', hasil)
print("\n===========================\n")
print("===Ini B===")
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b != 3
print(b, '!=', 3, '=', hasil)
print("===============================")
hasil = a != 4
print(a, "!=", 4, "=", hasil)
hasil = b != 4
print(b, "!=", 4, "=", hasil)

# if lelse (komparasi)
# itu semua dapat bekerja pada sintkas literal
# a ==4 (a ada nilai)----> memakan memori (bisa dipanggil di lain lain), (4 literal), (== is membandingkan objek)

# Is sebagai komparasi objek identity
x = 5 # ini aladalh assigmemnt membuat objek
y = 5
print("Nilai x = ", x, "id = ", hex(id(x)))
