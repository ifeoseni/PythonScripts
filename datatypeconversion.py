num = input("Enter a number ")
num = float(num)
print(type(num))
sum = num + 3
print(sum)
# result will be a floating number to get an integer use int()

# convert number to string
num = str(num)
print("I need "+num + " ladies")
print(type(num))

# task
first_number = input("Enter first number ")
second_number = input("Ener the multiplier number ")
number_one_integer = int(first_number)
number_two_integer = int(second_number)
multiplied_value = number_one_integer * number_two_integer
print("Multiplication of "+ first_number + " and "+second_number + " is "+ str(float(multiplied_value))  )