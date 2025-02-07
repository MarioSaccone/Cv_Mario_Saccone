#creazione liste
lista_interi = []
lista_decimali = []
lista_caratteri = []


#numero di iterazioni
x = int(input("Quante volte vuoi far partire il programma? "))
for i in range(x):
    
    #gestione input

    while x <= 0:
        print("Non hai inserito ciò che è richiesto")

        #x = int(input("Quante volte vuoi far partire il programma? "))

    #gestione del menu
    print("Benvenuto nel menù, per favore scegli: ")
    print("1. Immetti il tipo di dato")
    print("2. Esci")
    scelta = int(input("1-2 "))

    #opzione 1
    if scelta == 1: 
        print("Vuoi immettere un dato numerico (1) o alfabetico (2) ? ")
        scelta_dato = int(input(" "))
        if scelta_dato == 1:
            scelta_tipo = int(input("Intero (1) o Decimale (2): "))
            if scelta_tipo == 1:
                intero = int(input("Immetti il numero: "))
                lista_interi.append(intero)
            elif scelta_tipo == 2:
                 decimale = float(input("immetti il numero: "))
                 lista_decimali.append(decimale)
        elif scelta_dato == 2:
            alfabeto = input("Immetti la lettera: ")
            lista_caratteri.append(alfabeto)
    else:    #opzione 2
        break 

#print delle liste
print(lista_interi)
print(lista_decimali)
print(lista_caratteri)
