class Animal:

    def __init__(self, name, recent_food):
        print('We are in ANIMAL')
        self.name = name
        self.recent_food = recent_food
        print('We are leaving ANIMAL')

    def eat(self, food):
        self.recent_food = food
        print(f"{self.name} is eating {self.recent_food}")

    def __repr__(self):
        return f"<Animal name={self.name} >"
