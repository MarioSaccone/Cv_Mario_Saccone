class PersonaleCucina:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età

    def lavora(self):
        print("lavoro generico")

class Chef(PersonaleCucina):
    pass