import numpy as np
class MngFiles:
    def __init__(self, files=['./data/carros-km.txt', './data/carros-anos.txt']):
        self.files = files
    def start(self):
        if len(self.files) == 2:
            km = np.loadtxt(self.files[0])
            print(f"\nQUILOMETRAGEM:\n{km}\n\n")
            anos = np.loadtxt(self.files[1], dtype=int)
            print(f"\nANOS:\n{anos}\n\n")
            km_media = km / (2019-anos)
            print(f"\nKM_MEDIA:\n{km_media}\n\n{type(km_media)}")
        else:
            print("\nNot enough files to show\n")
