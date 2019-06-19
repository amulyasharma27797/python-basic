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

