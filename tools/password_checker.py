input_password = input("Masukkan password: ")

huruf = False
angka = False
simbol = False

for nilai in input_password:
    if nilai.isalpha():
        huruf = True
    elif nilai.isdigit():
        angka = True
    else:
        simbol = True

strong = huruf and angka and simbol and len(input_password) >= 8
two_types = (huruf and angka) or (huruf and simbol) or (simbol and angka)
if strong:
    print("STRONG")
elif two_types:
    print("MEDIUM")
else:
    print("WEAK")