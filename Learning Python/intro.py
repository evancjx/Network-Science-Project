
# import importLib as mm

# from importLib import find_index, test #better option
from importLib import * #not good
import sys

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)
print(test)

print(sys.path)
