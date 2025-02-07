class libro: 
    isbn = 0

    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn + 1
        isbn += 1

    def descrizione(self):
        return "Titolo: ", self.titolo, "Autore: ", self.autore, "ISBN:", self.isbn

class libreria:
    def __init__(self):
        self.catologo = []

    def aggiungi_libro(self, libro):
        self.catalogo.append(libro)
        print("libro", libro.titolo + "aggiunto al catalogo")

    def rimuovi_libro(self, isbn): 
        for libro in self.catologo: 
            if libro.isbn == isbn:
                self.catalogo.remove(libro)
                print("libro con ISBN", isbn + "rimosso dal catalogo")
                return
            print("Nessun libro trovato con ISBN", isbn)

    def cerca_titolo(self, titolo):
        risultati = [libro for libro in self.catalogo if libro.titolo.lower]