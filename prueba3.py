import random
def CreateDni():
    array_lletres = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
    primer_num = random.randint(0,5)
    numero_darrers = ""
    for cnt in range(0,7):
        num = random.randint(0, 9)
        numero_darrers = numero_darrers + str(num)
    numeros = str(primer_num) + str(numero_darrers)
    resto = int(numeros) % 23
    dni = numeros + array_lletres[resto]
    return dni

print(CreateDni())