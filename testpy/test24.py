# Operasi BitWise ( Operasi Biner )

a = 9
b = 5
c = a | b

print(f"nilai   : {a} binary    : {format(a, '08b')}")
print(f"nilai   : {b} binary    : {format(b, '08b')}")
print(f"nilai   : {c} binary   : {format(c, '08b')}")
print("==================================================")
# And
c = a & b
print(f"nilai   : {a} binary    : {format(a, '08b')}")
print(f"nilai   : {b} binary    : {format(b, '08b')}")
print(f"nilai   : {c} binary   : {format(c, '08b')}")
print("==================================================")
# XOR
c = a ^ b
print(f"nilai   : {a} binary    : {format(a, '08b')}")
print(f"nilai   : {b} binary    : {format(b, '08b')}")
print(f"nilai   : {c} binary   : {format(c, '08b')}")
print("==================================================")
# And
c = ~a
print(f"nilai   : {a} binary    : {format(a, '08b')}")
print(f"nilai   : {c} binary   : {format(c, '08b')}")
print("==================================================")
c = a >> 2
# Dan kebalikannya
print(f"nilai   : {a} binary    : {format(a, '08b')}")
print(f"nilai   : {b} binary    : {format(b, '08b')}")
print(f"nilai   : {c} binary   : {format(c, '08b')}")
print("==================================================")