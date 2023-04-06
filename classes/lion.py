from .big_cat import BigCat
from custom_decorator.my_decorator import my_decorator

class Lion(BigCat):

    # these are all class variables (can call Lion.proper_lion_names)
    # an instance can still access these variables
    proper_lion_names = ["Bill", "Ted", "Shareif", "Patty"]
    loudest_lion = None
    all_the_lions = []
    # if an instance makes its own variable called 'loudest_lion' or 'proper_lion_names'
    # then the instance will use that variable but the class variable still exists

    def __init__(self, name, recent_food, mane):
        super().__init__(name, recent_food)
        self.mane = mane
        Lion.add_lion(self)

    # the @classmethod is a decorator
    # this means it can be called by the class itself ( Lion.add_lion('Bob') )
    # instances can also call class methods
    @classmethod
    def add_lion(cls, lion):
        # it's convention to use cls instead of self in a class method
        cls.all_the_lions.append(lion)

    @classmethod
    def list_names(cls):
        return [ name + " the Lion" for name in  cls.proper_lion_names ]

    # this is an example of a custom decorator
    # the decorator affects and changes eat_foodies when it gets called
    # you can see and guess at what the decorator does in its file
    @my_decorator
    def eat_foodies(self, food):
        super().eat(food)
        print("IT WAS DELICIOUS AND I AM FULL RAWR")

    def __repr__(self):
        return f"<Lion name={self.name} recent_food={self.recent_food} mane={self.mane} >"
