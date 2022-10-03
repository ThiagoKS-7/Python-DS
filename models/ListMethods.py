from termcolor import colored
class ListMethods:
    def __init__(self, acessories):
        self.acessories = acessories
    def start(self):
        print(colored("\n\nMÉTODOS EM LISTAS\n", "cyan"))
        self.acessories.append('Airbag')
        self.acessories.sort() # organiza em ordem alfabética
        self.acessories.pop()
        self.acessories.append('Vidros elétricos')
        print(colored("\n\nNOVA LISTA: {self.acessories}\n", "yellow"))
