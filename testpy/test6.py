#Greet to user
print("Hello... I am a program that Arlech made you can ask me anything")

#List buah
buah = ["Jeruk", "Semangka", "Apel", "anggur"]
print(buah)

#Var nambah buah/ngurangin buah
print("""\nMenambah/Mengurangi
1. Apa kamu mau menambahkan buah baru ke dalam list di atas?
2. Apa kamu mau mengurangi buah dari list di atas?""")

pilihan = int(input("Pilihan: "))

if pilihan not in [1, 2]:
    print("Gausah gajelas baca njing!!!")

else:
        if pilihan == 1:
            buah_baru = input("Nama buah baru: ")
            buah.append(buah_baru)
            print(f"Buah {buah_baru} telah ditambahkan ke dalam List. List sekarang: {buah}")
        if pilihan == 2:
            buah_hapus = input("Nama buah yang ingin dihapus: ")
            buah.remove(buah_baru)
            print(f"Buah {buah_baru} telah dihapus dari list. List sekarang: {buah}")
        else:
            print(f"buah {buah_baru} Tidak ada di dalam List.")

potongan = buah[1:3]
print(potongan)
        