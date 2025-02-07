class MiaClasse:
    def _init_(self):
        self.__variabile_privata = "Sono privata"

    def __metodo_privato(self):
        return "Questo è un metodo privato"

obj = MiaClasse()
# Stampando direttamente la variabile privata solleverà un'eccezione
# print(obj.__variabile_privata)  # AttributeError
# L'accesso corretto (che dovrebbe essere evitato) sarebbe:
print(obj.MiaClasse_variabile_privata)  # Funzionerà, ma non è buona prassi