from termcolor import colored
class Loops:
    def __init__(self, acessories):
        self.acessories = acessories
    def start(self):
        print(colored("\n\nLOOPS\n", "cyan"))
        print(colored("FOR BASICO\n", "yellow"))
        for i in self.acessories:
            print(i)
        print(colored("\n\nFOR COM RANGE\n", "yellow"))
        for i in range(len(self.acessories)):
            print(self.acessories[i])
        print(colored("\nLIST COMPREHENSION\n", "yellow"))
        list = [self.acessories[i] for i in range(len(self.acessories))]
        print(list)