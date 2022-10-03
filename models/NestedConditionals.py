from termcolor import colored
import pyfiglet

class NestedConditionals:
    def __init__(self, data=[]):
        self.data = data
    def start(self):
        result = pyfiglet.figlet_format("CONDICIONAIS ANINHADAS", font = "smslant" )
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
        print(colored("\nIF ELSE NUM FOR", "yellow"))
        print(colored("\nImprime todos com filtro", "cyan"))
        novos,usados = [],[] 
        for i in self.data:
            if i[2] == True:
                novos.append(i)
            else:
                usados.append(i)

        print(colored(f"NOVOS - ", "green") + f"{novos}\n")   
        print(colored(f"USADOS:", "red"))
        for i in usados:
            print(i)

        print(colored("\nIF ELIF ELSE NUM FOR", "yellow"))
        ate_doisk,doisk_a_doisk10,outros = [],[],[]
        for i in self.data:
            if i[1] <= 2000:
                ate_doisk.append(i)
            elif i[1] > 2000 and i[1] <= 2010:
                doisk_a_doisk10.append(i)
            else:
                outros.append(i)

        print(colored(f"ATÉ 2000 - ", "blue") + f"{ate_doisk}\n") 
        print(colored(f"2001 A 2010 - ", "green") + f"{doisk_a_doisk10}\n")   
        print(colored(f"OUTROS:", "red"))
        for i in outros:
            print(i)
