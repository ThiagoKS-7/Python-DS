from models.Program import Program
from models.MngFiles import MngFiles
from models.MathOps import MathOps
from models.ListOps import ListOps
from models.ListMethods import ListMethods
class ProgramFactory:
    def __init__(self, classes='all'):
        self.classes = classes
    def start(self):
        if self.classes == 'all':
            p = Program([ MngFiles(),
                        MathOps(),
                        ListOps(),
                        ListMethods([
                            'Rodas de liga',
                            'Travas elétricas',
                            'Piloto automático',
                            'Bancos de couro',
                            'Ar condicionado']) ])
            p.start()
        else:
            p = Program(self.classes)
            p.start()
