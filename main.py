from tools.password_checker import password_checker
from tools.file_hash_checker import file_hash_checker
from tools.log_analyzer import log_analyzer
from tools.port_checker import localport_checker
from tools.network_calculator import network_calculator
from tools.system_information import system_information

ulang = True

while ulang:
    print(f"=============================")
    print(f"      🛡️ CYBER TOOLKIT")
    print(f"=============================")
    print(f"[1] Password Strength Checker")
    print(f"[2] File Hash Checker")
    print(f"[3] Log Analyzer")
    print(f"[4] Localhost Port Checker")
    print(f"[5] Network Calculator")
    print(f"[6] System Information")
    print(f"[0] Exit")

    pilihan = input("Pilih menu: ")
    
    match pilihan:
        case "1":
            password_checker()
        case "2":
            file_hash_checker() 
        case "3":
            log_analyzer()
        case "4":
            localport_checker()
        case "5":
            network_calculator()
        case "6":
            system_information()
        case "0":
            print("Terima kasih")
            ulang = False
        case _:
            print("Input tidak valid")
            


