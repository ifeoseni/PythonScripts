num1 = 25000000
num2 = 25_000_000 #the same with num1
print(num1)
print(num2)

num = float(175e3)
print(num)

small = 2e308 # n is 308. I achieved this using binary search. In the interactive window, try and find the smallest exponent N so that 2e<N>, where <N> is replaced with your number, returns inf.
print(small)

number1 = 5
number2 = 2
sum = number1 + number2
multiplication = number1 * number2
normaldivision = number1 / number2
integerdivision = number1 // number2  # returns the integer before the decimal
modulus = number1 % number2  # return the number after the division
exponential = number1 ** 2
print(f"Sum of {number1} and {number2} is {sum}")
print(f"multiplication of {number1} and {number2} is {multiplication}")
print(f"normaldivision of {number1} and {number2} is {normaldivision}")  # this will return the decimal value too
print(f"integerdivision of {number1} and {number2} is {integerdivision}")  # this will return the decimal value too
print(f"modulus of {number1} and {number2} is {modulus}")  # this will return the remainder of the division
print(f"exponential of {number1} and {number2} is {exponential}")  # this will return the decimal value too




