def acronym(kalimat):
    kata = kalimat.upper().split()
    a = ""
    for i in kata:
        a += i[0]
    return a

print(acronym("Negara Kesatuan Republik Indonesia"))

