import numpy as np
from termcolor import colored
import pyfiglet
class MngFiles:
    def __init__(self, files=['./data/carros-km.txt', './data/carros-anos.txt']):
        self.files = files
    def start(self):
        if len(self.files) == 2:
            result = pyfiglet.figlet_format("ABRINDO ARQUIVOS", font = "smslant" )
            print(colored(f"\n\n{result}\n", "cyan"))
            km = np.loadtxt(self.files[0])
            print(colored(f"QUILOMETRAGEM:\n{km[:40]}\n", "magenta"))
            anos = np.loadtxt(self.files[1], dtype=int)
            print(colored(f"\n\nANOS:\n{anos[:50]}\n", "yellow"))
            km_media = km / (2019-anos)
            print(colored(f"\n\nKM_MEDIA:\n{km_media[:20]}", "green"))
            print(colored(f"TIPO DE KM_MEDIA: {type(km_media)}", "blue"))
        else:
            print("\nNot enough files to show\n")
