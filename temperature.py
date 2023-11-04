def convert_cel_to_far(celsius):
    Fahrenheit = celsius * 9/5 + 32
    return Fahrenheit

def convert_far_to_cel(fahrenheit):
    Celsius = (fahrenheit - 32) * 5 / 9
    return Celsius
user_selected_number = float(input("Enter your preferred number"))
# number = float(user_selected_number)
far = convert_cel_to_far(user_selected_number)
cel = convert_far_to_cel(user_selected_number)

print(f'Fahreneheit Value of {user_selected_number} is {far: .4f} while the celsius value is {cel: .1f}')

# loop
n = 1  # declared the first part of the loop 
while n < 5:  # condition of the loop
    print(n)
    n = n+1  # change in the loop that prevent infinite loop

get_number = float(input(" Enter a  positive number"))
while get_number <= 0:
    print("This is not a positive number")
    get_number = float(input(" Enter a  positive number"))

# for loop
for x in "Python":
    print(x)

word = "Python"
position = 0

while position < len(word):
    print(word[position])
    position += 1

for n in range(3):  # the range is 0,1,2 range(1,5) will do 1,2,3,4
    print("Python")  # this will print python thrice

# review exercises

for z in range(2,10):  # you cn not declare the z outside the loop
    print(z)

num_2 = 2
while num_2 < 10:
    print(num_2)
    num_2 += 1

def doubles(n):
    twice = n * 2
    return twice
num_2 = 2
result = doubles(num_2)
print(f"Result is {result}")
k = 2
for i in range(0,3):    
    print("Result is ")
    print(doubles(k) )
    k = doubles(k)
    
