class Program:
    def __init__(self, classes):
        self.classes = classes
    def start(self):
        if len(self.classes) > 0:
            for i in self.classes:
                i.start()
        else:
            print("No classes were passed")
