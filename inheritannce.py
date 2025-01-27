# Write a program to create a parent class Person (attributes - name, idnumber) with a method display to display the attributes. 
# Create a child class Employee (attributes - name, idnumber, salary, post). Access the attributes of parent class in child class. 
# Then, create an object for child class and call the display method to display the name and idnumber.


class Person: 
    def __init__(self,name,rollno):
     self.name = name
     self.rollno = rollno


    def display(self):
        print(self.name)
        print(self.rollno)

class Employee(Person):

    def __init__(self,name,rollno,salary,poast):
        self.salary = salary
        self.post = poast

        Person.__init__(self,name,rollno)

a = Employee("Bob",35,420,"Marketing Manager")
a.display()







# Write a program to create a parent class Person (attributes - fname, lname) with a method printname to display the full name. 
# Create a child class Student (attributes - fname, lname, year). 
# Access the attributes of parent class in child class using super() function. 
# Then, create an object for the child class and call the display method to display the full name. 
# Also, print the graduation year.



class Person:
   def __init__(self,fname,lname):
      self.firstname = fname
      self.lastname = lname

   def printname(self):
      print(self.firstname, self.lastname)


class Student(Person):
   def __init__(self, fname, lname, year):
      super().__init__(fname, lname)
      self.graduationyear = year

x = Student("Joey", "King", 2021)
x.printname()
print(x.graduationyear)



# Write a program to implement abstraction on animal class (base class). 
# The abstract method will be move that is for displaying what subclasses can do.




from abc import ABC, abstractmethod
class Animal(ABC):

	def move(self):
		pass

class Human(Animal):

	def move(self):
		print("I can walk and run")

class Snake(Animal):

	def move(self):
		print("I can crawl")

class Dog(Animal):

	def move(self):
		print("I can bark")

class Lion(Animal):

	def move(self):
		print("I can roar")
		
R = Human()
R.move()
K = Snake()
K.move()
R = Dog()
R.move()
K = Lion()
K.move()

