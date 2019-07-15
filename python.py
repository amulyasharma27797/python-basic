# def add_num(a,b):
# 	"""Using f-stings to add two numbers using functions"""
# 	print(f"{a} + {b} = {a+b}")
# add_num(3,4)


# def add_number(a,b):
# 	"""Using return statement"""
# 	return(f"{a} + {b} = {a+b}")
# print(add_number(3,4))


# def greet(name="User"):
# 	"""Default argument in python"""
# 	return(f"Hello, {name}")
# print(greet())


# def say(*names):
# 	"""Arbitrary Arguments"""
# 	for name in names: 
# 		print(f"Hello, {name}")
# say("Ayushi", "Gaurav", "Sanyam")


# # Enumerator
# for i in enumerate([1,2,3,4,]):
# 	print(i)


# # Filter
# p = list(filter(lambda x:x%2==0, [4,3,1,2,0,False]))
# print(p)


# # getattr()
# class Person:
# 	name="Aditya"
# 	age=21

# person = Person()
# print(getattr(person, 'age'))


# # Class Methods
# class Car:
# 	def __init__(self, brand, model, color, fuel):
# 		self.brand = brand
# 		self.model = model
# 		self.color = color
# 		self.fuel = fuel

# 	def start(self):
# 		print(f"Car {self.model} is start")

# 	def stop(self):
# 		pass

# 	def turn(self):
# 		pass

# blackverna = Car('Hyundai', 'Verna', 'Black', 'Diesel')
# blackverna.start()


# # Python Method
# class Try:
# 	def __init__(self):
# 		pass

# 	def printhello(self, name):
# 		print(f"Hello {name}")
# 		# return name

# obj = Try()
# obj.printhello('Ayushi')



# class Try:

# 	def printhello(self, name):
# 		# print(f"Hello {name}")
# 		return (f"Hello {name}")

# obj = Try()
# # obj.printhello('Ayushi')


# # Constructors
# class three:
# 	def __init__(self):
# 		self.val = int(input("Enter your value \n"))

# t = three()
# print(t.val)


# class one:
# 	def __init__(self, a):
# 		print(a)

# o = one('a')



# # zip()
# for i in zip([1,2,3,4,5,6], [4,5,6,7,8]):
# 	print(i)


# z = zip([1,2], [3,4])
# a,b = zip(*z)
# print(a,b)


# # eval()
# print(eval('[1,2,3][2]'))


# # Iterating in list
# for i in [1,2,3]:
# 	if i%2==0:
# 		print(f"{i} is composite\n")

# # Tuples unpacking
# mytuple = (1,2,3)
# a,b,c = mytuple
# print(mytuple)
# print(a,b,c)
# # del mytuple
# print(mytuple)


# # List Comprehension
# even = [2*i for i in range(1,11)]
# print(even)

# even = [2*i for i in range(1,11) if i%3==0]
# print(even)


# # COLLECTIONS MODULE IN PYTHON

# # Counters
# from collections import Counter
# c = Counter("Hello")
# print(c)

# c = Counter()
# c.update('Updating a Counter')
# print(c['U'])

# for i in c.elements():
# 	print(f"{i}: {c[i]}")

# print(c.most_common(5))

# c1 = Counter("Hello")
# c2 = Counter("There")
# print(c1+c2)
# print(c1&c2)


# # Default Dict
# from collections import defaultdict
# d = defaultdict(lambda: 35)
# d['Ayushi'] = 95
# d['Aditya'] = 25
# d['Sanyam'] = 89
# d['Deepak']

# print(d)
# print(d.__missing__('Adam'))

# d = defaultdict(list)
# a = ('a', "One")
# b = ('b', "Two")
# c = ('c', "Three")
# for key, val in [a,b,c]:
# 	print(key,val)
# 	d[key].append(val)
# print(d['a'])


# # Ordered Dict
# from collections import OrderedDict

# o = OrderedDict()
# o[1] = "a"
# o[2] = "b"
# o[3] = "c"
# o.move_to_end(2, last=False)

# print(o)


