from models.Program import Program
from models.MngFiles import MngFiles
from models.MathOps import MathOps
from models.ListOps import ListOps
from models.ListMethods import ListMethods
from models.Loops import Loops
from models.NestedLoops import NestedLoops
from models.Conditionals import Conditionals
from models.NestedConditionals import NestedConditionals

class ProgramFactory:
    def __init__(self, classes='all'):
        self.classes = classes
    def start(self):
        import os
        if self.classes == 'all':
            acessories = [
                'Rodas de liga',
                'Travas elétricas',
                'Piloto automático',
                'Bancos de couro',
                'Ar condicionado',
            ]
            data = [ 
                ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
                ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
                ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
            ]
            p = Program([ MngFiles(),
                        MathOps(),
                        ListOps(),
                        ListMethods(acessories),
                        Loops(acessories),
                        NestedLoops(data),
                        Conditionals(),
                        NestedConditionals() ])
            p.start()
        else:
            p = Program(self.classes)
            p.start()
