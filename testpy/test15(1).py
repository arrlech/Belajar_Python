class Menu:
    def __init__(self, label, action):
        self.label = label
        self.action = action

def tampilkan_data():
    print("Anda memilih opsi 1!")

def masukkan_data():
    print("Anda memilih opsi 2")

def edit_data():
    print("Anda memilih opsi 3")

def hapus_data():
    print("Anda memilih opsi 4")

def keluar():
    exit()

def show_menu():
    menu_options = [
        Menu("[1] Tampilkan Data", tampilkan_data),
        Menu("[2] Masukkan Data", masukkan_data),
        Menu("[3] Edit Data", edit_data),
        Menu("[4] Hapus Data", hapus_data),
        Menu("[5] Keluar", keluar)
    ]

    print("\n===============Menu=============")
    for menu in menu_options:
        print(menu.label)

    menu_number = int(input("Pilih Menu : "))

    if 1 <= menu_number <= len(menu_options):
        menu_options[menu_number - 1].action()
    else:
        print("Punya mata gak sih lu jing?! Yang bener lah itu PILIHAN CUMA ADA 5 PILIH yang BENER LAH JING")

show_menu()
