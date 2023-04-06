class Animal:

    def __init__(self, name, recent_food):
        self.name = name
        self.recent_food = recent_food

    def eat(self, food):
        self.recent_food = food
        print(f"{self.name} is eating {self.recent_food}")

    def __repr__(self):
        return f"<Animal name={self.name} >"
