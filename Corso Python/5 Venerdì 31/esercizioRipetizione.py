#definire le operazioni
def addizione(numero1, numero2):
    return numero1 + numero2 

def sottrazione(numero1, numero2):
    return numero1 - numero2

def moltiplicazione(numero1, numero2):
    return numero1 * numero2

def divisione(numero1, numero2):
    if numero2 != 0:
        return numero1 / numero2
    else:
        return "Errore: divisione per zero!"

#lista per salvare i risultati
lista_risultati = []

x = int(input("Quanti calcoli vuoi fare? "))

for i in range(x):
    numero1 = float(input("Inserisci il primo numero: "))
    numero2 = float(input("Inserisci il secondo numero "))

#chiedere all'utente quante volte vuole fare un calcolo
    while x <= 0:
        print("Per favore ripeti, inserisci un valore valido")
        x = int(input("Quanti calcoli vuoi fare? "))

#chiedere all'utente che tipo di operazione vuole fare attraverso un menù
    print("Che operazione vuoi fare?")
    print("+")
    print("-")
    print("*")
    print("/")
    print("Esci")
    
    #calcolo delle operazioni
    scelta = input("+ - * / oppure Esci ")

    if scelta == "+":
       risultato = addizione(numero1, numero2)
    elif scelta == "-":
        risultato = sottrazione(numero1, numero2)
    elif scelta == "*":
        risultato = moltiplicazione(numero1, numero2)
    elif scelta == "/":
        risultato = divisione(numero1, numero2)
    else:
        ("Esci")

    
#stampa dei risultati
    lista_risultati.append(risultato)
    
for pippo in lista_risultati:
    print(pippo)

#non ho la minima idea di come implementare una tupla, lo splat e "and or not" all'interno di una calcolatrice ma dato che ormai l'ho fatto rimarrà lì e proverò a fare qualcos'altro

