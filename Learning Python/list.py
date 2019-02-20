#List
courses = ['History', 'Math', 'Physics', 'CompSci']
# print(courses)
# print(len(courses))
# print(courses[2])
# print(courses[-1]) #Last Item
# print(courses[0:2])
# print(courses[:2])
# print(courses[2:])

#Add item to the list
# courses.append('Art')
# print(courses)
# courses.insert(0, 'Chinese') #Insert into index 0
# print(courses)
# courses_2 = ['Education', 'Engineering']
# courses.insert(0, courses_2)
# print(courses)
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses.extend(courses_2)
# print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
courses.remove('Math')
print(courses)
popped = courses.pop()
print(courses)
print(popped)

# #Sort
# courses.reverse()
# print(courses)
# courses.sort()
# print(courses)
# num = [1, 5, 4, 3, 2]
# print(num)
# num.sort()
# print(num)
# num.sort(reverse=True)
# print(num)
# sorted_courses = sorted(courses)
# print(sorted_courses)
#
# print(min(num))
# print(max(num))
# print(sum(num))
#
# print(courses)
# print(courses.index('CompSci'))
# print('Art' in courses)
# print('Math' in courses)
#
# for item in courses:
#     print(item)
#
# for course in courses:
#     print(course)
#
# for index, course in enumerate(courses):
#     print(index, course)
#
# for index, course in enumerate(courses, start=1):
#     print(index, course)
#
# course_str = ', '.join(courses)
# print(course_str)
#
# new_list = course_str.split(', ')
# print(new_list)
#
# #Tuples and Sets
# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1
#
# print(list_1)
# print(list_2)
#
# list_1[0] = 'Art'
#
# print(list_1)
# print(list_2)
#
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1
#
# print(tuple_1)
# print(tuple_2)
#
# #tuple_1[0] = 'Art' #Cannot be modify
#
# #Sets
# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# print(cs_courses)
# cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
# print(cs_courses) #remove duplicate
# print('Math' in cs_courses)
#
# art_courses = {'History', 'Math', 'Art', 'Design'}
# print(cs_courses.intersection(art_courses))
# print(cs_courses.difference(art_courses))
# print(cs_courses.union(art_courses))
#
# #Empty list tuples and sets
# empty_list = []
# empty_list = list()
# empty_tuple = ()
# empty_tuple = tuple()
# empty_set = {} #this isn't right. its a dict
# empty_set = set()