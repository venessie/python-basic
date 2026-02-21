class student:
    grade = 7
    print("Hi, I am  a student of grade", grade)

ob = student()






class student:
    grade = 10
    name = "Penguin"

    def introduction(self):
        print("Hi I am a student")
    
    def details(self):
        print("My name is", self.name)

ob = student()
ob.introduction()
ob.details()








class Parrot:

    species = "bird"
    
    def __init__(self, name, age):
         self.name = name  
         self.age = age
    
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 10)

print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old". format( woo.name, woo.age))









class Parrot:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return "{} sings {}".format(self.name, song)
    
    def dance(self):
        return "{} is now dancing",format(self.name)
    
blu = Parrot("Blu", 10)

print(blu.sing("'Happy'"))
print(blu.dance())