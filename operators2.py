subject = "Literacy"
average = 84.75
has_passed = True
progressing_well = True
letter_grade = "A-"
grade = 7



print("Subject:",subject)
print("Average",average)
print("Passed?",has_passed)
print("Progressing Well?",progressing_well)
print("Letter Grade", letter_grade)
print("Grade",grade)

print("\n After Type Casting....")
grade = str(grade)
print(grade)
print("Data Type of grade is", type(grade))
average = int(average)
print(average)
print("Data Type of average is", type(average))








num1 = 3
num2 = 42

print("Floor Division:",num1 // num2)
print("Modulus Operation:", num1%num2)
print("Square:",num1**2)
print("Square Root:", num1**0.5)

print("Equal?", num1==num2)
print("Number 1 greater?", num1>num2)
print("Number 2 greater?", num1<num2)
print("Not Equal?", num1!=num2)

result = num1/2+num2**2+10
print("Result of given equation is:", result)