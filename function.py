# del keyword is used to unassign a variable

# to create a function use def functionname(argument):
def multiply(x,y):
    product = x * y
    return product
# all function body are indented properly

# not compulsory for function to have return keyword but it should return a value e.g you can use print

# calling of function
num = multiply(2,3)
print(num)

def greet(name):
    print(f'Hello, {name}')

return_name = greet("Ife")
print(return_name)  # returns none because the greet function does not return any value

# to know more about any function use the function help(functionname)
# help(len)  this only works in the IDLE

# to document function in python use a docstring i.e  triple-quoted string literal placed at the top of the function body

def newfunction(x,y):
    """Return the product of two numbers x and y. """
    product = x + y
    return product

# when you use help(userdefinedfunction) the docstring will be shown
# help(newfunction)

#review exercise
def cube(number):
    power_of_three = pow(number,3)
    return power_of_three
see_cube = cube(3)
print(see_cube)
print(cube(2))
