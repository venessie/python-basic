no = int(input("Enter a  WHOLE number"))
if no % 2 == 0:
    print("Even")
else:
    print("Odd")






no = int(input("Enter a number"))
if no > 0:
    print("Postive")
elif no < 0:
    print("Negative")
else:
    print("Neutral")





height = int(input("Enter a height in cm"))
weight = float(input("Enter a weight in kg"))
BMI = weight/(height/100)**2

if BMI <=18.4:
    print("You are Underweight. Your BMI is",BMI)
elif BMI <=24.9:
    print("You are Healthy. Your BMI is",BMI)
elif BMI <=34.9:
    print("You are Over Weight. Your BMI is",BMI)
elif BMI <=39.9:
    print("You are Obese. Your BMI is",BMI)
else: 
    print("You are Extremely Obese. Your BMI is",BMI)










import datetime
d = datetime.datetime.now()
print(d)
import calendar
c = calendar.calendar(2025)
print(c)