#Chiedere all'utente di inserire il numero
numero = int(input("Inserisci il numero positivo: "))

while numero <= 0: 
    print("Il numero non è positivo. Riprova")
    numero = int(input("Inserisci il numero positivo: "))

#menù a scelta 
print("Benvenuto nel menù, puoi scegliere tra le seguenti opzioni:")
print("1. Calcola la somma dei numeri pari da 1 fino al numero inserito precedentemente")
print("2. Stampa tutti i numeri dispari da 1 fino al numero inserito precedentemente")
print("3. Verifica se il numero inserito è un numero primo")
print("4. Esci.")
scelta = int(input("1-4 "))

#opzione 1
if scelta == 1:     
    somma_pari = 0
    for i in range(1, numero, + 1):
        if i % 2 == 0: 
                somma_pari += i
    print("la somma dei numeri pari tra 1 e" , numero, "è", somma_pari)  

#opzione 2 
elif scelta == 2:     
    print("Numeri dispari da 1 a", numero, ":")
    for i in range(1, numero, +1):
        if i % 2 != 0:
             print(i, " ")
    print()