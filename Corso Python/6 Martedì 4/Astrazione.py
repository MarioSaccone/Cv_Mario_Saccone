class Animale:
    def __init__(self, nome):
        self.nome = nome
        
    def parla(self):
        print(f"{self.nome} fa suono generico.")

class cane(Animale):

    def parla(self):
        print(f"{self.nome} abbaia!")

animale_generico = Animale("AnimaleGenerico")
cane = cane("Fido")

animale_generico.parla()
cane.parla()
