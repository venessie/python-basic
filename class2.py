class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("I am a cat. My name is {self.name}. I am {self.age} years old.")


    def make_sound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")

cat1 = Cat("Dodo", 2.5)
dog1 = Dog("Tyson", 8)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()










class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
    
    def setMaxPrice(self, price):
        self.__maxprice = price
c = Computer()
c.sell()

c.__maxprice = 1000
c.sell()


c.setMaxPrice(1000)
c.sell()

