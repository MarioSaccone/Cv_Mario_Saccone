def decoratore(funzione):
    def wrapper(): 
        print("Prima dell'esecuzione della funzione")
        funzione()
        print("Dopo l'esecuzione della funzione")
    return wrapper

@decoratore
def saluta():
    print("Ciao!")

saluta()

#2
def decoratore_con_argomenti(funzione):
    def wrapper(*args, **kwargs):
        print("prima")
        risultato = funzione(*args, **kwargs)
        print("dopo")
        return risultato
    return wrapper

@decoratore_con_argomenti
def somma(a, b):
    return a + b

print(somma(3, 4))