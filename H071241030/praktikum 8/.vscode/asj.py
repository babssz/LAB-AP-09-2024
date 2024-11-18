# import re 
 
# def is_valid_email(email): 
#     pattern = r"^[a-z]+[0-9]{2,}@[a-z0-9]+\.(com|co\.id|ac\.id)$" # TODO: Buatkan pola RegEx untuk validasi email. 
#     # Sudah ada clue berupa pola untuk mencocokkan domain email. 
#     return re.search(pattern, email) 
 

# email = input("Masukkan email: ") 
# hasil = email.split('@','\n', '.', '\n')    
 
# if is_valid_email(email):  
#     print(f"email valid\n"
#           f"{hasil}")   
# else: 
#     print("\nEmail yang kamu input tidak valid. Registrasi gagal!") 

import re 

def is_valid_email(email): 
    pola = r"^[a-z]+[0-9]{2,}@[a-z0-9]+\.(com|co\.id|ac\.id)$" 
    return re.match(pola, email)

email = input("Masukkan email: ") 

if is_valid_email(email):  
    username, domain = email.split('@')
    a, domain1 = domain.split('.')
    print(f"Email valid\n{username}\n{a}\n{domain1}")   
else: 
    print("\nEmail tidak valid. Registrasi gagal!") 
