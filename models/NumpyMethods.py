from termcolor import colored
import pyfiglet

from numpy import array, arange
import time


class NumpyMethods:
    def __init__(self, data):
        self.data = data

    def start(self):
        result = pyfiglet.figlet_format("METODOS  E  ATRIBUTOS \nNUMPY", font="smslant")
        print(colored(f"\n\n{result}\n", "cyan"))
        print(
            colored("USANDO SHAPE (nº linhas, nº colunas): ", "yellow")
            + f"{array(self.data).shape}\n"
        )
        print(
            colored("USANDO NDIM (dimensões do array): ", "magenta")
            + f"{array(self.data).ndim}\n"
        )
        print(
            colored("SIZE - Nº de elementos (linhas x colunas): ", "red")
            + f"{array(self.data).size}\n"
        )
        print(
            colored("DTYPE - TIPO DE DADOS: ", "blue") + f"{array(self.data).dtype}\n"
        )
        print(
            colored("TRANSPOSTO - INVERTE LINHA E COLUNAS: ", "cyan")
            + f"{array(self.data).T}\n"
        )
        print(
            colored("TO LIST - TRANSFORMA EM LISTA: ", "yellow")
            + f"{array(self.data).tolist()}\n"
        )
        print(colored("RESHAPE: 5x2 ", "magenta") + f"{arange(10).reshape(5,2)}\n")
        print(
            colored("RESHAPE 5x2 CONFORME C: ", "magenta")
            + f"{arange(10).reshape((5,2), order='C')}\n"
        )
        print(
            colored("RESHAPE 2x5 CONFORME FORTRAN: ", "magenta")
            + f"{arange(10).reshape((2,5), order='F')}\n"
        )
