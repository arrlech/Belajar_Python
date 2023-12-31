# Width and Multinline

# Data

data_nama = "ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

# String
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu} "
print(5*"="+"Data String"+5*"=")
print(data_string)

# String Multiline
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu} "
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# String Multiline (Kutip Triplets)

data_string = f"""
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# Mengatur lebar
data_string = f"""
nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)