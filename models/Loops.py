from termcolor import colored
import pyfiglet


class Loops:
    def __init__(self, acessories):
        self.acessories = acessories
    def start(self):
        result = pyfiglet.figlet_format("LOOPS", font = "smslant" )
        print(colored(f"\n\n{result}\n", "cyan"))
        print(colored("FOR BASICO\n", "yellow"))
        for i in self.acessories:
            print(i)
        print(colored("\n\nFOR COM RANGE\n", "yellow"))
        for i in range(len(self.acessories)):
            print(self.acessories[i])
        print(colored("\nLIST COMPREHENSION\n", "yellow"))
        list = [self.acessories[i] for i in range(len(self.acessories))]
        print(list)