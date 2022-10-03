from termcolor import colored
class NestedLoops:
    def __init__(self, data):
        self.data = data
    def start(self):
        print(colored("\n\nLOOPS ANINHADOS\n", "cyan"))
        print(colored("ANINHAMENTO BASICO:\n", "yellow"))
        for index, list in enumerate(self.data):
            print(colored(f"Lista {index}:","green"))
            for item in list:
                print(item)
            print("\n")