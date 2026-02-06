numero1 = int(input("Digite o numero desejavel:"))
numerolimite = int(input("Limete de multiplicacao:"))

contador = 0

while contador <= numerolimite:
    print(numero1, "x", contador, "=", contador * numero1)
    contador += 1
