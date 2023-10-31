#To echo or display output in python you use print() function e.g
print('Print this text')

#to declare a variable in python you just assign without using any special character like $ in python or var in javascript e.g
myName = "Ifeoluwa"
#to print myName use the print function
print(myName)

# note that variable are case sensitive e.g myName is not equal to MyName or myname. If you declare myName and are trying to use MyName you will get a run-time error. Error message got in the terminal is NameError: name 'MyName' is not defined. Did you mean 'myName'?
# print(MyName) will produce an error

## variable rules
## rule 1 variable can contain uppercase and lowe case letters, digits and underscroe
## rule 2 variable name can not start with a digit (number)
### variale name can contain many different valid unicode character. Unicode can contain non-English alphabets e.g  é and ü

## how to get a good variable name
### your variable name should be self explanatory and this is better than just been short
s = 3600
seconds = 3600

#### it is better to use seconds than s as seconds is more descriptive

#### note that seconds is still not descriptive enough as it did not tell us the amount of seconds or what seconds we are talking about
seconds_per_hour = 3600

#### seconds_per_hour is better than seconds

## variable rule continuation avoid excessively long variable name
## let your variable name be at most 3 to 4 words

## snake casing is more popular in python than came casing
snake_casing = "snake_casing"
camelCasing = "camelCasing"

snake_casing_two ="Each Word In Snake Case Is Usually Seperated By An Underscore"

# snake case was made popular for pythonist in PEP 8 which serve as the official style guide for writing python
# Another Advantage of using Snake Case In Python is that your code can easily be read or worked on by under developers. 

snake_casing