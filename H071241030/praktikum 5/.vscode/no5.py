def caesar_cipher(text, shift):
    hasil = ""
    for karakter in text:
        if karakter.islower():
            hasil += chr((ord(karakter) - ord('a') + shift) % 26 + ord('a'))
        elif karakter.isupper():
            hasil += chr((ord(karakter) - ord('A') + shift) % 26 + ord('A'))
        else:
            hasil += karakter
    return hasil

text = input("Masukkan string: ")
shift = int(input("Masukkan jumlah pergeseran: "))

print(f"Text : {text}")
print(f"Shift: {shift}")
print(f"Cipher: {caesar_cipher(text, shift)}")