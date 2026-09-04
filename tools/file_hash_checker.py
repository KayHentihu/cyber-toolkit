import hashlib

path_file = input("Masukkan path file: ")

try:
    with open(path_file, "rb") as file:
        data = file.read()
        hash_object = hashlib.sha256(data)
    print(hash_object.hexdigest())
except FileNotFoundError:
    print("Maaf File tidak ditemukan!!")
