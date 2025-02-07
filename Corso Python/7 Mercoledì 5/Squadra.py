#classe squadra

class Squadra:
    def __init__(self, nome, eta):
        self.nome = nome  
        self.eta = int(eta)  
    
    def __str__(self):
        return f"Nome: {self.nome}, Età: {self.eta}"
    
    def descrivi(self):
        return f"Nome: {self.nome}, Età: {self.eta}"

#classe giocatore

class Giocatore(Squadra):
    def __init__(self, nome, eta, ruolo, numero_maglia):
        super().__init__(nome, eta)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
    
    def __str__(self):
        return f"{super().__str__()}, Ruolo: {self.ruolo}, Numero Maglia: {self.numero_maglia}"
    
    def descrivi(self):
        return f"{super().descrivi()}, Ruolo: {self.ruolo}, Numero Maglia: {self.numero_maglia}"

    def gioca_partita(self):
        print(f"{self.nome}, {self.ruolo}, numero {self.numero_maglia} sta giocando la partita.")

#classe allenatore

class Allenatore(Squadra):
    def __init__(self, nome, eta, anni_di_esperienza):
        super().__init__(nome, eta)
        self.anni_di_esperienza = anni_di_esperienza
    
    def __str__(self):
        return f"{super().__str__()}, Anni di Esperienza: {self.anni_di_esperienza}"
    
    def descrivi(self):
        return f"{super().descrivi()}, Anni di Esperienza: {self.anni_di_esperienza}"

    def dirige_allenamento(self):
        print(f"{self.nome}, con {self.anni_di_esperienza} anni di esperienza, sta dirigendo l'allenamento.")

#classe assistente

class Assistente(Squadra):
    def __init__(self, nome, eta, specializzazione):
        super().__init__(nome, eta)
        self.specializzazione = specializzazione
    
    def __str__(self):
        
        return f"{super().__str__()}, Specializzazione: {self.specializzazione}"
    
    def descrivi(self):
        
        return f"{super().descrivi()}, Specializzazione: {self.specializzazione}"

    def supporta_team(self):
        print(f"{self.nome}, {self.specializzazione}, sta supportando il team.")


#Creazione membri della squadra
giocatore1 = Giocatore("Mario", 20, "Ala", 16)
allenatore1 = Allenatore("Conte", 55, 20)
assistente1 = Assistente("Starace", 35, "Preparatore di Caffè")


print(giocatore1.descrivi())  
giocatore1.gioca_partita()  

print(allenatore1.descrivi())  
allenatore1.dirige_allenamento()  

print(assistente1.descrivi())  
assistente1.supporta_team()  

