import sys
from factories.ProgramFactory import ProgramFactory

if __name__ == "__main__":
    print (sys.version)
    pf = ProgramFactory()
    pf.start()
