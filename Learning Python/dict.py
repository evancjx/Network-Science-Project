student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)
print(student['name'])
print(student['courses'])
student2 = {1: 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student2[1])

print(student.get('age'))
print(student.get('phone', 'not found'))

student['phone'] = '555-55555'
print(student.get('phone', 'not found'))
student['name'] = 'Jane'
print(student)

student.update({'name': 'James', 'age': '26', 'phone': '123456'})
print(student)

del student['age']
print(student)

phone = student.pop('phone')
print(student)
print(phone)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)