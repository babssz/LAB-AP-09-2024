baris = int(input("Masukan jumlah baris: "))

if baris % 2 == 0:
    for i in range (1, (baris // 2) + 2//2):
        print(((baris // 2) + 1 - i) * " " + (2*i-1) * "*")
    for i in range ((baris // 2), 0, -1):
        print(((baris // 2) + 1 - i)* " " + (2*i-1) * "*")
else:
    for i in range (1, (baris // 2) + 2):
        print(((baris // 2) + 1 - i) * " " + (2*i-1) * "*")
    for i in range ((baris // 2), 0, -1):
        print(((baris // 2) + 1 - i)* " " + (2*i-1) * "*")