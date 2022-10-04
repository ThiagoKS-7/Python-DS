from models import (
    Program as p,
    MngFiles as mf,
    MathOps as mo,
    ListOps as lo,
    ListMethods as lm,
    Loops as l,
    NestedLoops as nl,
    Conditionals as c,
    NestedConditionals as nc,
    NumpyArrays as na
)

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
            classes = [ 
                mf.MngFiles(),
                mo.MathOps(),
                lo.ListOps(),
                lm.ListMethods(acessories),
                l.Loops(acessories),
                nl.NestedLoops(data),
                c.Conditionals(),
                nc.NestedConditionals(),
                na.NumpyArrays(data)
            ]
            prog = p.Program(classes)
            prog.start()
        else:
            prog = p.Program(self.classes)
            prog.start()
