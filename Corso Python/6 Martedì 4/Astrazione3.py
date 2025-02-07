#classe padre
class Animale:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def fai_suono(self):
        print(f"{self.nome} fa un suono generico.")

#classe figlie
class Leone(Animale):
    def __init__(self, nome, eta, tipo_caccia):
        super().__init__(nome, eta)
        self.tipo_caccia = tipo_caccia 

    def caccia(self):
        print(f"il {self.nome} sta cacciando {self.tipo_caccia}.")

    def fai_suono(self):
        print(f"il {self.nome} ruggisce!")

class Giraffa(Animale):
    def __init__(self, nome, eta, altezza):
        super().__init__(nome, eta)
        self.altezza = altezza  
    def mangia(self):
        print(f"la {self.nome} sta mangiando foglie dagli alberi.")

    def fai_suono(self):
        print(f"la {self.nome} landisce.")

class Pinguino(Animale):
    def __init__(self, nome, eta, regione):
        super().__init__(nome, eta)
        self.regione = regione  

    def nuota(self):
        print(f"il {self.nome} sta nuotando nel ghiaccio!")

    def fai_suono(self):
        print(f"il {self.nome} fa un suono diverso in base alla specie!")

#vari print
leone = Leone("Leone", 5, "antilope")
giraffa = Giraffa("Giraffa", 8, 4.5)
pinguino = Pinguino("Pinguino", 3, "Antartide")


leone.fai_suono()  
giraffa.fai_suono()  
pinguino.fai_suono()  


leone.caccia()  
giraffa.mangia()  
pinguino.nuota() 


#secondo esercizio
#Prima classe padre 
class Veicolo:
    def __init__(self, modello, anno_produzione):
        self.modello = modello
        self.anno_produzione = anno_produzione

    def descrizione(self):
        return f"Modello: {self.modello}, Anno: {self.anno_produzione}"


#Seconda classe padre 
class Motore:
    def __init__(self, tipo_carburante):
        self.tipo_carburante = tipo_carburante

    def rifornisci(self):
        return f"Rifornimento effettuato con {self.tipo_carburante}"


#Classi figlie
class Auto(Veicolo, Motore):
    def __init__(self, modello, anno_produzione, tipo_carburante, posti):
        Veicolo.__init__(self, modello, anno_produzione)
        Motore.__init__(self, tipo_carburante)
        self.posti = posti

    def descrizione(self):
        return f"Auto: {self.modello}, Anno: {self.anno_produzione}, Posti: {self.posti}, Carburante: {self.tipo_carburante}"



class Bicicletta(Veicolo):
    def __init__(self, modello, anno_produzione, tipo):
        super().__init__(modello, anno_produzione)
        self.tipo = tipo  

    def descrizione(self):
        return f"Bicicletta: {self.modello}, Anno: {self.anno_produzione}, Tipo: {self.tipo}"


class ScooterElettrico(Veicolo):
    def __init__(self, modello, anno_produzione, autonomia):
        super().__init__(modello, anno_produzione)
        self.autonomia = autonomia  # in km

    def ricarica(self):
        return f"Lo scooter {self.modello} è in ricarica."

    def descrizione(self):
        return f"Scooter Elettrico: {self.modello}, Anno: {self.anno_produzione}, Autonomia: {self.autonomia} km"


# Creazione degli oggetti
auto1 = Auto("Fiat Panda", 2022, "Benzina", 5)
bici1 = Bicicletta("Bianchi", 2021, "Mountain bike")
scooter1 = ScooterElettrico("Xiaomi M365", 2023, 45)

#Stampa
print(auto1.descrizione())
print(auto1.rifornisci())  

print(bici1.descrizione())

print(scooter1.descrizione())
print(scooter1.ricarica())  
