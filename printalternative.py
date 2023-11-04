name = "Ife"
age = 25
print(name,"is ",age)  #age is meant to take str() inbuilt method
print(name + " is "+str(age))

# both method are not recommendd when printing string and number in python

# another method is using the f-string i.e f""
new_printing_style = f"{name} is {age}"
print(new_printing_style)

# review exercise
weight = 0.2
animal = "newt"
print(str(weight) + " kg is the weight of the "+ animal)
print("{} kg is the weight of the {}".format(weight,animal))  # this method is outdated
print(f"{weight} kg is the weight of the {animal}")

# using method find on string s variable.find('word') returns the start character position if it exist or -1 if the word does not exist
find_w = animal.find('wt')
print(find_w)

# note that the find method returns the position of the first occurence of the characcter or word
# you can only pass a strng in the method find i.e find("5") and not find(5)

# to replace all instances of the word that is being looked for use .replace("findword","replaceword")
word = " Names of Beautiful Girls include Odunola, Dasola, Blessing, Janet, Marvelous"
print(word.replace("Janet","Abba"))

# to replace multiple words you need to use the .replace() method multiple times

# exercise
print("AAA".find('a')) #  In one line of code, display the result of trying to .find() the substring "a" in the string "AAA". The result should be -1
n = 2.0
user_input = input("Enter a word ")
print(user_input.find("n"))  # Create the variable n = 2.0. Then use input() to get a string from the user. Finally, display the index of the first occurrence of n in the input string using .find()