# # Named Tuples
# from collections import namedtuple

# colors = namedtuple('color', 'r g b')
# red = colors(r=255, g=0, b=0)
# print(red.r)
# print(red[1])
# print(getattr(red, 'g'))
# print(red._asdict())
# print(red._fields)
# print(red._replace(g=3))

# # Converting an Iterable into a namedtuple
# print(colors._make(['1', '2', '3']))

# # Converting a dict into namedtuple
# print(colors(**{'r': 255, 'g':0, 'b':0}))


# # DATETIME MODULE

# import datetime
# import time

# print(datetime.MAXYEAR)
# print(type(datetime.MINYEAR))
# print(datetime.date.today())

# print(time.time())
# print(datetime.date.fromtimestamp(time.time()+99999))
# print(datetime.date.today().timetuple())

# print(datetime.datetime.today())


# # Python pprint Module

# data=[(1,{'a':'A','b':'B','c':'C','d':'D'}),
# 		(2,{'e':'E','f':'F','g':'G','h':'H','i':'I','j':'J','k':'K','l':'L'}),
# 		(3,['m','n']),
# 		(4,['o','p','q','r','s','t','u','v','w']),
# 		(5,['x','y','z']),]

# print(data)

# from pprint import pprint
# pprint(data)


# class Color:
# 	def __init__(self, name, hex_value):
# 		self.name = name
# 		self.hex_value = hex_value

# 	def __repr__(self):
# 		return('I am '+self.name+' and you can find me at '+self.hex_value)

# colors=[Color('salmon','#FA8072'),Color('olive','#808000'),Color('purple','#800080')]
# print(colors)

# pprint(colors)


# # LIST COMPREHENSION
# mylist = []
# for i in 'anxiety':
# 	mylist.append(i)
# print(mylist)

# mylist1 = [i for i in 'happiness']
# print(mylist1)

# print([i*2 for i in {3,4,2}])

# myset = {3,1,2}
# makelist = lambda i:list(i)
# mylist = makelist(myset)
# print(mylist)

# print(list(map(lambda i:i, myset)))

# print([i for i in range(8) if i%2==0 if i%3==0])

# print(["Even" if i%2==0 else "Odd" for i in range(8)])


# for i in range(7,9):
# 	for j in range(1,11):
# 		print(f"{i} * {j} = {i*j}")
# 	print()


# print([[i*j for j in range(1,11)] for i in range(7,9)])


# # RECURSION

# def factorial(n):
# 	f = 1
# 	while n>0:
# 		f *= n
# 		n -= 1
# 	print(f)

# factorial(4)


# def factorial(n):
# 	if n == 1:
# 		return 1
# 	return n * factorial(n-1)

# print(factorial(5))


# def sumofn(n):
# 	if n == 1:
# 		return 1
# 	return n + sumofn(n-1)

# print(sumofn(16))


# a,b, fib = 0,1,[]
# fib.append(a)
# fib.append(b)

# def fibonacci(n):
# 	if n == 2:
# 		return
# 	global a,b
# 	a,b = b, a+b
# 	fib.append(b)
# 	fibonacci(n-1)

# fibonacci(9)
# print(fib)


# # DECORATORS

# def decorator(func):
# 	def wrap():
# 		print("**********")
# 		func()
# 		print("**********")
# 	return wrap

# @decorator
# def sayhello():
# 	print("Hello")

# sayhello()
# fun = decorator(sayhello)
# fun()


# def divide(a,b):
# 	return a/b

# def decorator(func):
# 	def wrapper(a,b):
# 		if b==0:
# 			print("Can't divide by zero")
# 			return 
# 		return func(a,b)
# 	return wrapper

# fun = decorator(divide)
# print(fun(2,0))


# Chaining decorators

# def dec1(func):
# 	def wrap():
# 		print("*****")
# 		func()
# 		print("*****")
# 	return wrap

# def dec2(func):
# 	def wrap():
# 		print("-----")
# 		func()
# 		print("-----")
# 	return wrap

# @dec2
# @dec1
# def sayhello():
# 	print("Hello World")

