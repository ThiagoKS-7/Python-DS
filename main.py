import sys
from factories.ProgramFactory import ProgramFactory
import os
import pyfiglet
from termcolor import colored

def salute():
    os.system('color')
    up_title = pyfiglet.figlet_format("Python for", font = "big" )
    sub_1=pyfiglet.figlet_format("Data", font = "univers" )
    sub_2=pyfiglet.figlet_format(" Science", font = "univers" )
    print(colored(up_title, color="green"))
    print(colored(sub_1, color="blue") + colored(sub_2, color="yellow"))
    print (colored("PYTHON VERSION: ", color="green"), sys.version)

if __name__ == "__main__":
    salute()
    pf = ProgramFactory()
    pf.start()
