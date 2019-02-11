#Welcome Message

message = "Hello World"

my_message_2 = 'Bobby\'s world'
my_message_2 = """Bobby\'s world
Cartoon world"""

print(message) #Hello World
print(len(message)) #11
print(message[0]) #H
print(message[0:5]) #Hello
print(message[:5]) #Hello
print(message[6:]) #World

print(message.lower()) #hello world
print(message.upper()) #HELLO WORLD
print(message.count('Hello')) #1
print(message.count('l')) #3
print(message.find('World')) #6

new_message = message.replace('World', 'Universe')

print(new_message)

message = message.replace('World', 'Universe')
print(message)

greeting = 'Hello'
name = 'Michael'
message = greeting + ', ' + name
print(message)

message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

#print(dir(name))
#print(help(str))
print(help(str.lower))