# sayhello()


# # GENERATORS

# def counter():
# 	i =1
# 	while (i<=10):
# 		yield i
# 		i += 1

# for i in counter():
# 	print(i)


# def even(x):
# 	while x%2==0:
# 		yield "Even"
# 		break	

# for i in even(2):
# 	print(i)


# def even_squares(x):
# 	for i in range(x):
# 		if i**2%2==0:
# 			yield i**2

# print(list(even_squares(10)))


# mylist = [1,3,6,10]
# a = (x**2 for x in mylist)
# print(next(a))
# print(next(a))
# print(next(a))
# for i in a:
# 	print(i)


# # ITERATORS
# Creating your own iterator

# class PowTwo:
# 	def __init__(self, max=0):
# 		self.max = max

# 	def __iter__(self):
# 		self.n = 0
# 		return self

# 	def __next__(self):
# 		if self.n <= self.max:
# 			result = 2**self.n
# 			self.n += 1
# 			return result
# 		else:
# 			raise StopIteration


# a = PowTwo(4)
# i = iter(a)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))


# # CLASSES AND INHERITANCE

# class fruit:
# 	size = "Small"
# 	def __init__(self, color, shape):
# 		self.color = color
# 		self.shape = shape

# 	def salutation():
# 		print("I am happy")

# fruit.salutation() 

# class Person:
# 	pass

# class Student(Person):
# 	pass

# print(issubclass(Student, Person))

# x = 0
# class Fruit:
# 	def __init__(self):
# 		global x
# 		x += 1
# 		print("I'm a fruit")

# class Citrus(Fruit):
# 	def __init__(self):
# 		super().__init__()
# 		global x
# 		x += 2
# 		print("I'm citrus")

# print(x)

# lime = Citrus()
# # print(lime)

# print(x)


# class Vehicle:
# 	def start(self):
# 		print("Engine Starting")
# 	def stop(self):
# 		print("Engine Stopping")

# class TwoWheeler(Vehicle):
# 	def say(self):
# 		super().start()
# 		print("I have two wheels")
# 		super().stop()

# pulsar = TwoWheeler()
# pulsar.say()


# # DEEP COPY & SHALLOW COPY

# import copy
# list1 = [1,3,[7,4],6]
# list2 = copy.deepcopy(list1)
# list2[2][0] = 5
# print(list1)
# print(list2)

# list3 = [1,3,[7,4],6]
# list4 = copy.copy(list3)
# list2[2][0] = 5
# print(list3)
# print(list4)


# dict1 = {'a':1, 'b':2, 'c':[1,2,3]}
# dict2 = dict1.copy()
# dict2['c'].append(7)
# print(dict1)
# print(dict2)

# dict1 = {'a':1, 'b':2, 'c':[1,2,3]}
# dict2 = copy.deepcopy(dict1)
# dict2['c'].append(7)
# print(dict1)
# print(dict2)


# # PYTHON EXCEPTION

# try:
# 	for i in range(3):
# 		print(3/i)
# except:
# 	print("You divided by 0")
# 	print("This prints because the exception was handled")


# a,b = 1,0
# try:
# 	print(a/b)
# 	print("This won't be printed")
# 	print('10'+10)

# except TypeError:
# 	print("You added values of incompatible types")

# except ZeroDivisionError:
# 	print("You divided by 0")


# a,b=1,0
# try:
#    print(a/b)
# except:
#    print("You can't divide by 0")
# print("Will this be printed?")


# try:
#       print('10'+10)
#       print(1/0)
# except (TypeError,ZeroDivisionError):
#       print("Invalid input")


# try:
#            print('1'+1)
#            print(sum)
#            print(1/0)
# except NameError:
#            print("sum does not exist")
# except ZeroDivisionError:
#            print("Cannot divide by 0")
# except:
#            print("Something went wrong")


# try:
#    print("1")
# print("2")
# except:
#    print("3")


try:
        print(1/0)
except ZeroDivisionError:
        print("This is a value error")
finally:
        print("This will print no matter what.")