# Operator dalam bentuk method

## Merubah case dari string

# merubah semua ke uppercase

salam = "Anneyong"
print(salam)
salam = salam.upper()
print(salam)

alay = "Alay lo ngengtod"
print(alay)
alay = alay.lower()
print(alay)

## Pengecekan dengan isX method

# Contoh untuk pengecekan lowercase
salam = "sis"

apakah_lower = salam.islower()
apakah_upper = salam.isupper()

print(salam + " is lower = " + str(apakah_lower))
print(salam + " is lower = " + str(apakah_upper))

# isalpha() --> Untuk mengecek semuanya huruf
# isalum() --> Huruf dan angka
# isdecimal() --> angka saja
# isspace --> spasi, tab, newline \n
# istitle() --> semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Okay"
cek_judul = judul.istitle()
print(judul + " is judul = " + str(cek_judul))

## Ngecek komponen starswitch() endswitch() --> keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim") #.endswitch("Sangjiangnim") --> liat apakaha kata nya benber apa engga
print("start = " + str(cek_start))

## Penggabungan kompoenen join() split()
# List adalah kumpulan data
pisah = ['saya', 'anda', 'dia', 'mereka']
gabung = ', '.join(pisah)
print(pisah)
print(gabung)

gabung = " ehm".join(pisah)
print(gabung)

gabungan = "ssaya ehmanda ehmdia ehmmereka"
print(gabungan.split('ehm'))

# Alokasi karakter
kanan = "kanan".rjust(1) #Rjust buat ratain ke kanan ke kiri ljust kalo tengah center
print(kanan)
tengah = "tengah".center(20,":")
print("'"+tengah+"'")

# Kebalikannya --> Strip()
tengah = tengah.strip(":") # Menghilangkan tanda :
print("'"+tengah+"'")
