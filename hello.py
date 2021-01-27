import math
# This loads the math module and assigns it to a variable called math
# Equivalent to math = __import__("math")

# Defines a function (block) creating a function object
# Python then assigns this object to a variable called randomFunction
def randomFunction():
    print("hello world!")

# When the Python interpreter reads a source file,
# it sets special variables like __name__ which
# it assigns "__main__" (if the module is the main program)

# If the main program is in another file that is imported
# Python will assign __name__ as the name of the imported file
# The interpreter will then search for that file
if __name__ == "__main__":
    randomFunction()
    # newFunction()

print("My name is Henry.")

# def newFunction():
#     print("this won't print unless you bring it before main")