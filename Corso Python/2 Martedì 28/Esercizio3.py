#chiedere all'utente che tipo di operazione vuole eseguire
numero1 = float(input("inserisci il primo numero "))
numero2 = float(input("inserisci il secondo numero "))


scelta = input("scegli tra i seguenti operatori: +, -, *, / ")

if scelta == "+":
    print(numero1 + numero2)
elif scelta == "-":
    print(numero1 - numero2)
elif scelta == "*":
    print(numero1 * numero2)
elif scelta == "/":
    if numero2 == 0:
        print("impossibile dividere per 0")