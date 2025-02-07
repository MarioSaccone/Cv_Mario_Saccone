#definire le aree
def area_triangolo(base, altezza):
    return (base * altezza) / 2

def area_quadrato(lato):
    return lato * lato

def area_rettangolo(base, altezza):
    return base * altezza

def calcolo_area():

    risultati = []

#creazione menù
    while True: 
        print("Benvenuto scegli la forma per cui calcolare l'area: ")
        print("1. Triangolo")
        print("2. Quadrato")
        print("3. Rettangolo")
        print("4. Esci")

        scelta = int(input("Cosa Scegli? 1-4 "))
        if scelta == 1:
            base = float(input("Inserisci la base del triangolo: "))
            altezza = float(input("Inserisci l'altezza del triangolo: "))
            area = area_triangolo(base, altezza)
            print("L'area del triangolo è: ", area_triangolo)
            risultati.append(area)
        
        elif scelta == 2:
            lato = float(input("Inserisci il lato del quadrato: "))
            area = area_quadrato(lato)
            print("L'area del quadrato è: ", area_quadrato)
            risultati.append(area)
        
        elif scelta == 3: 
            base = float(input("Inserisci la base del rettangolo: "))
            altezza = float(input("Inserisci l'altezza del rettangolo: "))
            area = area_rettangolo(base, altezza)
            print("L'area del rettangolo è: ", area_rettangolo)
            risultati.append(area)
        
        elif scelta == 4: 
            print("Hai deciso di uscire.")
            break

        else:
            print("Pippo guarda che hai sbagliato, riprova!")

        print("Risultato: ")
        for i in risultati:
            print(i) 

calcolo_area()