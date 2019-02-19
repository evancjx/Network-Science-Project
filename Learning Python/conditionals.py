if True:
    print('Conditional was true')
if False:
    print('Conditional was false') #not printed

#language = 'Python'
language = 'Java'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No match')

#does not have switch case

# and or not
user  = 'Admin'
logged_in = False
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if user == 'Admin' or logged_in:
    print('Admin Page')

if user == 'Admin' and not logged_in:
    print('Please log in')

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)
print(id(a))
print(id(b))
a=b
print(a is b)

#condition = False;
#condition = None;
#condition = 10;
condition = '';
condition = {};
condition = [];
condition = ();
condition = 'test'
if condition:
    print('Evaluted to True')
else:
    print('Evaulated to False')
