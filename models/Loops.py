class Loops:
    def __init__(self, acessories):
        self.acessories = acessories
    def start(self):
        print("\n\nLOOPS\n")
        print("FOR BASICO:\n")
        for i in self.acessories:
            print(i)
        print("\n\nFOR USANDO RANGE:\n")
        for i in range(len(self.acessories)):
            print(self.acessories[i])
        print("\n\nLIST COMPREHENSION:\n")
        list = [self.acessories[i] for i in range(len(self.acessories))]
        print(list)