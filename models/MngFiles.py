import numpy as np
from termcolor import colored
class MngFiles:
    def __init__(self, files=['./data/carros-km.txt', './data/carros-anos.txt']):
        self.files = files
    def start(self):
        if len(self.files) == 2:
            km = np.loadtxt(self.files[0])
            print(colored(f"\n\nQUILOMETRAGEM:\n{km}\n", "cyan"))
            anos = np.loadtxt(self.files[1], dtype=int)
            print(colored(f"\n\nANOS:\n{anos}\n", "yellow"))
            km_media = km / (2019-anos)
            print(colored(f"\n\nKM_MEDIA:\n{km_media}\n\n{type(km_media)}\n", "yellow"))
        else:
            print("\nNot enough files to show\n")
