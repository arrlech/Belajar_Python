# Operasi Logika Boolean

#not, or, and, xor

print("====================NOT")
a = True
c = not a
print(f"Nilai data boolean = {a} ")
print(f"Nilai data boolean = {c} ")


# OR Jika salah satunya adalah true maka hasilnya adalah True
print("===================OR")
a = True
b = False
c = a or b
print(f"{a} or {b} = {c}")

a = True
b = True
c = a or b
print(f"{a} or {b} = {c}")

a = False
b = False
c = a or b
print(f"{a} or {b} = {c}")

a = False
b = True
c = a and b
print(f"{a} or {b} = {c}")

#JIka 2 buah true maka hasilnya ture
print("====================AND")
a = True
b = False
c = a and b
print(f"{a} and {b} = {c}")

a = True
b = True
c = a and b
print(f"{a} and {b} = {c}")

a = False
b = False
c = a and b
print(f"{a} and {b} = {c}")

a = False
b = True
c = a and b
print(f"{a} and {b} = {c}")

#Hanya akan true jika salah satu true sisanya false
print("====================XOR")
a = True
b = False
c = a ^ b
print(f"{a} XOR {b} = {c}")

a = True
b = True
c = a ^ b
print(f"{a} XOR {b} = {c}")

a = False
b = False
c = a ^ b
print(f"{a} XOR {b} = {c}")

a = False
b = True
c = a ^ b
print(f"{a} XOR {b} = {c}")