from termcolor import colored
import pyfiglet
class ListOps:
    def __init__(self, listA=['a', 'b', 'c'], listB=['d', 'e', 'f']):
        self.listA = listA
        self.listB = listB
    def start(self):
        result = pyfiglet.figlet_format("OPERACOES EM LISTAS", font = "smslant" )
        print(colored(f"\n\n{result}\n", "cyan"))
        test1 = 'a' in self.listA
        print(f"a em lista: {test1}")
        print(f"Concatenação: {self.listA + self.listB}")
        print(f"Comprimento: {len(self.listB)}")
        carro = [
            'Jetta Variant',
            'Motor 4.0 Turbo',
            2003,
            44410.0,
            False,
            ['Rodas de liga', 'Travas elétricas', 'Piloto automático'],
            88078.64
        ]
        a = '2003' in carro
        b = 'Rodas de liga' in carro
        c = 'False' not in carro
        print(f"resposta para A, B e C: {a} {b} {c}")
