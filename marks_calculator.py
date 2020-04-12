# From helper.py import functions required OR you can just do this
# from helper import * (which imports all of the functions in helper)
# import helper (which also imports all of the functions in helper except you need to prefix all functions with
#   helper --> helper.getmarks())

from helper import get_marks, average

marks = get_marks()

averageMarks = average(marks)

print(averageMarks)