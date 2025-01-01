for i in range(1,13):
    print(f"25 * {i}={25 * i}")

for i in range(1,13):
    print(f"1 * {i}={1 * i}")





n = int(input("Enter the number of rows you want to display"))
for i in range(1,n+1):
    for j in range(i):
        print('*',end = '')
    print()


n = int(input("Enter the number of rows you want to display"))
for i in range(n,0,-1):
    for j in range(i):
       print('*',end = '')
    print()



a = sum(range(1,500))
print(a)



while True:
    print("Im a slay queen")
