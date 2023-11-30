data = "ini adalah string"
print(data)
print(type(data))
# 1. Cara buat String

'''
    1. Dengan menggunakan single quote '...'
    2. Menggunakan double quote '...'
'''
data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("Ini adalah hari jum'at")

# 2. Menggunakan tanda \

# Membuat tanda ' ini menjadi string
print('mari beribadah pada hari jum\'at')
print('g\'day, isn\'t it?')

# Backslash ( tanda backslash adalah karkter khusus )
print("C:\\user\\Ucup")

# Tab
print("Ucup\tOtong, jauhan")

# Baclspace
print("Ucup \botong, jadi deketan")

# NewLine
print("Baris pertama.\nBaris kedua.") # LF --> Line feed --> Unix, Linux, MacOS
print("Baris pertama.\rBaris kedua.") # CR --> carriage Return --> Coomodore, Acorn, lisp
print("Baris pertama.\n\nBaris kedua.") # CRLF --> Line Feed Carriage Return --> Dipakai oleh windows

# 3. String Literal atau Raw

# Hati - hati 
print('c:\new folder') # Akan salah pathya
# Menggunakan raw string
print(r'C:\New Folder')

# Multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD
""")

# Multiline literal string dan RAW
print(r"""
Nama : Ucup
kelas : 3
Website : www.dokjassi.com/newID
""")


print("""
Ini adalah catatan dari Arlech
""")

x = ["Jeruk"]
print("Semua x ada {} buah".format(len(x)))

