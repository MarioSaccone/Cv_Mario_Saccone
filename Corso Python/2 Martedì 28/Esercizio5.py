pari_trovati = 0  

while pari_trovati < 5:  
    numero = int(input("Inserisci un numero: "))
    
    if numero % 2 == 0:  
        pari_trovati += 1  
        print(str(numero) + " è un numero pari!")
    else:
        print(str(numero) + " non è un numero pari.")
    
    if pari_trovati < 5:
        print("Finora hai trovato " + str(pari_trovati) + " numeri pari.")

print("Hai trovato 5 numeri pari, il ciclo si ferma!")
