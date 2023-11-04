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

# other methods used for numbers include round(number),abs(number) and pow(number)

# round(2.5) will return 2 because the number before the 5 is an even number. If it is a odd number it will e rounded up

# using round(number,amount) will show the amount of decimal unit after integer. Note that amount must be an integer

# difference between pow and ** is that pow can take 3 argument which are pow(number,power,powervaluemodulusthisamount)
pow(2,3,4)  # 2 ** 3 %4 = 8 % 4 = 0

# only number method that comes after the number like string .lower() is is_number()

# revision exercise
number = input("Enter number")
two_dp = round(float(number),2)  # anserr to number 1
print(two_dp)
absolute = abs(two_dp)

print(two_dp)
print(absolute)

number2 = input('Enter second number')
difference = two_dp - float(number2)
abs_number = abs(difference)

check_if_number = abs_number.is_integer()
print(check_if_number)

n = 3233
print(f"{n: ,.4f}")  # using , will group in 3s and the 4f will be rounded up or down to 4 digit

print(f'Naira {n: ,.2f}')  # used for currency

# use of %
ratio = 0.5
print(f'Ratio is {ratio: .1%}')  # this will convert your text to ratio

# note that the .n% and .nf can not go together

# 5.6 exercise
expo = 3 ** .125
print(f"{expo: ,.3f}")
currency = 150000
print(f'{currency: ,.2f}')
two_ratio = 2 / 10
print(f'{two_ratio: .0%}')

# 5.7 complex number
n = 1 + 2j  #where n = 1i + 2j
n_real = n.real
n_imag = n.imag
n_conjugate = n.conjugate()  # returns the formula
print(f'{n.real} is the real number and {n.imag} is the imaginary number')