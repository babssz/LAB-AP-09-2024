def anagram(string1, string2):
    penghapusan = 0
    semua_karakter = string1 + string2

    for karakter in semua_karakter:
        if semua_karakter.count(karakter) > 0:
            count1 = string1.count(karakter)
            count2 = string2.count(karakter)

            if count1 > count2:
                penghapusan += count1 - count2
            else:
                penghapusan += count2 - count1
            
            semua_karakter = semua_karakter.replace(karakter, '')

    return penghapusan

str1 = input("Masukkan string pertama: ")
str2 = input("Masukkan string kedua: ")

hasil = anagram(str1, str2)
print(f"Jumlah minimum penghapusan untuk membuat anagram: {hasil}")
