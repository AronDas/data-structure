my_set = {1, 5, 7}
print(my_set)

my_set = {1.0, "Hello world", (1, 5, 7)}
print(my_set)

my_set = {1, 5, 7, 8, 4, 2}
print(my_set)

my_set = set([1, 5, 7, 5])
print(my_set)

num_set = set([0, 1, 3, 4, 5])
print("Original set")
print(num_set)
num_set.pop()
print("After removing the first element from said set:")
print(num_set)