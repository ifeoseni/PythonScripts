# list are mutable i.e you can change list value while tuple is immutable
# list are declared using [] while tuple are declared using ()
# list usually contain data of the same data type but like tuple they can contain different data type
list_one = ["red","yellow","green"]
tuple_one = ("red","yellow","green")
print(type(list_one))
print(type(tuple_one))

print(list_one)
print(tuple_one)

list_declaration_two = list("1") # tuple would have been declared using tuple note that this works with string values and using int value will not give you what you want
print(list_declaration_two)

create_list_from_tuple = list(tuple_one)
print(create_list_from_tuple)

create_tuple_from_list = tuple(list_one)
print(create_tuple_from_list)

# you can convert a string that contains list of words seperated by a seperator e.g a comma  using .split(",") where the seperator is ,
listed_string = "Sambo, Ifeoluwa, Daniel"
listed_string_list = listed_string.split(', ')  # note that it is , and a space that is used here because that is what the user used
print(listed_string_list)

# if the seperator used to create a list from a string does not exist. The list will contain all the string as a single list item
seperator_not_found_list = listed_string.split('1')
print(seperator_not_found_list)