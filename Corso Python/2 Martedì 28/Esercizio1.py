nomeUtente = ""
password = ""
domandaSegreta = ""
rispostaSegreta = ""

#registrazione
print("Benvenuto Registrati!")
print("Per la registrazione Crea un nome utente e una password")

nomeUtente = input("Crea il nome utente ")
password = input("Crea la password ")

#richiesta della domanda segreta
print("Scegli una domanda segreta:")
print("1. Che squadra tifi?")
print("2. Qual è il tuo videogioco preferito?")
domandaSegreta = input("Scegli 1 o 2: ")

if domandaSegreta == "1":
    rispostaSegreta = input("Qual è la tua squadra del cuore? ")
elif domandaSegreta == "2":
    rispostaSegreta = input("Qual è il tuo videogioco preferito? ")
else:
    print("Domanda non valida. Registrazione fallita.")
    exit()

#!=avvenuta registrazione
if(nomeUtente != "" and password != ""):
    print("ti sei registrato correttamente")
else: 
    print("Per continuare devi registrarti!")

#login
print("Per favore effettua il login")

nomeUtente_input = input("Inserisci il nome utente ")
password_input = input("Inserisci la password ")

if(nomeUtente_input == nomeUtente and password_input == password):
    print("Hai effettuato il login con successo!")
else: 
    print("Nome utente o password non corretti. Per Favore Riprova!")
    exit()

#domanda segreta
print("Per confermare l'accesso, rispondi alla domanda segreta.")
print("1. Che squadra tifi?")
print("2. Qual è il tuo videogioco preferito?")
domandaSegreta_input = input("Scegli 1 o 2: ")

if domandaSegreta_input == domandaSegreta:
    if domandaSegreta_input == "1":
        risposta_input = input("Qual è la tua squadra del cuore? ")
    elif domandaSegreta_input == "2":
        risposta_input = input("Qual è il tuo videogioco preferito? ")
    if(risposta_input == rispostaSegreta):
        print("Autenticazione riuscita")
    else:
        print("Risposta errata. Accesso negato.")
    exit()
else:
    print("Domanda non valida. Accesso negato.")
    exit()
    
#modifica dati del programma
modifica = input("Vuoi modificare il nome utente o la password? Sì/No: ")

if modifica == "Sì":
    scelta = input("Cosa vuoi modificare: nome utente o password? ")
    if scelta == "nome utente":
        nomeUtente = input("Modifica il nome utente: ")
        print("Nome utente modificato con successo.")
    elif scelta == "password":
        password = input("Modifica la password: ")
        print("Password modificata con successo.")
    else:
        print("Torno indietro.")
elif modifica == "No":
    print("Torno indietro")
else:
    print("Torno indietro.")
