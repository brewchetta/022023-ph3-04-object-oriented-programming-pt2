# relative import
from .animal import Animal

class BigCat(Animal):

    def __init__(self, name, recent_food):
        super().__init__(name, recent_food)

    def __repr__(self):
        return f"<BigCat name={self.name} recent_food={self.recent_food}>"
