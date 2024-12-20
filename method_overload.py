def product(a, b):
	p = a * b
	print(p)


def product(a, b, c):
	p = a * b*c
	print(p)


# product(4, 5) error


product(4, 5, 5) #correct




# Solution : Method 1 (Not The Most Efficient Method):

# Function to take multiple arguments
def add(datatype, *args):
	if datatype == 'int':
		answer = 0

	if datatype == 'str':
		answer = ''


	for x in args:
		answer = answer + x

	print(answer)


add('int', 5, 6)

add('str', 'Hi ', 'Geeks')



# Solution : Method 2 (Not the efficient one):

def add(a=None, b=None):
	if a != None and b == None:
		print(a)
	else:
		print(a+b)


add(2, 3) #correct
add(2) ##correct



"""
Solution : Method 3 (Efficient One)
    By Using Multiple Dispatch Decorator 
"""

from multipledispatch import dispatch

@dispatch(int, int)
def product(first, second):
	result = first*second
	print(result)


@dispatch(int, int, int)
def product(first, second, third):
	result = first * second * third
	print(result)


@dispatch(float, float, float)
def product(first, second, third):
	result = first * second * third
	print(result)


product(2, 3) # this will give output of 6


product(2, 3, 2) # this will give output of 12


product(2.2, 3.4, 2.3) # this will give output of 17.985999999999997
