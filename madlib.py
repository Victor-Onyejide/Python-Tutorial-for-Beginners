
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
