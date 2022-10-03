from models.Program import Program
from models.MngFiles import MngFiles
from models.MathOps import MathOps
from models.ListOps import ListOps
from models.ListMethods import ListMethods
from models.Loops import Loops

class ProgramFactory:
    def __init__(self, classes='all'):
        self.classes = classes
    def start(self):
        if self.classes == 'all':
            acessories = [
                'Rodas de liga',
                'Travas elétricas',
                'Piloto automático',
                'Bancos de couro',
                'Ar condicionado',
            ]
            p = Program([ MngFiles(),
                        MathOps(),
                        ListOps(),
                        ListMethods(acessories),
                        Loops(acessories) ])
            p.start()
        else:
            p = Program(self.classes)
            p.start()
