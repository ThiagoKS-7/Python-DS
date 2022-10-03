from termcolor import colored
import pyfiglet
class ListMethods:
    def __init__(self, acessories):
        self.acessories = acessories
    def start(self):
        result = pyfiglet.figlet_format("METODOS EM LISTAS", font = "smslant" )
        print(colored(f"\n\n{result}\n", "cyan"))
        self.acessories.append('Airbag')
        self.acessories.sort() # organiza em ordem alfabética
        self.acessories.pop()
        self.acessories.append('Vidros elétricos')
        print(colored("\n\nNOVA LISTA: {self.acessories}\n", "yellow"))
