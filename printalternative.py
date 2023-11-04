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