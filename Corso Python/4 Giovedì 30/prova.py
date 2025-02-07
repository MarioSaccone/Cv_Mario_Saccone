#funzioni di esecuzione
def saluta(nome): #parametro
    print("Ciao,", nome)

saluta("Mario") #argomento

def somma(a, b):
    risultato = a + b
    print("La somma è ", risultato)

somma(5, 3)

#funzioni di ritorno
def quadrato(numero):
    return numero * numero

risultato = quadrato(4)
print(risultato) 

risultato = quadrato(124)
print(risultato)