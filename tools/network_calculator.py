def network_calculator():
    ip_addres = input("Masukkan IP addres: ")

    bagian_ip = ip_addres.split(".")

    angka_ip = []

    for bagian in bagian_ip:
        angka_ip.append(int(bagian))

    subnet_mask = input("Masukkan Subnet Mask: ")

    bagian_mask = subnet_mask.split(".")

    angka_mask = []

    for bagian in bagian_mask:
        angka_mask.append(int(bagian))
        

    network = []

    for ip, mask in zip(angka_ip, angka_mask):
        network.append(ip & mask)
        
    string_network = []

    for bagian in network:
        string_network.append(str(bagian))

    hasil_network = ".".join(string_network)    
    print(f"Network Address: {hasil_network}")
