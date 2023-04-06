from .big_cat import BigCat

class Lion(BigCat):

    def __init__(self, name, recent_food, mane):
        print('We are in LION')
        super().__init__(name, recent_food)
        self.mane = mane
        print('We are leaving LION')

    def eat_foodies(self, food):
        super().eat(food)
        print("IT WAS DELICIOUS AND I AM FULL RAWR")

    def __repr__(self):
        return f"<Lion name={self.name} recent_food={self.recent_food} mane={self.mane} >"
