#randomizzatore
import random

def indovina_numero(minimo, massimo):

    numero_casuale = random.randint(minimo, massimo)
    print("Ho scelto un numero tra ", minimo,  massimo, "indovinalo")
    print("Digita '0' se vuoi uscire.")

    #ciclo per indovinare
    while True:
        tentativo = int(input("Inserisci il tuo numero: "))

        if tentativo == 0:
            print("Hai deciso di uscire. Il numero era", numero_casuale)
            break

        if tentativo == numero_casuale:
            print("Complimenti! Hai indovinato il numero!")
            break
        elif tentativo < numero_casuale:
            print("Il numero da indovinare è più alto!")
        else:
            print("Il numero da indovinare è più basso!")

#richiamo della funzione nel caso si voglia rendere più facile o difficile indovinare il numero
indovina_numero(1, 100)  

