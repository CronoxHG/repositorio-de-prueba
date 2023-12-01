import random

def numeroAleatorio():
    while True:

        numero = random.randint(0, 10)
        usuario = int(input("Adivina el numero (0, 10): "))
        if usuario != numero:
            print("respuesta incorecta")
            usuario = input("quieres volverlo a intentar (s/n):")
            if usuario == "s":
                usuario = int(input("Adivina el numero (0, 10): "))
            elif print("programa finalizado"):
                break 
            else:
                print("Introduce 's' o 'n'")
        else:
            print(f"felicidades el numero {numero} es el correcto")
            break 

numeroAleatorio()

