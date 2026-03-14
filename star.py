file = open("saturday.txt","w")

file.write("Saturday is the best day of the week!\n")
file.write("I love spending time with my family and friend on Saturdays.\n")
file.write("On Saturdays, I like to relax and do fun activites.\n")
file.write("I often go to the park or watch movies on Saturdays.\n")
file.write("Saturdays are perfect for trying new hobbies and exploring new places.\n")
file.close()

file1 = open("saturday.txt", "r")
print(file1.read())
file1.close()

file2 = open("saturday.txt","a")
file2.write("I always look forward to Saturdays because they are so enjoyable.\n")
file2.write("Saturdays are a great time to unwind and recharge for the week ahead.\n")
file2.close()












file = open("saturday.txt","r")
Counter = 0

Content = file.read()
CoList = Content.split("\n")

for i in CoList:
    if i:
        Counter += 1

print("This is the number of lines in the file")
print(Counter)