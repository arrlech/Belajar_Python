from sympy import symbols, simplify, diff, integrate, sqrt

def kalkulator_rumit():
    print("Selamat datang di Kalkulator Rumit!")
    while True:
        ekspresi = input("Masukkan ekspresi matematika (atau ketik 'selesai' untuk keluar): ")
        
        if ekspresi.lower() == 'selesai':
            print("Terima kasih! Sampai jumpa!")
            break
        
        try:
            x = symbols('x')
            hasil = simplify(ekspresi)
            derivatif = diff(ekspresi, x)
            integral = integrate(ekspresi, x)
            
            print(f"Hasil sederhana: {hasil}")
            print(f"Turunan: {derivatif}")
            print(f"Integral: {integral}")
            
            # Menambahkan fitur tambah, kurang, kali, bagi, pangkat, dan akar
            hasil_evaluasi = eval(ekspresi)
            print(f"Hasil evaluasi: {hasil_evaluasi}")
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    kalkulator_rumit()
