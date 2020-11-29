
# Types

# name = "Victor"  # STRING
# last_name = 'Onyejide'  # STRING
# age = 22  # Integer

# print(name + " " + last_name + " " + str(age))


# Mandlib Genreator

story = """
My name is {}. I am {}
I do not like people that {}
"""

# Getting Input from user
blank_1 = input("Enter a noun/adjective: ")
blank_2 = input("Enter a noun/adjective: ")
blank_3 = input("Enter a noun/adjective: ")


print(story.format(blank_1, blank_2, blank_3))


# TYPES

# int(anyData) #any into integer
# str(anyData) #any into string
# ord(chr) #character into number
# hex(int) #integer into hexadecimal string
# oct(int) #integer into octal string
# float(anyData) #any into float
# tuple() #convert to tuple
# set() #returns the type after converting to set
# list() #convert any data type to a list
# dict() #convert a tuple of order (key,value) into a dictionary
# complex(real,imag) #converts real numbers to complex(real,imag) number
