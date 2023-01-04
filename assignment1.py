#Lists are ordered collections of items that can be of any data type, including other lists. They are defined using square brackets and items are separated by commas. Lists are mutable, meaning they can be changed after they are created.
#list of string
fruits = ['apple', 'banana', 'orange', 'strawberry']
#list of numbers
number=[1,2,3,4,5] 
#list of mixed type
list1=[True,1.233,22389,'deaf',1, 'hello', 3.14, ['a', 'b', 'c'], {1: 'one', 2: 'two'}]

#Tuples are similar to lists, but they are immutable, meaning they cannot be modified after they are created. They are defined using parentheses and items are separated by commas.
#Tuple of string
colors = ('red', 'green', 'blue')
#Tuple of number
number=(1,4,5,6,2,7)
#Tuple of mixed type
mytuple = (1, 'hello', 3.14, ['a', 'b', 'c'], {1: 'one', 2: 'two'})

#Dictionaries are collections of key-value pairs. They are defined using curly braces and keys are separated from values by a colon. Dictionaries are unordered and are often used to store data that needs to be accessed by a unique identifier (the key).
student = {'name': 'John', 'age': 25, 'major': 'Computer Science'}
student_ages = {1: 'John', 2: 'Jane', 3: 'Jack'}
mydict = {'int': 1, 'string': 'hello', 'float': 3.14, 'list': ['a', 'b', 'c'], 'tuple': (1, 2, 3)}

#Sets are unordered collections of unique items. They are defined using curly braces and items are separated by commas. Sets do not allow duplicate items.
primes = {2, 3, 5, 7, 11, 13}
decimals = {1.2, 3.14, 2.718, 0.577}
mixed_set = {1, 'hello', 3.14, ['a', 'b', 'c'], {1: 'one', 2: 'two'}}
