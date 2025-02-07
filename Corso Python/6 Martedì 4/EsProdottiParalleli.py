#classe prodotto
class prodotto: 
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome 
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione
    
#classe derivate
class elettronica(prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        self.prodotto = prodotto(nome, costo_produzione, prezzo_vendita, garanzia)
        self.garanzia = garanzia

    def calcola_profitto(self):
        return self.prodotto.calcola_profitto()
    
    def get_nome(self):
        return self.prodotto.nome

class abbigliamento:
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        self.prodotto = prodotto(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale

    def calcola_profitto(self):
        return self.prodotto.calcola_profitto()

    def get_nome(self):
        return self.prodotto.nome

#creazione fabbrica
class Fabbrica:
    def __init__(self):
        self.inventario = {}

    def aggiungi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome] += quantita
        else:
            self.inventario[prodotto.nome] = quantita
        print("Aggiunti", quantita, "unità di", prodotto.nome, "all'inventario.")

    def vendi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.inventario and self.inventario[prodotto.nome] >= quantita:
            self.inventario[prodotto.nome] -= quantita
            print("Venduti", quantita, "unità di", prodotto.nome + ".")
        else:
            print("Prodotto", prodotto.nome, "non disponibile o quantità insufficiente.")

    def resi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome] += quantita
            print("Resi", quantita, "unità di", prodotto.nome + ".")
        else:
            print("Prodotto", prodotto.nome, "non trovato nell'inventario.")

