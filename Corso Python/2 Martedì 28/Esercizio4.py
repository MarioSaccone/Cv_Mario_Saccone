while True:
    numero = int(input("inserisci un numero: "))

    for pippo in range(numero, -1, -1):
        print(pippo)

    ripetizione = input("vuoi ripetere? si/no ")
    if ripetizione == "no":
        break
