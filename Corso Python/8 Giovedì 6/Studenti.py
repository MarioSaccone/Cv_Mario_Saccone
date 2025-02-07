
class Persona:
    def __init__(self, nome, età):
        self.__nome = nome
        self.__età = età

    def get_nome(self):
        return self.__nome

    def get_età(self):
        return self.__età

    def presentazione(self):
        return f"{self.get_nome()} ha {self.get_età()} anni"


class Studente(Persona):
    def __init__(self, nome, età, voti):
        super().__init__(nome, età)
        self.voti = voti

    def calcola_media(self):
        if len(self.voti) > 0:
            media = sum(self.voti) / len(self.voti)
            return media
        else:
            return f"Non ci sono voti"

    def presentazione(self):
        return f"{self.get_nome()} ha {self.get_età()} anni e la sua media è {self.calcola_media():.2f}"


class Professore(Persona):
    def __init__(self, nome, età, materia):
        super().__init__(nome, età)
        self.materia = materia

    def presentazione(self):
        return f"{self.get_nome()} ha {self.get_età()} anni e insegna {self.materia}"



# studente = Studente("Mario", 20, [8, 9, 7, 10])
# print(studente.presentazione())  

# professore = Professore("Anna", 40, "Matematica")
# print(professore.presentazione())  

class Scuola:
    def __init__(self):
        self.studenti = []  
        self.professori = []  

    def aggiungi_studente(self):
        nome = input("Inserisci il nome dello studente: ")
        eta = int(input("Inserisci l'età dello studente: "))
        voti = list(map(int, input("Inserisci i voti dello studente separati da spazio: ")))
        
        
        studente = Studente(nome, eta, voti)
        self.studenti.append(studente)
        print(f"Studente {nome} aggiunto!")

    def aggiungi_professore(self):
        nome = input("Inserisci il nome del professore: ")
        eta = int(input("Inserisci l'età del professore: "))
        materia = input("Inserisci la materia che insegna: ")
        
        
        professore = Professore(nome, eta, materia)
        self.professori.append(professore)
        print(f"Professore {nome} aggiunto!")

    def mostra_studenti(self):
        print("Elenco degli studenti:")
        for studente in self.studenti:
            print(studente.presentazione())

    def mostra_professori(self):
        print("Elenco dei professori:")
        for professore in self.professori:
            print(professore.presentazione())

scuola = Scuola()


scuola.aggiungi_studente()
scuola.aggiungi_studente()


scuola.aggiungi_professore()


scuola.mostra_studenti()


scuola.mostra_professori()
