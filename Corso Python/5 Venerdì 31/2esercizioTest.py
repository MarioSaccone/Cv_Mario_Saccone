lista_stringhe = []

stringa_uno = str(input("Inserisci la prima stringa: "))
lista_stringhe.append(stringa_uno)

while True:
    stringa_due = str(input("Inserisci la stringa successiva: "))
    if len(stringa_due) >= len(stringa_uno):
        break
    elif len(stringa_due) < len(stringa_uno):
        stringa_uno = stringa_due
    else:
        continue

#mi sono bloccato










        