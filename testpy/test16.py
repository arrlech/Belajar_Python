import socket

def start_server():
    # Membuat socket dengan address family IPv4 dan tipe TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Menetapkan alamat dan port server
    server_address = ('localhost', 8080)

    # Mengikat socket ke alamat dan port tertentu
    server_socket.bind(server_address)

    # Mendengarkan koneksi masuk
    server_socket.listen(5)
    print("Server berjalan di", server_address)

    while True:
        # Menunggu koneksi masuk
        print("Menunggu koneksi...")
        client_socket, client_address = server_socket.accept()
        print("Menerima koneksi dari", client_address)

        # Membaca data dari klien
        data = client_socket.recv(1024)
        print(f"Data yang diterima: {data.decode('utf-8')}")

        # Memberikan respons kepada klien
        response = "Terima kasih atas koneksi!"
        client_socket.send(response.encode('utf-8'))

        # Menutup koneksi dengan klien
        client_socket.close()

if __name__ == "__main__":
    start_server()
