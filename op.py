#Write a program to create a class with name Student and perform the following tasks - Declare a variable grade 
#Print a sentence inside the class Create an object of class student and see the output


class student:
    grade = 6
    print("Hi my name is venini~ and I am in grade",grade)
obj = student()


#Write a program to create a class with name Student and perform the following tasks - Create a class variable grade and name 
#Create a function to print a sentence Create a function to print class variables grade and name 
#Create an object of class Student Call the two functions to execute them

class student:
    name = "venini"
    grade = 6
    def intro(self):
        print("Hi, im a student!~")
    def details(self):
        print("My name is",self.name)
        print("and my grade is",self.grade)
obj = student()
obj.intro()
obj.details()




#Write a program to create a class Parrot and perform the following tasks - Create a class variable species 
#Create a __init__ method that has instance variables - name and age 
#Create instances of class Parrot, passing arguments as well Print Class variable by accessing it Print Instance variables as well

class parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sing(self,song):
        return "{}sing {}".format(self.name,song)
obj = parrot("cinnamon",7)
print("cinnamon is a {}".format(obj.species))
print(obj.sing("WOKE UP IN TOKYO"))



#Write a program to create a class Parrot and perform the following tasks - Create a class variable species 
#Create a constructor that has instance variables - name and age Create instance methods for this class named sing and dance, 
#making them print a message. 
# Create instances of class Parrot, passing arguments as well Print Class variable by accessing it Print Instance variables as well

