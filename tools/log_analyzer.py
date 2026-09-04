path_file = input("Masukkan path file log: ")

info = 0
warning = 0
error = 0

with open(path_file, "r") as file:
    for baris in file:
        if "INFO" in baris:
            info += 1
        elif "WARNING" in baris:
            warning += 1
        elif "ERROR" in baris:
            error += 1
            
print("INFO:", info)
print("WARNING:", warning)
print("ERROR:", error)            