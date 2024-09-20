import random

angka_rahasia = random.randint(1,100)
for i in range(5):
    tebakan = int(input("masukkan angka anda (0 untuk berhenti) : "))
    if tebakan == angka_rahasia :
        print("selamat, angka benar")
        break
    elif tebakan == 0 :
        print("permainan berhenti")
        break
    elif tebakan > angka_rahasia :
        print("angka terlalu besar")
    else:
        print("angka terlalu kecil")
    

if tebakan != angka_rahasia :
    print(f"anda kehabisan percobaan, angka rahasia adalah {angka_rahasia}")