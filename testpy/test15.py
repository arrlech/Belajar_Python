def show_menu():
    print("\n")
    print("===============Menu=============")
    print("[1] Tampilkan Data")
    print("[2] Masukkan Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("[5] Keluar")

    menu = int(input("Pilih Menu : "))
    print("\n")

    if menu == 1:
        print("Anda memlih opsi 1!")
    elif menu == 2:
        print("Anda memilih opsi 2")
    elif menu == 3:
        print("Anda memilih opsi 3")
    elif menu == 4:
        print("Anda memilih opsi 4")
    elif menu == 5:
        exit()
    else:
        print("Punya mata gk si lu jing?! yang bener lah itu PILIHAN CUMA ADA 5 PILIH yang BENER LAH JING")

show_menu()