#Sistema di stampa pari-dispari
pari_trovati = 0 
dispari_trovati = 0 

numero = int(input("Inserisci un numero: "))

if numero % 2 == 0: 
    pari_trovati += 1
    print(str(numero) + " è un numero pari")
else:
    dispari_trovati += 1
    print(str(numero) + " è un numero dispari")

#Sistema che stampa da n positivo a 0 compreso all'infinito

while True:
    positivo = int(input("Inserisci il numero positivo: "))
    
    for i in range(positivo, -1, -1):
        print(i)

    ripetizione = input("Vuoi continuare? si/no ")
    if ripetizione == "no":
        break

#Sistema che prende l'input di una lista di numeri e ne stampa il quadrato
quanti_numeri = int(input("Quanti numeri vuoi aggiungere alla lista? "))
lista = []

while len(lista)<=quanti_numeri:
    numeri = int(input("Quali numeri vuoi aggiungere alla lista? "))
    lista.append(numeri)
    (print(numeri ** 2))

#Sistema che prende un input di una lista trovando il numero massimo, deve contare quanti numeri sono presenti nella lista e stampare lista vuota se vuota altrimenti deve stampare il numero massimo

numeri= int(input("Quanti numeri vuoi aggiungere alla lista? "))
lista = [int(numero) for numero in numeri.split()]

if len(lista) == 0: print("lista vuota")
else : 
    massimo = lista[0] 
    for numero in lista:
        if numero > massimo :
            massimo = numero

    contatore = 0
    while contatore < len(lista) :
        contatore += 1

print("Il numero masssimo è " ,massimo)
print("il numero " ,numero)


