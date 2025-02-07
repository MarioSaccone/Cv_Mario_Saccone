print("Benvenuto al menu CRUD!")
print("Scegli un'opzione:")
print("1. Aggiungi")
print("2. Rimuovi")
print("3. Elimina")
print("4. Esci")

scelta = input("Inserisci il numero della tua scelta: ")

if scelta == "1":
    print("Hai scelto di aggiungere qualcosa.")
   
    elemento = input("Cosa vuoi aggiungere? ")
    print(elemento + " aggiunto con successo!")

elif scelta == "2":
    print("Hai scelto di rimuovere qualcosa.")
    
    elemento = input("Cosa vuoi rimuovere? ")
    print(elemento + " rimosso con successo!")

elif scelta == "3":
    print("Hai scelto di eliminare tutto.")
    
    conferma = input("Sei sicuro di voler eliminare tutto? (sì/no): ")
    if conferma == "sì":
        print("Tutto eliminato!")
    else:
        print("Operazione annullata.")

else:
    print("Scelta non valida.")
