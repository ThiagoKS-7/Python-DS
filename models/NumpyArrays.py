from termcolor import colored
import pyfiglet
# import numpy as np  # importa tudo
from numpy import arange,array,loadtxt
import time

class NumpyArrays:
    def __init__(self, data):
        self.data = data
    def start(self):
        result = pyfiglet.figlet_format("ARRAYS   NUMPY", font = "smslant" )
        print(colored(f"\n\n{result}", "cyan"))
        print(colored("USANDO ARANGE", "yellow"))
        print(arange(10))
        print(colored("\nNP ARRAY A PARTIR DE UMA LISTA NORMAL\n", "yellow"))
        km = array(self.data)
        print(km, type(km), km.dtype,km.shape)
        print(colored("\nABRINDO ARQUIVOS COMO LISTA\n", "yellow"))
        km = loadtxt(fname="./data/carros-km.txt", dtype=int)
        print(colored("QUILOMETRAGEM:", "green"))
        print(km[:40],km.shape)
        '''
            A PARTE ABAIXO PODE ESTOURAR A MEMÓRIA DO PC
            Descomente por sua conta e risco
        '''
        # print(colored("\nDESEMPENHO\n", "yellow"))
        # np_array=arange(1000000)
        # for _ in range(100): 
        #     np_array *=2
        # print('RANGE 100 1M NUMPY - Current Time:', time.ctime(time.time()))
        # print("Aguarde a lista...")
        # py_list=list(range(1000000))
        # for _ in range(100): py_list=[x*2 for x in py_list]
        # print('RANGE 100 1M LISTA - Current Time:', time.ctime(time.time()))