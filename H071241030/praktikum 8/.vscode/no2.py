import re

jumlah = int(input("Masukkan jumlah: "))
for i in range(jumlah):
    alamat = input("Masukkan id: ").strip()
    if re.match(r'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$', alamat):
        print("IPv4")
    elif re.match(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$', alamat):
        print("IPv6")
    else:
        print("Bukan ip address")