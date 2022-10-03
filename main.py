import sys
from factories.ProgramFactory import ProgramFactory
import os
if __name__ == "__main__":
    os.system('color')
    print (sys.version)
    pf = ProgramFactory()
    pf.start()
