my_tuple = ()
print(my_tuple)

my_tuple = (1, 2, 3)
print(my_tuple)

my_tuple = (1, 2, 3)
print(my_tuple)

my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[0])
print(my_tuple[5])

n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

print(n_tuple[0][3])
print(n_tuple[1][1])

print("Sliced :", my_tuple[1:4])

for letter in (my_tuple):
    print("Hello", letter)










my_set = {1, 2, 2, 3, 4, 4, 4}
print("Set :", my_set)

my_set.add(5)
print("Updated Set:", my_set)

set1 = my_set
set2 = {2,4,4,6}

print("\nSet 1", set1)
print("Set 2", set2)
print("Difference")
print("Symmerteric Difference")
print(set1.symmetric_difference(set2))






setc1 = {"green", "blue"}
setc2 = {"blue", "yellow"}
print( "Original sets:")
print(setc1)
print(setc2)
setc = setc1. union(setc2)
print("\nUnion of above sets:")
print(setc)




setc1 = {"green", "blue"}
setc2 = {"blue", "yellow"}
print( "Original sets:")
print(setc1)
print(setc2)
setc = setc1. intersection(setc2)
print("\Intersection of above sets:")
print(setc)