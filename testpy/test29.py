# Operasi dan Manipulasi string

# 1. Menyambung string (concatenate)
nama_pertama = "Ucup"
nama_tengah = "D"
nama_akhir = "fame"

nama_lengkap = nama_pertama+" "+nama_tengah+" "+nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang dari string
panjang = len(nama_lengkap)
print("Panjang dari " + nama_lengkap + " " + str(panjang))

# 3. Operator untuk string

# Mengecek apakah ada komponen char atau string di string

d = "D"
status = d in nama_lengkap
print(status)

D = "d"
status = D in nama_lengkap
print(status)

d = "d"
status = d not in nama_lengkap
print(status)

# Mengulang String
print("wk"*100)

# Indexing
# Kalau -1 ngambil dari belakang

print("index ke-0 : " + nama_lengkap[0])
print("index ke-0 : " + nama_lengkap[1])
print("index ke-0 : " + nama_lengkap[2])
print("index ke-1 : " + nama_lengkap[-2])
print("index ke-2 : " + nama_lengkap[-1])
print("index ke-[0,3]: " + nama_lengkap[0:3+1]) #print("index ke-[0,3]: " + nama_lengkap[0:4])
print("index ke-[0,3]: " + nama_lengkap[0:11:2])

# Item paling kecil
print("Item paling kecil : " + min(nama_lengkap))
print("Item paling gede : " + max(nama_lengkap))

ascii_code = ord(" ")
print("Ascii code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk Ascii adalah " + chr(data))

# 4. Operator dalam bentuk method

data = "Otong Surototong Pararotong"
jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))

