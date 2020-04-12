# For if, elseif, else, while or for loops etc...
# Indentations help tell Python what is in the above statements
# i.e. everything indented in a block belongs to that block

x = 5

# so if x = 5, then it will print Hello and then move to the next statement
if x == 5:
    print("Equals 5")

if x < 10:
    print("Less than 10")

# similarly
# note that range takes (start, stop, step)
for i in range(0, 9, 2):
    print(i)

if i == 10:
    print("Equals 10")
