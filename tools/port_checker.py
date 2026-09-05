import socket

nomor_port = int(input("Masukkan nomor port: "))

koneksi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hasil = koneksi.connect_ex(("localhost", nomor_port))

if hasil == 0:
    print("OPEN")
else:
    print("CLOSED")
    
koneksi.closed()