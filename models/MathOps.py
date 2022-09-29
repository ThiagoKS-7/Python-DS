class MathOps:
    def __init__(self, ops=[10 % 2 + 3 // 10, 5 * (2 + 3) / 2, 2 ** 3 * 4]):
        self.ops = ops
    def start(self):
        print("\n\nEXERCICIOS\n")
        for i in self.ops:
            print(i)
