import argparse
import re
from collections import Counter

def ambil_kata_kunci(teks):
    kata_kunci = re.findall(r'\b\w+\b', teks.lower())
    kata_kunci = [kata for kata in kata_kunci if len(kata) > 3]  
    frekuensi_kata = Counter(kata_kunci)
    kata_kunci_terkait = [kata for kata, frekuensi in frekuensi_kata.items() if frekuensi > 1]

    return kata_kunci_terkait

def buat_analogi(teks):
    # Implementasikan cara membuat analogi sesuai kebutuhan
    # Contoh sederhana: Membuat analogi dengan perbandingan ke sesuatu yang umum atau dikenal.
    return f"Contoh analogi: {teks.lower()}"

def rangkum_teks(teks, fokus_topik, poin_khusus, penjelasan_sederhana, tampilkan_analogi):
    # Fokus pada topik utama
    topik_utama = fokus_topik if fokus_topik else "Topik utama belum ditentukan."

    # Menekankan poin-poin khusus
    poin_khusus = poin_khusus if poin_khusus else "Poin khusus belum ditentukan."

    # Menjelaskan dengan analogi atau penjelasan sederhana
    penjelasan_sederhana = penjelasan_sederhana if penjelasan_sederhana else "Penjelasan disederhanakan belum diimplementasikan."

    # Menampilkan seluruh kata kunci terkait
    kata_kunci = ambil_kata_kunci(teks)

    # Membuat rangkuman
    rangkuman = f"""
    Rangkuman:

    1. Topik Utama: {topik_utama}
    2. Poin Khusus: {poin_khusus}
    3. Penjelasan Sederhana: {penjelasan_sederhana}
    4. Kata Kunci Terkait: {', '.join(kata_kunci)}
    """

    # Menampilkan analogi jika diperlukan
    if tampilkan_analogi:
        analogi = buat_analogi(teks)
        rangkuman += f"\n5. Analogi: {analogi}"

    return rangkuman

def main():
    parser = argparse.ArgumentParser(description="Program Rangkum Teks")
    parser.add_argument("--rangkum", action="store_true", help="Melakukan rangkuman teks.")
    parser.add_argument("-s", "--teks", type=str, help="Teks yang akan dirangkum.")
    parser.add_argument("-ft", "--fokus_topik", type=str, help="Fokus pada topik utama rangkuman.")
    parser.add_argument("-pk", "--poin_khusus", type=str, help="Menekankan poin-poin khusus dalam rangkuman.")
    parser.add_argument("-ps", "--penjelasan_sederhana", type=str, help="Menjelaskan konsep dengan sederhana.")
    parser.add_argument("--analogi", action="store_true", help="Tampilkan analogi dalam rangkuman.")

    args = parser.parse_args()

    if args.rangkum and args.teks:
        hasil_rangkuman = rangkum_teks(args.teks, args.fokus_topik, args.poin_khusus, args.penjelasan_sederhana, args.analogi)
        print(hasil_rangkuman)
    else:
        print("Silakan gunakan opsi --rangkum dan -s/--teks untuk membuat rangkuman teks.")

if __name__ == "__main__":
    main()
