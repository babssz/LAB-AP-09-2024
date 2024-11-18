import re
S = input("masukkan: ").strip()
print("True" if len(S)==45 and re.match(r'^[a-zA-Z02468]{40}[13579\s]{5}$', S) else "False")
