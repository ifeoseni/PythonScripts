# 1. convert the following words to lowercase
animals = "Animals"
badger = "Badger"
honey_bee = "Honey Bee"
honey_badger = "Honeybadger"

animals = animals.lower()
badger = badger.lower()
honey_bee = honey_bee.lower()
honey_badger = honey_badger.lower()

print(animals)
print(badger)
print(honey_bee)
print(honey_badger)

# 2. Convert all to upper case now
animals = animals.upper()
badger = badger.upper()
honey_bee = honey_bee.upper()
honey_badger = honey_badger.upper()

print(animals)
print(badger)
print(honey_bee)
print(honey_badger)

# 3. Write a script that removes whitespace from the following strings:
string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "

string1_rstrip = string1.lstrip()
string2_lstrip = string2.rstrip()
string3_strip  = string3.strip()

print(string1_rstrip)
print(string2_lstrip)
print(string3_strip)

# Write a script that prints out the result of .startswith("be") on each of the following strings:
string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"

check_string1_start_word = string1.startswith("be")
check_string2_start_word = string2.startswith("be")
check_string3_start_word = string3.startswith("be")
check_string4_start_word = string4.startswith("be")

print(check_string1_start_word)
print(check_string2_start_word)
print(check_string3_start_word)
print(check_string4_start_word)

# Using the same four strings from Exercise 4, write a script that uses string methods to alter each string so that .startswith("be") returns True for all of them.
string1 = "be" + string1[2:]
string2 = "be" + string2[2:]
string3 = "be" + string3[2:]
string4 = "be" + string4[3:]
check_string1_start_word = string1.startswith("be")
check_string2_start_word = string2.startswith("be")
check_string3_start_word = string3.startswith("be")
check_string4_start_word = string4.startswith("be")
print(string4)
print(check_string1_start_word)
print(check_string2_start_word)
print(check_string3_start_word)
print(check_string4_start_word)
