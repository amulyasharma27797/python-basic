def add_num(a,b):
	"""Using f-stings to add two numbers using functions"""
	print(f"{a} + {b} = {a+b}")
add_num(3,4)


def add_number(a,b):
	"""Using return statement"""
	return(f"{a} + {b} = {a+b}")
print(add_number(3,4))


def greet(name="User"):
	"""Default argument in python"""
	return(f"Hello, {name}")
print(greet())


def say(*names):
	"""Arbitrary Arguments"""
	for name in names: 
		print(f"Hello, {name}")
say("Ayushi", "Gaurav", "Sanyam")


# Enumerator
for i in enumerate([1,2,3,4,]):
	print(i)


# Filter
p = list(filter(lambda x:x%2==0, [4,3,1,2,0,False]))
print(p)


# getattr()
class Person:
	name="Aditya"
	age=21

person = Person()
print(getattr(person, 'age'))


# Class Methods
class Car:
	def __init__(self, brand, model, color, fuel):
		self.brand = brand
		self.model = model
		self.color = color
		self.fuel = fuel

	def start(self):
		print(f"Car {self.model} is start")

	def stop(self):
		pass

	def turn(self):
		pass

blackverna = Car('Hyundai', 'Verna', 'Black', 'Diesel')
blackverna.start()


# Python Method
class Try:
	def __init__(self):
		pass

	def printhello(self, name):
		print(f"Hello {name}")
		# return name

obj = Try()
obj.printhello('Ayushi')



class Try:

	def printhello(self, name):
		# print(f"Hello {name}")
		return (f"Hello {name}")

obj = Try()
# obj.printhello('Ayushi')


# Constructors
class three:
	def __init__(self):
		self.val = int(input("Enter your value \n"))

t = three()
print(t.val)


class one:
	def __init__(self, a):
		print(a)

o = one('a')



# zip()
for i in zip([1,2,3,4,5,6], [4,5,6,7,8]):
	print(i)


z = zip([1,2], [3,4])
a,b = zip(*z)
print(a,b)


# eval()
print(eval('[1,2,3][2]'))


# Iterating in list
for i in [1,2,3]:
	if i%2==0:
		print(f"{i} is composite\n")

# Tuples unpacking
mytuple = (1,2,3)
a,b,c = mytuple
print(mytuple)
print(a,b,c)
# del mytuple
print(mytuple)


# List Comprehension
even = [2*i for i in range(1,11)]
print(even)

even = [2*i for i in range(1,11) if i%3==0]
print(even)


# COLLECTIONS MODULE IN PYTHON

# Counters
from collections import Counter
c = Counter("Hello")
print(c)

c = Counter()
c.update('Updating a Counter')
print(c['U'])

for i in c.elements():
	print(f"{i}: {c[i]}")

print(c.most_common(5))

c1 = Counter("Hello")
c2 = Counter("There")
print(c1+c2)
print(c1&c2)


# Default Dict
from collections import defaultdict
d = defaultdict(lambda: 35)
d['Ayushi'] = 95
d['Aditya'] = 25
d['Sanyam'] = 89
d['Deepak']

print(d)
print(d.__missing__('Adam'))

d = defaultdict(list)
a = ('a', "One")
b = ('b', "Two")
c = ('c', "Three")
for key, val in [a,b,c]:
	print(key,val)
	d[key].append(val)
print(d['a'])


# Ordered Dict
from collections import OrderedDict

o = OrderedDict()
o[1] = "a"
o[2] = "b"
o[3] = "c"
o.move_to_end(2, last=False)

print(o)


# Named Tuples
from collections import namedtuple

colors = namedtuple('color', 'r g b')
red = colors(r=255, g=0, b=0)
print(red.r)
print(red[1])
print(getattr(red, 'g'))
print(red._asdict())
print(red._fields)
print(red._replace(g=3))

# Converting an Iterable into a namedtuple
print(colors._make(['1', '2', '3']))

# Converting a dict into namedtuple
print(colors(**{'r': 255, 'g':0, 'b':0}))
