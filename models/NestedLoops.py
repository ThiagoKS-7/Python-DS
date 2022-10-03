from termcolor import colored
class NestedLoops:
    def __init__(self, data):
        self.data = data
    def start(self):
        print(colored("\n\nLOOPS ANINHADOS\n", "cyan"))
        print(colored("ANINHAMENTO BASICO:\n", "yellow"))
        acessories = []
        for index, list in enumerate(self.data):
            print(colored(f"Lista {index}:","green"))
            for item in list:
                print(item)
                acessories.append(item)
            print("\n")
        acessories = [set(acessories)]
        print(colored("ACESSORIOS SEM DUPLICATAS:", "yellow"))
        print(acessories)
        print(colored("\nACESSORIOS SEM DUPLICATAS (LIST COMPREHENSION):", "green"))
        acessories = [set([item for list in self.data for item in list])]
        print(acessories)
