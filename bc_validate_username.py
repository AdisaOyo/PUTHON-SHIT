# Validate username input exercise
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username mus not contain digits
""" BRO CODE SOLUTION """
username = input("Enter your username: ")

if len(username) > 12:
    print("Your username can't contain more than 12 characters. Re-enter")
elif not username.find(" ") == -1:
    print("Your username can't spaces spaces. Re-enter")
elif not username.isalpha():
    print("Your username can't contain numbers. Re-enter")
else:
    print("Welcome! You are logged in")


"""
My method: I passed 

username = input("Enter your username: ")
username_num = username.__len__()
username_space = username.__contains__(" ")
username_alpha = username.isalpha()

if username_num < 13 and username_space == False and username_alpha == True:
    print("Welcome! You are logged in!")
else:
    print("Invalid username: can't be more than 12 characers")
"""