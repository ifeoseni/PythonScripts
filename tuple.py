# tuple are like strings but work like a list or an array. It can be declared using () or tuple or by writing the values with a comma. To declare a single tuple value that is an integer you should have a , after it e.g (1,) is a tuple but (1) is not
# for a single strin

first_tuple = ('P','Y','T','O','N')
print(type(first_tuple))
string_that_is_not_a_tuple = ("Python") # is a string but tuple("Python") is a tuple
print(type(string_that_is_not_a_tuple))

tuple_two = tuple("Python")

print(type(tuple_two))

# Exercise Create a tuple literal named cardinal_numbers that holds the strings "first", "second" and "third", in that order
cardinal_numbers = ("first","second","third")
print(type(cardinal_numbers))
cardinal_numbers_index_one = cardinal_numbers[1]
print(cardinal_numbers_index_one)

position1, position2, position3 = "first","second","third"
print(position1)
print(position2)
print(position3)

my_name = tuple("Ifeoluwa")
checking_x = "x" in my_name # note that we did not include the for keyword and the x is in quote because it is a string
print(checking_x)
my_name_without_I = my_name[1:]
print(my_name_without_I)

# tuple is immutatble i.e the values can't be changed unless you create another tuple with the new value