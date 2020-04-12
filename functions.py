# Python dynamically determines the function, return and argument types
# Note also that functions that are called need to be def'd before they are called
def addtwoNumbers(num1, num2):
    sum = num1 + num2
    return sum

result = addtwoNumbers(5, 8)
print(result)

# Default values; we can assign default values to a variable if it has not been
# assigned a value

# Default value for name is "World"
def print_hello(name = "World"):
    print("Hello " + name)

print_hello("Anna")
print_hello()


# Having arbitrary arguments
# *numbers is like an array of elements 
def add_numbers(*numbers):
    sum = 0 
    for number in numbers:
        sum += number
    return sum

result = add_numbers(1, 2, 3, 4)
print(result) 