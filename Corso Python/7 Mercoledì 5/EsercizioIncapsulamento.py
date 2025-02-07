class ContoBancario:
    def __init__(self, titolare, saldo_iniziale=0.0):
        self.__titolare = None 
        self.__saldo = 0.0  
        self.set_titolare(titolare)  
        self.__saldo = saldo_iniziale if saldo_iniziale >= 0 else 0.0   
    
    # Getter per il titolare
    def get_titolare(self):
        return self.__titolare
    
    # Setter per il titolare con validazione 
    def set_titolare(self, nuovo_titolare):
        if nuovo_titolare and len(str(nuovo_titolare)) > 0:  
            self.__titolare = str(nuovo_titolare)  
        else:
            print("Errore: il nome del titolare deve essere una stringa non vuota.")

    # Metodo per depositare denaro
    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo
            print(f"Deposito di {importo:.2f}€ effettuato. Saldo attuale: {self.__saldo:.2f}€")
        else:
            print("Errore: l'importo del deposito deve essere positivo.")

    # Metodo per prelevare denaro
    def preleva(self, importo):
        if importo > 0 and importo <= self.__saldo:
            self.__saldo -= importo
            print(f"Prelievo di {importo:.2f}€ effettuato. Saldo rimanente: {self.__saldo:.2f}€")
        elif importo > self.__saldo:
            print("Errore: fondi insufficienti per il prelievo.")
        else:
            print("Errore: l'importo del prelievo deve essere positivo.")

    # Metodo per visualizzare il saldo senza modificarlo
    def visualizza_saldo(self):
        return f"Saldo attuale: {self.__saldo:.2f}€"


# Test della classe
conto = ContoBancario("Mario Rossi", 500.0)
print(conto.get_titolare())  
conto.deposita(200)
conto.preleva(100)
print(conto.visualizza_saldo())  
conto.preleva(1000)  
conto.set_titolare("Luca Bianchi")
print(conto.get_titolare())  

