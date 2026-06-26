class Basechai:
    def __init__(self, name):
        self.name = name

    def prepare(self):
        print(f"Preparing {self.name} chai")



class MasalaChai(Basechai):    
    def add_spices(self):
        print(f"Adding spices to {self.name} chai")


class ChaiShop:
    chai_cls = Basechai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve_chai(self):
        print(f"Serving {self.chai.name} chai")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

    def serve_chai(self):
        print(f"Serving {self.chai.name} chai with extra care")
        self.chai.prepare()
        self.chai.add_spices()

shop = ChaiShop()    
fancy_shop = FancyChaiShop()
shop.serve_chai()
fancy_shop.serve_chai()

