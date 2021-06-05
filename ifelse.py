x = 1
if x == 1:
    #there must always be indentation where there 
    #would be curly braces
    print('x is 1')

x = 2
print(x == 2) #prints out True
print(x == 3) #prints out False
print(x < 3) #prints out True

name = 'Vanessa'
name2 = 'Bob'
age = 27
if name == 'Vanessa' and age == 27:
    print('Your name is %s and you are %d years old.' % (name, age))

if name == 'Vanessa' or name == 'Bob':
    print('Your name is either %s or %s.' % (name, name2))

name = 'Vanessa'
if name in ['Vanessa', 'Victoria', 'Veronica', 'Valentina', 'Viridiana']:
    print('Your name is either Vanessa, Victoria, Veronica, Valentina, or Viridiana.')

statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass

x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

print(not False) # Prints out True
print((not False) == (False)) # Prints out False