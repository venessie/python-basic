with open('Codingal.txt', 'w') as file: 
    file.write("Hi! I am Peguin am I am 1 yr old.")
file.close()

with open('codingal.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are....")
    for line in data:
        word = line.split()
        print(word)
    file.close()



new_file = open('New_file.txt', 'x')
new_file.close()

import os
print("Checking if my_file exists or not....")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else: 
    print("The file does not exist")

my_file = open("myfile.txt", "w")
my_file.write("Hi! I am Penguin and I am 1 yr old.")
my_file.close()

os.remove('Codingal.txt')










with open('Codingal.txt') as fp:
    data1 = fp.read()

with open('sample_doc.txt') as fp:
    data2 = fp.read()


data1 += "\n"
data1 += data2
print("Merging two files....")
with open ('MergedFile.txt', 'w') as fp:
    fp.write(data1)