usr = input("Masukkan angka pertama: ")
nmb = float(input("Masukkan angka desimal: "))
hasil_jumlah = float(usr) + nmb
print(f"Angka pertama: {usr} dan Angka desimal: {nmb}")
print(f"Hasil jumlah: {hasil_jumlah}")

data_bool = bool(hasil_jumlah)
data_int = int(hasil_jumlah)
data_str = str(hasil_jumlah)

print(f"Angka pertama: ", data_str, "dan Angka desimal: ", data_str)
print(f"Angka pertama: ", data_bool, "dan Angka desimal: ", data_bool)
print(f"Angka pertama: ", data_int, "dan Angka desimal: ", data_int)