if 2 + 2 == 4:
    print("2 and 2 is 4")

if(1 - -5 < 2):
    print(0)
elif 2 +2 == 4:
    print('3')
else:
    print('trie')

prompt = input("Enter any word of your choice ")

if len(prompt) < 5:
    print(f'{prompt} has less than 5 characters')
elif len(prompt) > 5:
    print(f'{prompt} has more than 5 characters')
else:
    print(f'{prompt} has 5 characters')

input_number =  int(input('Enter a number'))
for i in range(1,input_number):
    if input_number % i == 0:
        print(f'{i} is a factor of {input_number}')

request_character = input('Enter a single character')

while request_character.upper() != 'Q':
    request_character = input('Enter a single character')

# method 2
user_input  = input('Input a letter ')
if user_input != 'q' or user_input != 'Q':
    user_input  = int(input('Input a number '))

for i in range(1,50):
    if i % 3 != 0:
        print(f'{i}')