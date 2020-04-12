# immutable : static 
# Strings: are lists that can only contain characters
# String are immutable, cannot change the elements/characters of a string
sample_string = "Hello world"

# tuples (use round brackets)
# tuples are lists except they are immutable 
sample_tuple = ('a', 'b', 1, 2)

print(sample_tuple)

# sets (unordered and unindexable use curly braces)
# no duplicates
fruits = {"orange", "mango", "pineapple"}

print(fruits)

# adding item to set
fruits.add("lemon")

# removing item
fruits.remove("mango")

# dictionary (collection of key:value pairs, which can both be any types)
# similar to a list that is indexed by a key which can be any types
# mutable
my_dict = {}
marks = {"Anna": 72, "Isaac": 95, "Huss": 85, "George": 95}

print(marks)

print(marks["Anna"])

marks["Isaac"] = 85

print(marks["Isaac"])

print(marks.keys()) # return all the keys
print(marks.values()) # return all the values

for key in marks.keys():
    print("Key is", key)
    print("Value", marks[key])

# Using a dictionary to count frequency of elements
userinput = ""

fruits = []

while userinput != "q":
    userinput = input("enter a fruit: ")
    fruits.append(userinput)

print(fruits)

# Define dictionary

fruit_quantities = {}

for fruit in fruits:
    if fruit in fruit_quantities:
        fruit_quantities[fruit] += 1
    else:
        fruit_quantities[fruit] = 1

for fruit in fruit_quantities:
    print(fruit, fruit_quantities[fruit])