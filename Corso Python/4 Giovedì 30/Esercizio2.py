#chiedere all'utente di inserire un numero
def sequenza_fibonacci(n): 

    lista = [0, 1]

    while True: 
        fibonacci = lista[-1] + lista [-2]

        if fibonacci > n:
            break
        lista.append(fibonacci)
    
    return lista   

numero = int(input("Scegli un numero: "))

numero_finale = sequenza_fibonacci(numero)
print("la sequenza di fibonacci del numero che hai scelto è ", numero_finale)