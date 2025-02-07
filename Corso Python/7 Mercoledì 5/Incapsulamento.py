class Persona:
    __nome = "mirko"
    _cognome = "campari"

    def get_nome(self):
        print(self.__nome)
    def set_nome(self, n):
        self.__nome = n
        print(self.__nome)

mirko1 = Persona()

mirko1.get_nome()