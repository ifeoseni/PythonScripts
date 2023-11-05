# a line of code in python should not be more than 79 characters to seperate it you can use \
string_name = "Ife \
Ade \
"

# to get variable data type use type(variablename)
print(type(string_name))
string_data = "String Length"

string_len = len(string_data)  # to get the number of character in a string
string_substring_one = string_data[1]  # remember to start counting from zero. This will give you t
string_slice = string_data[0:6]  # print from zero to six

string_with_quote = 'I love "Ade" very well. Print with quote' #you can print quote in python
print(string_name)
print(string_len)
print(string_substring_one)
print(string_slice)
print(string_with_quote)

first_string_to_concatenate = "To concatenate use + like is done in JavaScript"
item_to_concatenate_with = ". Add us and see if it works fine"
concatenated_string = first_string_to_concatenate + item_to_concatenate_with

print(concatenated_string)
get_concatenated_length = len(concatenated_string)
print_last_concatenated_string = concatenated_string[get_concatenated_length-1]
create_upperCase = print_last_concatenated_string.upper()
create_lowerCase = print_last_concatenated_string.lower()

print(print_last_concatenated_string)
print(create_upperCase)
print(create_lowerCase)



# TO remove with space you can use .rstrip(), .lstrip(), .strip() in-built string method
my_name = " Oseni "
my_name_no_whitespace = my_name.strip()
print(my_name)
print(my_name_no_whitespace)

# determine what letter starts a word using .startswith('Word') note that it is case sensitive
starship = "Enterprise"
confirm_status = starship.startswith('en')
endswith = starship.endswith('Enterprise')
print(endswith)

