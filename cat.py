class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old")

    def make_sound(self):
        print("Bark")

cat1 = Cat("Dodo", 2.5)
dog1 = Dog("Bobo", 8)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()








    # Write a program to create two classes Dog and Cat, with the same attributes - (name and age) and methods - (info and make_sound). 
    # Create different objects for each class and pass the parameters. Showcase the concept of polymorphism in this program.


    class Computer:
        def __init__(self):
            self.__maxprice = 900

        def sell(self):
            print("Selling Price:",format(self.__maxprice))

        def setMaxPrice(self, price):
            self.__maxprice = price

    c = Computer()
    c.sell()

    #change the price
    c.__maxprice = 1000
    c.sell()

    #using setter function
    c.setMaxPrice(1000)
    c.sell()

