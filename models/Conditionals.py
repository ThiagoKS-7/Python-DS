from termcolor import colored
import pyfiglet
class Conditionals:
    def __init__(self, data=[]):
        self.data = data
    def start(self):
        result = pyfiglet.figlet_format("CONDICIONAIS", font = "smslant" )
        print(colored(f"\n\n{result}\n", "cyan"))
        self.data = [
            ['Jetta Variant', 2003, False],
            ['Passat', 1991, False],
            ['Crossfox', 1990, False],
            ['DS5', 2019, True],
            ['Aston Martin DB4', 2006, False],
            ['Palio Weekend', 2012, False],
            ['A5', 2019, True],
            ['Série 3 Cabrio', 2009, False],
            ['Dodge Jorney', 2019, False],
            ['Carens', 2011, False]
        ]
        print(colored("IF COM == e != NUM FOR", "yellow"))
        print(colored("\nImprime os 0km", "green"))
        for i in self.data:
            if i[2] == True:
                print(i)
        print(colored("\nImprime os velhos", "red"))
        for i in self.data:
            if i[2] != True:
                print(i)
        print(colored("\n\nIF COM == e != NUM LIST COMPREHENSION", "yellow"))
        print(colored("\nImprime os 0km com LC", "blue"))
        print([i for i in self.data if i[2] == True])
        print(colored("\nImprime os velhos com LC", "green"))
        lc = [i for i in self.data if i[2] != True]
        for j in lc:
            print(j)