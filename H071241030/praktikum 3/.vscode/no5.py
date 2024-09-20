populasi_awal_A = int(input("Masukkan populasi awal Serangga A: "))
populasi_awal_B = int(input("Masukkan populasi awal Serangga B: "))
hari = int(input("Masukkan jumlah hari: "))


for hari in range(1, hari + 1):
    if hari % 2 == 1:
        populasi_awal_A = int(populasi_awal_A * 1.3)
        populasi_awal_B = int(populasi_awal_B * 1.5)
    else:
        populasi_awal_A = int(populasi_awal_A * 0.8)
        populasi_awal_B = int(populasi_awal_B * 0.6)
    if hari % 5 == 0:
        populasi_awal_A = int(populasi_awal_A * 0.9)
        populasi_awal_B = int(populasi_awal_B * 0.9)
        print(f"hari {hari} : predator memakan 10% populasi")

    
    print(f"Hari {hari}: Serangga A = {populasi_awal_A:.0f}, Serangga B = {populasi_awal_B:.0f}")