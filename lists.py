# Defining and initialising a list:
my_list = [] # an empty list
print(my_list)

students = ["Ian", "Emily", "Sharon"]
print(students)

# You can also have differing data types in the list
mixed = ["Hello", 2, 10, "World"]
print(mixed)

# Splitting/cutting a list
# [start index: end index: increment]
# by default if start index not entered, it will start from beginning
# by default if end index not entered, it will run until the end of list
mixed[1:3:1]


# To access members of a list 

print(students[0])

for member in mixed:
    print(member) 

i = 0

while i < len(mixed):
    print(mixed[i])
    i+=1

# Append to list
print("Before:", mixed)
mixed.append("Emily")
print("After:", mixed)

# popping from list
print("Before:", mixed)
x = mixed.pop()
print("After:", mixed)

# x should be the element popped from end of list
print(x) 

# create an array that has x where x is in range(1, 10) --> 1, 9
my_numbers = [x for x in range(1,10)]

print(my_numbers)

# can also add if/else statements
# only want odd numbers
my_odd = [x for x in range(1,10) if x % 2 == 1]
print(my_odd)

# can also apply to the element itself
halved = [x/2 for x in my_numbers]
print(halved)