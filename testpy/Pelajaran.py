import os
import platform
from colorama import Fore, Style
import distro
import time
import sympy as sp
from IPython.display import display, Math

f = sp.Function("f")

def clear_screen():
    os.system('clear')

def get_linux_distribution():
    try:
        return distro.id(), distro.version(), distro.name()
    except AttributeError:
        return platform.dist()

def print_system_info():
    system_name = platform.system()

    if system_name.lower() == 'linux':
        distribution, version, kernel = get_linux_distribution()

        supported_distributions = ['kali', 'parrot', 'arch']

        if any(dist.lower() in distribution.lower() for dist in supported_distributions):
            system_info = f"Nama OS: {distribution}"
            version_info = f"Versi OS: {version}"
            kernel_info = f"Versi Kernel: {kernel}"
            print(f"{Fore.CYAN}{system_info}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{version_info}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{kernel_info}{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.RED}Sistem operasi tidak didukung.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Script ini hanya mendukung sistem operasi Linux.{Style.RESET_ALL}")

# Fungsi untuk menampilkan teks dengan efek mengetik dari kiri ke kanan
def type_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)  # Adjust the sleep duration to control typing speed
    print()

# Contoh pemanggilan fungsi
clear_screen()
print_system_info()
type_text("""
 _    _      _ _                            _        
| |  | |    | | |                          | |       
| |  | | ___| | | ___ ___  _ __ ___   ___  | |_ ___  
| |/\| |/ _ \ | |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \ 
\  /\  /  __/ | | (_| (_) | | | | | |  __/ | || (_) |
 \/  \/ \___|_|_|\___\___/|_| |_| |_|\___|  \__\___/ 
                                                     
                                                     
 _     _ _                                           
| |   (_) |                                          
| |    _| |__  _ __ __ _ _ __ _   _                  
| |   | | '_ \| '__/ _` | '__| | | |                 
| |___| | |_) | | | (_| | |  | |_| |                 
\_____/_|_.__/|_|  \__,_|_|   \__, |                 
                               __/ |                 
                              |___/                  
""")

def print_menu(options):
    for i, option in enumerate(options, 1):
        print(f"{Fore.RED}{i}.{Style.RESET_ALL} {Fore.YELLOW}{option}{Style.RESET_ALL}")

def main_menu():
    clear_screen()
    print_system_info()
    print_menu(["Pelajaran", "Python", "Latihan"])
    user_choice = input("Pilihlah pilihan berikut (1-3): ")
    
    if user_choice == '1':
        matematika_menu()
    elif user_choice == '2':
        python_menu()
    elif user_choice == '3':
        latihan_menu()
    else:
        print(f"{Fore.RED}Pilih yang bener lah!{Style.RESET_ALL}")
        input("Tekan Enter untuk melanjutkan...")
        main_menu()

def matematika_menu():
    clear_screen()
    print_system_info()
    print_menu(["Matematika", "Bahasa Inggris", "Program"])
    user_choice = input("Pilih pelajaran apa (1-3): ")
    x, a = sp.symbols('x a')
    f = sp.Function('f')(x)
    f_x = sp.limit(f, x, sp.oo)

    # Handle user choice here...
    if user_choice == '1':
        type_text("Anda memilih Matematika")
        print("Matematika: Limit Fungsi")

        print("\nLimit fungsi adalah konsep dalam matematika yang menggambarkan perilaku suatu fungsi saat variabel inputnya mendekati suatu nilai tertentu.")
        print("Limit digunakan untuk memahami nilai yang diharapkan dari suatu fungsi saat variabelnya mendekati suatu titik tanpa benar-benar mencapainya.")
        print(f"Dalam notasi matematika, limit fungsi {f_x} saat x mendekati a dapat dituliskan sebagai:")
        print("\n")
        display(Math(r'\lim_{{x \to \infty}} f(x)'))
        print("\n")
        print("Limit memiliki beberapa sifat fundamental, seperti sifat keunikan dan sifat operasi limit, yang memungkinkan kita untuk memanipulasi dan memahami batasan fungsi dengan lebih baik.")
        print("Konsep limit sangat penting dalam kalkulus, di mana digunakan untuk mendefinisikan turunan dan integral.")
        print("Limit juga membantu dalam memahami asimtot dan konvergensi deret tak hingga.")
        print("\nOpsi:")
        print("0. Kembali")
        print("1. Lanjutkan ke halaman selanjutnya")
        user_choice_limit = input("Pilih opsi (0-1): ")

        if user_choice_limit == '0':
            main_menu()
        elif user_choice_limit == '1':
            # Implementasikan logika untuk halaman selanjutnya jika diperlukan
            print("Implementasikan halaman selanjutnya di sini.")
            input("Tekan Enter untuk melanjutkan...")
            pelajaran_menu()
        else:
            print(f"{Fore.RED}Pilihan tidak valid. Silakan coba lagi.{Style.RESET_ALL}")
            input("Tekan Enter untuk melanjutkan...")
            pelajaran_menu()
    elif user_choice == '2':
        type_text("Anda memilih Bahasa Inggris")
    elif user_choice == '3':
        type_text("Anda memilih Program")
    else:
        print(f"{Fore.RED}Pilih yang bener lah!{Style.RESET_ALL}")
        input("Tekan Enter untuk melanjutkan...")
        pelajaran_menu()

def python_menu():
    # Pengecekan sistem operasi
    if platform.system() != 'Linux':
        type_text("Program hanya dapat dijalankan di sistem operasi Linux.")
        return

    clear_screen()
    print_system_info()
    type_text("Menu Python")
    # Add Python menu options here...
    input("Tekan Enter untuk melanjutkan...")

def latihan_menu():
    # Pengecekan sistem operasi
    if platform.system() != 'Linux':
        type_text("Program hanya dapat dijalankan di sistem operasi Linux.")
        return

    # Add logic for the 'Latihan' menu here...
    clear_screen()
    print_system_info()
    type_text("Menu Latihan")
    # Add Latihan menu options here...
    input("Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main_menu()