# li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
#
# s_li = sorted(li)
# s_li = sorted(li, reverse=True)
#
# print('Sorted Variable:\t', s_li)
#
# li.sort()
# li.sort(reverse=True)
#
# print('Orignial Variable:\t', li)
#
# tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
# s_tup = sorted(tup)
# print('Tuple\t', tup)
# print('Tuple\t', s_tup)

# dict = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
# s_di = sorted(dict)
# print('Dict\t', dict)
# print('Dict\t', s_di)

# li = [-6, -5, -4, 1, 2, 3]
# s_li = sorted(li)
# print(s_li)
# s_li = sorted(li, key=abs)
# print(s_li)


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self): # how you want the class to be represented
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)

from operator import attrgetter

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]


def e_sort(emp):
    return emp.name


s_employees = sorted(employees, key=e_sort, reverse=True)
print(s_employees)

s_employees = sorted(employees, key=lambda e: e.name, reverse=True)
print(s_employees)
s_employees = sorted(employees, key=attrgetter('age'), reverse=True)
print(s_employees)
