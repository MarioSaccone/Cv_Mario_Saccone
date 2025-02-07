# superclasse
class UnitàMilitare:
    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati

    def muovi(self):
        print(f"L'unità {self.nome} si muove verso il campo di battaglia")

    def attacco(self):
        print(f"L'unità {self.nome} attacca l'esercito nemico")

    def ritirata(self):
        print(f"L'unità {self.nome} si ritira dalla battaglia")

# sottoclassi

# sottoclasse fanteria
class Fanteria(UnitàMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def costruisci_trincea(self):
        print(f"L'unità {self.nome} costruisce un riparo")

# sottoclasse artiglieria
class Artiglieria(UnitàMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def calibra_artiglieria(self):
        print(f"L'unità {self.nome} calibra i pezzi dell'artiglieria")

# sottoclasse cavalleria
class Cavalleria(UnitàMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def esplora_terreno(self):
        print(f"L'unità {self.nome} esplora il terreno circostante")

# sottoclasse supporto logitistico
class SupportoLogistico(UnitàMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def rifornisci_unità(self):
        print(f"L'unità {self.nome} rifornisce le altre unità")

# sottoclasse ricognizione
class Ricognizione(UnitàMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def conduci_ricognizione(self):
        print(f"L'unità {self.nome} va in ricognizione")

# classe per il controllo
class ControlloMilitare: 
    def __init__(self):
        self.unità_registrate = {}

    def registra_unità(self, unità):
        self.unità_registrate[unità.nome] = unità  
        print(f"L'unità {unità.nome} è stata registrata correttamente ") 

    def mostra_unità(self):
        if self.unità_registrate:
            print("Unità registrate: ")
            for nome, unità in self.unità_registrate:
                unità = self.unità_registrate[nome]
                print(f"Unità {nome}, Soldati: {unità.numero_soldati}")
        else:
            print("Nessuna unità registrata")
    
    def dettagli_unità(self, nome):
        if nome in self.unità_registrate:
            unità = self.unità_registrate[nome]
            print(f"Dettagli dell'unità {nome}: ")
            print(f"Numero di soldati: {unità.numero_soldati}")
        else:
            print(f"Unità {nome} non trovata")     

# creazione menù

    def menu(self):
        while True:
            print("Menu:")
            print("1. Registra un'unità")
            print("2. Mostra tutte le unità")
            print("3. Mostra dettagli di un'unità")
            print("4. Modifica un'unità")
            print("5. Rimuovi un'unità")
            print("6. Esci")

# input
        
            scelta = input("Scegli un'opzione (1-6): ")
        
            if scelta == "1":
                nome = input("Inserisci il nome dell'unità: ")
                numero_soldati = int(input("Inserisci il numero di soldati: "))
                tipo_unità = input("Scegli il tipo di unità (Fanteria, Artiglieria, Cavalleria, SupportoLogistico, Ricognizione): ")
                
                if tipo_unità == "Fanteria":
                    unità = Fanteria(nome, numero_soldati)
                elif tipo_unità == "Artiglieria":
                    unità = Artiglieria(nome, numero_soldati)
                elif tipo_unità == "Cavalleria":
                    unità = Cavalleria(nome, numero_soldati)
                elif tipo_unità == "SupportoLogistico":
                    unità = SupportoLogistico(nome, numero_soldati)
                elif tipo_unità == "Ricognizione":
                    unità = Ricognizione(nome, numero_soldati)
                else:
                    print("Tipo di unità non valido.")
                    continue
                
                self.registra_unità(unità)
            
            elif scelta == "2":
                self.mostra_unità()
                
            elif scelta == "3":
                nome = input("Inserisci il nome dell'unità per vedere i dettagli: ")
                self.dettagli_unità(nome)
                
            elif scelta == "4":
                nome = input("Inserisci il nome dell'unità da modificare: ")
                numero_soldati = int(input("Inserisci il nuovo numero di soldati: "))
                self.modifica_unità(nome, numero_soldati)
                
            elif scelta == "5":
                nome = input("Inserisci il nome dell'unità da rimuovere: ")
                self.rimuovi_unità(nome)
                
            elif scelta == "6":
                print("Uscendo dal programma...")
                break
            else:
                print("Opzione non valida, riprova.")

# avvio programma

controllo = ControlloMilitare()
controllo.menu()