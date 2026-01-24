for i in range(1, 11):
    print(f"23 x {i} = {23 * i}")
for i in range(1, 11):
    print(f"22 x {i} = {22 * i}")





n = int (input("Enter the number of rows: "))
for i in range(1, n+1):
    for j in range(i):
        print('*', end=' ')
    print()

n = int (input("Enter the number of rows: "))
for i in range(n, 1, -1):
    for j in range(i):
        print('*', end=' ')
    print()

total = sum(range(1,23))
print(total)













num = int(input("Enter a number: "))

if num > 1:
      for i in range(2, int(num**0.5) + 1):
          if num % i == 0:
              print(f"{num} is not a prime number.")
              break
          else: 
              print(f"{num} is a prime number.")
else: 
    print(f"{num} is not a prime number.")
              
          