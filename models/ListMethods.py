class ListMethods:
    def __init__(self, acessories):
        self.acessories = acessories
    def start(self):
        print("\n\nMÉTODOS EM LISTAS\n")
        self.acessories.append('Airbag')
        self.acessories.sort() # organiza em ordem alfabética
        self.acessories.pop()
        self.acessories.append('Vidros elétricos')
        print(f"NOVA LISTA: {self.acessories}\n")
