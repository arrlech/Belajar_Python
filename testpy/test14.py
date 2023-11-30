import requests
from bs4 import BeautifulSoup
import os

def atur_permintaan(proksi=True):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    session = requests.Session()
    session.headers.update(headers)

    if proksi:
        # Add proxy configuration if proksi is True
        proxies = {'http': 'http://192.168.1.1', 'https': 'https://google.com'}
        session.proxies.update(proxies)
    
    return session
# Rest of the code remains unchanged...


def ekstrak_informasi_halaman(html):
    hasil = []
    soup = BeautifulSoup(html, 'html.parser')

    # Contoh ekstraksi judul dan URL dari hasil pencarian Google
    hasil_pencarian = soup.find_all('div', class_='tF2Cxc')

    for hasil_item in hasil_pencarian:
        judul = hasil_item.find('h3').get_text()
        url = hasil_item.find('a')['href']
        hasil.append(f"{judul}: {url}")

    return hasil


def cari_google(query):
    try:
        # Use proxy for Google searches
        session = atur_permintaan(proksi=True)
        
        url = f'https://www.google.com/search?q={query}'
        response = session.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        hasil = ekstrak_informasi_halaman(response.text)
        return hasil
    except requests.exceptions.RequestException as e:
        print(f"Error during Google search: {e}")
        return []

def cari_tor(query):
    # Atur sesi dengan proksi dan header
    session = atur_permintaan()
    
    # Tentukan URL atau endpoint yang sesuai untuk pencarian di Tor
    tor_url = 'https://your_tor_search_api_endpoint'
    
    # Definisikan parameter pencarian
    parameter_pencarian = {'query': query, 'additional_param': 'value'}
    
    # Lakukan permintaan pencarian di Tor
    response = session.get(tor_url, params=parameter_pencarian)
    
    # Ekstrak informasi dari halaman hasil pencarian di Tor
    hasil = ekstrak_informasi_halaman(response.text)
    
    return hasil


def cari_seluruh_sumber(query):
    hasil_google = cari_google(query)
    hasil_tor = cari_tor(query)
    hasil_seluruh_sumber = hasil_google + hasil_tor
    return hasil_seluruh_sumber

def tampilkan_hasil(output):
    # Menampilkan hasil pencarian dengan format yang sesuai
    for i, hasil in enumerate(output, start=1):
        print(f"{i}. {hasil}")
        
def main():
    while True:
        print("=== Mesin Pencari ===")
        print("1. Cari dengan Google")
        print("2. Cari dengan Tor")
        print("3. Cari dengan Seluruh Sumber")
        print("0. Kembali ke Menu Awal")
        print("99. Sudahi (Clear Screen)")
        
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            query = input("Masukkan kata kunci: ")
            hasil = cari_google(query)
            tampilkan_hasil(hasil)

        elif pilihan == "2":
            query = input("Masukkan kata kunci: ")
            hasil = cari_tor(query)
            tampilkan_hasil(hasil)

        elif pilihan == "3":
            query = input("Masukkan kata kunci: ")
            hasil = cari_seluruh_sumber(query)
            tampilkan_hasil(hasil)

        elif pilihan == "0":
            # Kembali ke Menu Awal
            break

        elif pilihan == "99":
            os.system("clear")  # Jika menggunakan sistem operasi Unix/Linux
            # Untuk sistem operasi Windows, gunakan os.system("cls")

        else:
            print("Opsi tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
