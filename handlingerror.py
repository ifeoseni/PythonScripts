# solution to Write a script that repeatedly asks the user to input an integer, displaying a message to “try again” by catching the ValueError that is raised if the user did not enter an integer. Once the user enters an integer, the program should display the number back to the user and end without crashing.

while True :
    try:
        integer_input =  int(input('Enter an integer'))
        print('Correct')
        break
    except ValueError:
        print('Try again')
    except NameError:
        print("Name Error")

# Write a program that asks the user to input a string and an integer n. Then display the character at index n in the string. Use error handling to make sure the program doesn’t crash if the user does not enter an integer or the index is out of bounds. The program should display a different message depending on what error occurs
while True:
    user_string = input('Enter a string of your choice')
   
    try:
        index_number = int(input('Enter a number of your choice'))
        single_character = user_string[index_number]
        print(f"{single_character}")
        break
    except IndexError:
        print("Error messages")
    except ValueError:
        print("Enter a value")

    
