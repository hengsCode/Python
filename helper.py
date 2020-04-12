# Using Helpers

def get_marks():
    return [81, 75, 56, 90, 48, 83, 99]

def average(numbers):
    sum = 0
    for number in numbers:
        sum+= number
    average = sum / len(numbers)
    return average