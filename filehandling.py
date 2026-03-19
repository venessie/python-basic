file = open("sunday.txt", "w")
file.write("On Sundays, I hangout with friends\n")
file.write("I go to dance classes on Sundays\n")
file.write("On Sundays, I have piano lessons\n")
file.write("On Sundays, I travel alot.\n")
file.close()


file1 = open("sunday.txt", "r")
print(file1.read())
file1.close

file2 = open("sunday.txt", "a")
file2.write("I spend alot of my time outside on Sundays.\n")
file2.write("I have alot of freetime on Sundays.\n")
file2.close()








file1 = open('sunday.txt', 'r')

file2 = open('sundayupdated.txt', 'w')

for line in file1.readlines():

    if not (line.startswith('Sunday')):
        print(line)
        file2.write(line)

file2.close()
file1.close()








fn = open('sunday.txt')

fn1 = open('sundayupdated.txt', 'w')

cont = fn.readlines()
type(cont)
for i in range(1, len(cont)+1):
    if(i % 2 != 0):
      fn1.write(cont[i - 1])
    else:
        pass

fn1.close()
fn1 = open('sundayupdated.txt', 'r')
cont1 = fn1.read()
print(cont1)
fn.close()
fn1.close()
   