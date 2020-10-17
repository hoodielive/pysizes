class Egungun:
    def __init__(self, name, praxis):
        self.name = name
        self.praxis = praxis
        print(self.praxis)

class EgungunPriest(Egungun):
    def __init__(self, purpose):
        super().__init__("abifoluwa", "Iwa Rere")
        self.purpose = purpose

egunda = EgungunPriest("Iwa Pele")

print(egunda)
