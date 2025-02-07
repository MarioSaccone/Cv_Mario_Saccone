class GestorePagamenti:
    def __init__(self, metodo_pagamento):
        self.metodo_pagamento = metodo_pagamento
    
    def pagamento(self, importo):
        self.metodo_pagamento.effettua_pagamento(importo)

class Carta_di_credito:
    def effettua_pagamento(self, importo):
        print(f"Pagamento di Euro: {importo} fatto con Carta di Credito")

class PayPal:
    def effettua_pagamento(self, importo):
        print(f"Pagamento di Euro: {importo} fatto tramite PayPal")

class Bonifico:
    def effettua_pagamento(self, importo):
        print(f"Pagamento di Euro: {importo} fatto con Bonifico Bancario")

while True:
    metodo = input("Come preferisci pagare? (Carta, Paypal, Bonifico, Esci): ")
    if metodo == "Esci":
        break
    importo = int(input("Inserisci l'importo del pagamento: "))
    
    if metodo == "Carta":
        gestore = GestorePagamenti(Carta_di_credito())
    elif metodo == "Paypal":
        gestore = GestorePagamenti(PayPal())
    elif metodo == "Bonifico":
        gestore = GestorePagamenti(Bonifico())
    else:
        print("Metodo non valido, riprova.")
        continue
    
    gestore.pagamento(importo)