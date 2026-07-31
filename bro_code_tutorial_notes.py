"""
Variables = A container fro a value (string, integer, boolean, float)
               A variable behaves as if it was the value it contains
"""
# Strings
frist_name = "Bro"
food = "pizza"
email = "Bro123@fake.com"

# Integers
age1 = 25
quantity = 3
num_of_students = 3

# Float
price = 10.99
gpa1 = 3.2
distance = 5.5

# Boolean
is_student1 = True
fro_sale = False
is_online = False

if is_online:
    print ("You are online!")
else: 
    print ("You are offline!")


"""
Typecasting = The process of converting one data type to another
                 str(), int(), float(), bool().
"""
name = "Bro code"
age = 25
gpa = 3.2
is_student = True

type(name)
print (type(name))

gpa = int(gpa)
print (gpa)

age = float(age)
print (age)


"""
input = A function that prompts the user to enter data
        Returns the entered data as a sting
"""
age2 = input("What is your age? \n")
#convert input to int and print type of data after conversion
age2 = int(age2)
print ("Your age is an",type(age2),"type of data")

# A better way to type cast is to jst embed the data into the type cast
#   e.g int( 
#            input("What is your name?")
#           )

"""
math stuff
"""

# we have normal math operators like +, -, /, *
# we also have a modulus (%) which gives us the remander of any division and exponetiation (**) which is basically raised tothe power of
friends = 10
remainder = friends%3
print(remainder)
power = friends**3
print(power)

#math functions [round(), abs(), max(), min() ]
# abs() is for getting absolute values
# max() is used to get the max value between various values
# min() does the opposite of max()

#  instead of using ** i can use pow(4, 3)
round(power,2)
non_abs = -4.67
absolute = abs(non_abs)
print(absolute)
print(non_abs)
print(pow(absolute, 3))
maximum = max (non_abs, absolute, friends)
print(maximum)

# If there are math stuff you need to do asides opperatiors you need the import math function
# To activate the libraray just use import math at start of code

import math

# These are the functions I can get. There may be more 
print(math.pi)
print(math.e)

sqr = math.sqrt(4)
print(sqr)
#math.ceil() will always round floats up
#  math.floor() deos the opposite of math.ceil()
ceil = math.ceil(absolute)
print(ceil)

# If/Else statements are used to Do some code only if some condition is True
#  Else do something else
user_age = int(
    input("What is your age? ")
)

if user_age >= 18:
    print("You are now signed up")
# use the elif statement to give anoher condition that can be used
elif user_age < 13:
    print("You are even too young to use a bank lol")
elif user_age >12:
    print("You must be 18+ to sign up")

# try: statement is used to check thing as conditionals and then continue code basd on their arguments
"""
try:
    num1 = float(num1)
except ValueError:
    num1 = input("Input valid first number!")
try:
    num1 = float(num1)
except ValueError:
    num2 = input("Input valid first number!")
if operator == "+":
    output = float(num1) + float(num2)
    print(output)
elif operator == "-":
    output = float(num1) - float(num2)
    print(output)
elif operator == "*":
    output = float(num1) * float(num2)
    print(output)
elif operator == "/":
    output = float(num1) / float(num2)
    print(output)
else:
    input("Invalid opertor! Give valid operator: ")
"""

"""
Logical operators = evaluate multiple conditions (or, and, not)
                    or = at least one codition must be True
                    and = both conditions must be True
                    not = inverts the condition (not False, not True)
"""

temp = 36
is_raining = False
is_sunny = False
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is canceled")
else:
    print("The outdoor event is still on")

if temp > 28 and is_sunny:
    print("It's HOT outside")
elif temp >= 28 and is_sunny:
    print("It is HOT outside 🥵") 
    print("It is sunny ☀️")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside 🥵") 
    print("It is cloudy ☁️")
elif temp <= 0 and is_sunny:
    print("It is COLD outside ❄️") 
    print("It is cloudy ☁️")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside ❄️") 
    print("It is cloudy ☁️")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside")
    print("It is cloudy ☁️")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside")
    print("It is sunny ☀️")

"""
conditional expressions = A one-line shortcut for the if-else statement (ternary operator)
                          Print or assign one of two values based on a condition
                          X if condition else Y
"""

num = 5
print("Positive" if num > 0 else "Negative")
print("EVEN" if num%2 == 0 else "ODD")

""" MORE ON STRINGS """
oruko = input("What is your name?")
#result = len(name)  to find the length of input str or any str
#result = name.find(" ")  Is used to tell where the instance of whatever is in find(""). Always start counting from 0
#result = name.rfind(" ") Is used to find last occurence of a str
    ## if python cannot find any result it will return value of -1
# name = name.capitalize() capitalized first letter of a str
# name = name.upper() capitalized all letters of str
# name = name.lower() changes str to all lower case
#result = name.isdigit() used to check if input is a digit and returns True or False value depending on answer
      ##oruko = oruko.isdecimal() for decimals
      ##name = name.isalpha() to check if input is only alphabets. if input has space it will be False. It would be wise to use .strip() with this one when handling str data
# phone_number = phone_number.count("-") used to check the number of what is in the .count("") whithin the input
# phone_number = phone_number.replace("-", " ") used to replace first "" with second "" after he comma

## Get all you can do with str by using help(str) can probably use for other statements too idk
print(oruko)

"""
str indexing = accessing elements of a sequence using [] (indexing operator)
            [start : end : step]
"""
credit_number = "1234-5678-9012-3456"

print(credit_number[4])
print(credit_number[0:4]) #[:4] would also work
print(credit_number[5:9]) #you need to count the spaces yourself too lol
print(credit_number[15:20])
print(credit_number[5:]) #to get from that point to end 
print(credit_number[-1]) #you can use negative indexing. this is to get the last number

print(credit_number[::2]) # prints every [:: ] character in the str
last_four_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{credit_number[-4:]}")
print(credit_number[:: -1]) #This reverses input str


## This is me geeking out. I want to do the collecting it if there are o dashes and making it make sense sti ...... nigga I can't do all that yet. 
#     Well will you look at that, I figured it out lool
access = "1234-5678-9012-3456"
credit_number2 = input("What is your credit card number?: ") #"123456789123456"
#fourth = credit_number2[4:]
fifth_to_eight = credit_number2[4:8:]


cr2 = str (credit_number2.replace(credit_number2,credit_number2[:4]))+"-"
cr3 = str (credit_number2.replace(credit_number2, credit_number2[4:8]))+"-"
cr4 = str (credit_number2.replace(credit_number2, credit_number2[8:12]))+"-"
cr5 = str (credit_number2.replace(credit_number2, credit_number2[12:16]))
num = cr2 + cr3 + cr4 + cr5
#print (cr2)
#print (cr3)
Your_card_num_corrected = num
credit_number2_num_check = len(credit_number2)

print(f"XXXX-XXXX-XXXX-"+Your_card_num_corrected[-4:])
''' 
try:
    credit_number2_num_check < 19
except False:
    print("Too amny nmbers")
    ''' 
if credit_number2_num_check == 16 and Your_card_num_corrected == access:
    print("Transaction success")
elif credit_number2_num_check > 16 and Your_card_num_corrected == access:
    print("Too many numbers")
elif credit_number2_num_check < 16 and not Your_card_num_corrected == access:
    print("Card Number Incomplete!")
else:
    print("ACCESS DENIED")

#print(Your_card_num_corrected)
#print (cr3)

"""
Format specifiers : = {value : flags} format a value based on what flags are iserted

          :.(number)f = round to that many decimal places (fixed point)
          :(number) = allocate that many spaces
          :03 = allocate and zero pad that many spaces
          :< = left justify
          :> = right justify
          :^ = centre align
          :+ = use a plus sign to indicate positive value
          := = place sign to left most position
          :  = insert a space before positive numbers
          :, = comma seperator
"""


price1 = 30000.1214
price2 = -900000.77
price3 = 120000.3444
print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")

print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")

print(f"Price 1 is ${price1:050}$")
print(f"Price 2 is ${price2:050}$")
print(f"Price 3 is ${price3:050}$")
#
print(f"Price 1 is ${price1:010}$")
print(f"Price 2 is ${price2:010}$")
print(f"Price 3 is ${price3:010}$")

print(f"Price 1 is ${price1:<10}$")
print(f"Price 2 is ${price2:<10}$")
print(f"Price 3 is ${price3:<10}$")

print(f"Price 1 is ${price1:>10}$")
print(f"Price 2 is ${price2:>10}$")
print(f"Price 3 is ${price3:>10}$")

print(f"Price 1 is ${price1:^10}$")
print(f"Price 2 is ${price2:^10}$")
print(f"Price 3 is ${price3:^10}$")

print(f"Price 1 is ${price1:+}$")
print(f"Price 2 is ${price2:+}$")
print(f"Price 3 is ${price3:+}$")

print(f"Price 1 is ${price1: }$")
print(f"Price 2 is ${price2: }$")
print(f"Price 3 is ${price3: }$")

print(f"Price 1c is ${price1:,}$")
print(f"Price 2c is ${price2:,}$")
print(f"Price 3c is ${price3:,}$")

print(f"Price 1 is ${price1:=}$")
print(f"Price 2 is ${price2:=}$")
print(f"Price 3 is ${price3:=}$")


"""
While Loop: Execute some coe WHILE some condition remains true
"""

name = input("Enter name: ")

while name == "":
    print("You did not give input! Reenter: ")
    name = input("Enter name: ")
else:
    print(f"Hello, {name}!")
num = 0
while True:
    num = float(input("What is the number?: "))
    if num > 0:
        print("number is greater than 0")
    else:
        break

"""
For loops = execute a block of code a fixed number of times.
            you can iterate over a range, string, sequence, etc.
"""

for x in range(1, 11):
    print(x)

for x in reversed(range(1, 11)):
    print ("HAPPY NEW YEAR")

for x in reversed(range(1, 11, 2)):
    print(x)

credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)

## continue and break are useful keywords in while and for loops

for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x)
## continue skips over an iteration while break will end loop
for x in range(1,21):
    if x == 13:
        break
    else:
        print(x)


## import.time to import time modules
#time.sleep makes the computer sleep for a given time in seconds before executing code
"""
Nested loop = A loop within another loop (outer, inner)
              Outer loop:
                  inner loop:
"""
for z in range(3):
    for x in range(1,10):
        print(x, end ="")
    print()
## use end in for loops to specify what you would like each iteration to end with instead of the default new line 
    for y in range(1,10):
        print(y, end = "yayy")
    print()


"""
collection = single "variable" used to store multiple values
    List = [] ordered and changeable. Duplicates OK
    Set  = {} unordered and immutable, but Add/Remove OK. NO duplicates
    Tuple= () ordered and unchangeable. Duplicates OK. FASTER
"""

fruits = ("apple", "orange", "bannana", "coconut")
## LISTS ##
'''
print(fruits[0])
print(len(fruits))
print("orange" in fruits) #find if a value is in a collection. prints a boolean answer
fruits[0] = "pineaple" #replace element in collection
fruits.append("mango") #add to end of collection
fruits.remove("orange") #remove element from collection
fruits.insert(0, "tiger") #insert value at given index
fruits.sort() #sorts list in ascendign order alphabetically not sure about numerically yet
fruits.reverse() #reverses a list and are reversed based on placement order in list. I only got t=reverse alphabetical output because i had sorted the list
#fruits.clear() #removes all elements in list
print(fruits.index("mango")) # prints index of an element in a list provided
print(fruits.count("bannana")) #counts number of given element in a list
for fruit in fruits:
    print(fruit)
'''
##print(dir(fruits)) #used to check for methods available to a collection
##help(fruits) #gives description of all usable attributes
'''
## SET ##
print(fruits) #always comes back in a different order
print(len(fruits))
print("orange" in fruits) #find if a value is in a collection. prints a boolean answer
##cannot use indexing in set so fruits[0] = "leg" will not work
fruits.add("pineaple")
fruits.remove("apple")
#fruits.pop() #removes first element, Remeber, always random
#fruits.clear() #removes all elements in list
fruits.add("orange") #sets don't accept duplicates
print(fruits)
'''
## TUPLE ##

print(fruits)
print(len(fruits))
print("orange" in fruits) #find if a value is in a collection. prints a boolean answer
print(fruits.index("bannana")) #prints index of an element in a tuple provided
print(fruits.count("bannana")) #counts number of given element in a tuple

### 2D LISTS or tuples ###

#it is a list of lists, or a list of tuples, or a tuple of lists, or a tuple of tuples
###
#fruits = ["apple", "banana", "orange"]
#vegetables = ["carrot", "broccoli", "spinach"]
#meats = ["chicken", "beef", "pork"]
# grocery_list = [fruits, vegetables, meats]
###
# I can also declare 2d lists like this:

grocery_list = [["apple", "banana", "orange"],
                ["carrot", "broccoli", "spinach"],
                ["chicken", "beef", "pork"]]

#fruits[0] = "grape"
for collection in grocery_list:
    for food in collection:
        print(food, end = " ") 
    print() #this is for new line after each collection.
print(grocery_list[0][0]) #this prints grape. second [] is for element is inner list.

"""
dictionary = a collection of {key: value} pairs.
             ordered and changeable. No duplicates. 
"""

#creating a dictionary of country and capitals

capitals = {
    "USA": "Washington DC",
    "Canada": "Ottawa",
    "UK": "London"
}

print(capitals) #prints the whole dictionary
print(capitals["USA"]) #prints the value of the key "USA"
print(capitals.get("UK")) #prints the value of the key "UK"

if capitals.get("Canada"):
    print("That key exists.")
else:
    print("That key does not exist.")

capitals["Germany"] = "Berlin" #adds a new key-value pair to the dictionary
print(capitals)
capitals.update({"France": "Paris"}) #adds a new key-value pair to the dictionary using the update method
print(capitals)
capitals.pop("UK") #removes the key-value pair with the key "UK"
print(capitals)
capitals.popitem() #removes the last key-value pair added to the dictionary
print(capitals)
#capitals.clear() #removes all key-value pairs from the dictionary
#print(capitals)
keys = capitals.keys() #returns a list of all the keys in the dictionary
print(keys)
reversed
for key in capitals.keys(): #loops through the keys in the dictionary
    print(key) 

values = capitals.values() #returns a list of all the values in the dictionary
print(values)
for value in capitals.values(): #loops through the values in the dictionary
    print(value)

items = capitals.items() #returns a list of all the key-value pairs in the dictionary as tuples
print(items)
for item in capitals.items(): #loops through the key-value pairs in the dictionary
    print(item)
for key, value in capitals.items(): #loops through the key-value pairs in the dictionary and unpacks them into key and value variables
    print(f"{key}: {value}")

###RANDOM MODULE###
import random

#print(help(random))

low = 1
high = 100
number = random.randint(low, high)
print(number)
num = random.random() #this will give us a random number between 0 and 1
print(num)

options = ["rock", "paper", "scissors"]
choice = random.choice(options) #this will give us a random choice from the list of options
print(choice)
cards = ["2 of Hearts", "3 of Diamonds", "4 of Clubs", "5 of Spades", "6 of Hearts", "7 of Diamonds", "8 of Clubs", "9 of Spades", "10 of Hearts", "Jack of Diamonds", "Queen of Clubs", "King of Spades", "Ace of Hearts"]
random.shuffle(cards) #this will shuffle the list of cards
print(cards)


# Program to simulate a concession stand at a movie theater.
# The program will allow the user to select items from a menu and calculate the total cost.

menu = {
    "popcorn": 5.00,
    "candy": 2.50,
    "soda": 3.00,
    "water": 2.00,
    "nachos": 4.50,
    "fries": 3.50,
    "hot dog": 4.00,
    "chips": 2.00,
    "pretzel": 3.00,
    "lemonade": 3.50
}

order = []
total_cost = 0
print("Welcome to the movie theater concession stand!")
print("----------------MENUE----------------")
for key, value in menu.items():
    print(f"{key.title():12}: ${value:.2f}")
print("-------------------------------------")
while True:
    item = input("What would you like to order? (Type 'q' to finish): ").lower()
    if item == "q":
        break
    elif item in menu:
        order.append(item)
        total_cost += menu[item]
        print(f"{item.title()} added to your order. Current total: ${total_cost:.2f}")
    else:
        print("Sorry, we don't have that item. Please choose from the menu.")
print("-------------ORDER SUMMARY-------------")
for item in order:
    print(f"{item.title():12}: ${menu[item]:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
print("Thank you for your order!")

'''
Default argument = A default value for certain parameters
                   defalt is used when that argument is ommited
                   make your functions more flexible, reduces # of arguments
                   1. Positional, 2. DEFAULT, 3. Keyword, 4. Arbitrary
'''

def net_price(list_price, discount=0, tax=0.05):
    return list_price*(1-discount)*(1+tax)

print(net_price(500,0.3,0.06))

### Keyword argument = an argument preceeded by an identifier
#                      helps with readability
#                      order of arrangement does not matter

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

print(hello("Hello", title="Mr.", first="Joshua", last="King")) #possitional arguments must always come first

for x in range(1,11):
    print(x, end=" ")

### *args = allows to pass multiple non-key argements
# **kwargs = allows you to pass multiple keyword-arguments
#          * is the unpacking operator
#            1. positional 2. default 3. keyword 4. ARBITRARY

'''
args packs all the arguments into a tupple while kwargs packs them into a dictionary
'''

def add(*args):
    #return a+b
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,5,6))

def display_name(*names):
    for name in names:
        print(name, end=" ")

display_name("Dr", "Spongebon", "Squarepants")
print()
def print_addrss(**kwargs):
    for value in kwargs.values():
        print(value)
    for key in kwargs.keys():
        print(key)
    for key, value in kwargs.items():
        print(f"{key}:{value}")
print_addrss(street ="123 Fake St", 
             apt = 100,
             city="Detroit", 
             state="Michigan", 
             zip="1234")


'''
Iterables = An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop
'''

numbers = [1,2,3,4,5] #lists are iterable

for number in numbers:
    print(number)

fruits = {"apple", "orange", "banana", "coconut"} #sets are also iterables. They are not reversable

for fruit in fruits:
    print(fruit)

name = "Bro Code"

for character in name:
    print(character, end = " ")
print()
my_dictionary = {"A":1, "B":2, "C":3,}  #Dictionaries are also iterables, they return all the keys but not values when iterated over

for key in my_dictionary: #for getting the keys
    print(key) 

for value in my_dictionary.values(): #for getting the values
    print(value) 

for key, value in my_dictionary.items(): #for getting the keys and values
    print(f"{key}: {value}") 
# or i can code it like...
for key, value in my_dictionary.items():
    print(key,value)


'''
Membership operators = used to test weather a value or variable is found in a sequence
                       (string, list, tuble, set, or dictionary)
                       1. in
                       2. not in
'''

word = "APPLE"

letter = input("Guess a letter in the secret word: ").capitalize()

if letter in word:
    print(f"There is a {letter}")
else:
    print("Letter not found")
# do the opposite with 'not in'

students = {"Spongebob", "Sandy", "Patrick"}
student = input("Enter the name of a student: ")
if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} not found")

grades = {
    "Sandy":"A",
    "Squidward":"B",
    "Spongebob":"C",
    "Patrick":"D"
}

student = input("Enter the name of a student: ")
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")

email = "Brocode@gmail.com"
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email!!")

'''
List comprehenson = A concise way to create lists in python
                   Compact and easier to read than traditional loops
                   [expression for value in iterable if condition]
'''
'''
doubles = []
for x in range(1,11):
    doubles.append(x*2)

print(doubles)
'''
#now to make it more concise
doubles = [x*2 for x in range(1,11)]
print(doubles)

fruits = ["Apple", "Orange", "Banana", "Coconut"]
fruits = [fruit.upper() for fruit in fruits]
fruits = [fruit[0] for fruit in fruits]
print(fruits)

numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_nums = [num for num in numbers if num>=0]
negative_nums = [num for num in numbers if num<0]
even_num = [num for num in numbers if num%2 == 0]
print(positive_nums)
print(negative_nums)
print(even_num)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade>=60]
print(passing_grades)


'''
Match-case statement (switch): An alternative to using many 'elif' statements
                               Execute some code if a value maches a case
                               Benefits: cleaner and syntax is more readable
'''

from unittest import case


def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:
            return "Invalid day"

print(day_of_week(1)) 

def weekend(day):
    match day:
        case "Sunday": 
            return "It is the weekend"
        case "Monday":
            return "It is a weekday"
        case "Tuesday":
            return "It is a weekday"
        case "Wednesday":
            return "It is a weekday"    
        case "Thursday":
            return "It is a weekday"
        case "Friday":
            return "It is a weekday"
        case "Saturday":
            return "It is the weekend"
        case _:
            return "Invalid day"
        
print(weekend("Sunday"))

# or
def weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return "It is the weekend"
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "It is a weekday"
print(weekend("Sunday"))

'''
    if day == 1:
        return "It is Sunday"
    elif day == 2:
        return "It is Monday"
    elif day == 3:
        return "It is Tuesday"
    elif day == 4:
        return "It is Wednesday"
    elif day == 5:
        return "It is Thursday"
    elif day == 6:
        return "It is Friday"
    elif day == 7:
        return "It is Saturday"
    else:
        return "Invalid day"
    
print(day_of_week(1))
'''

'''
Module = a file containing code you want to include in your program.
         use 'import' to include a module in your program. (built-in modules, third-party modules, and user-defined modules)
         useful to break up a large program reusable seperate files
'''
#help('modules')
#print(help('modules'))

import math
import math as m #using an alias to reduce typing
#from math import pi # using from to geth a fincion from a module. takes a lot f writing space do not recommend
#print(m.pi)

#to create a module 

# 1. right click on project folder > new > python file

import bc_mod_exaple as example

result = example.pi
result = example.square(3)
result = example.cube(3)
result = example.area(3)
result = example.circumference(3)

print(result)

'''
# Variable scope = where a variable is visible and accessible
# Scope resolution = (LEGB) Local-> Enclosed-> Global-> Built-in. This is how python would use your variables sort of like BODMAS
'''
'''
LOCAL
def func1():
    a=1
    print(a)
def func2():
    b=2
    print(b)
'''
'''
ENCLOSED
def func1():
    a=1
    
    def func2():
        print(a)
    func2()

func1()
'''
'''
GLOBAL
def func1():
    print(a)
def func2():
    print(a)

a = 3 
func1()
func2()
'''
'''
BUILT-IN
from math import e
def func1():
    print(e)

#e =4
print(e)
func1()
'''
# Variables declared within a function have a local scope

'''
if __name__==__main__: (this script can be imported OR run standalone)
                       Functions and classes in this module can be reused
                       without the main block of code executing
Good practice (code is modular,
               helps readability,
               leaves no global variables,
               avoid unintended execution)

               ex. library  import library functionality 
               when running library directly, display a help page
'''

#def main():
#    #Your code goes here

#if __name__=='__main__':
#    main()
#from bc_script2 import * # * means to import everything

#print(__name__)

#def favourite_food(food):
#   print(f"Your favourite food is {food}")
#def main():
#    print("This is script 1")
#    favourite_food("pizza")
#    print("Goodbye")

#if __name__ == '__main__':
#    main()
#without the if statement __name__ the code would run everything without giving me a chance to chose what part of it i want to run


### OBJECT ORIENTED PROGRAMMING ###
'''
Object = A "bundle" of related attributes (variables) and methods (functions)
         Ex. phone, cup, book
         You need a "class" to create many objects

#class = (blueprint) used to design the structure and layout of an object
'''
from bc_car import Car

car1 = Car("Mustang", 2024, "Red", False)
car2 = Car("Corvet", 2025, "Blue", True)

print(car1.model)
print(car1.year)
print(car1.colour)
print(car1.for_sale,"\n")
 
print(car2.model)
print(car2.year)
print(car2.colour)
print(car2.for_sale)

car1.drive()
car2.stop()
car1.describe()

'''
Class variables = Shared among all instances of a class
                  Defined outside the constructor
                  Allow you to share data among all objects created from that class
'''

class Student:

    class_year = 2024
    num_students = 0


    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students +=1


student1 = Student("Spongebob", 30)
student2 = Student("Sandy", 25)
student3 = Student("Squidward", 55)

print(student1.name)
print(student2.age)
print(Student.class_year) #It is goood practice to access class variables with the class name instead of like this #print(student1.class_year)
print(Student.num_students)

'''
Inheritance = Allows a class to inherit attributes and methods from another class
              Helps with code reusability and extensibility
              class Child(Paent)
'''

class Animal:

    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF")
class Cat(Animal):
    def speak(self):
        print("MEOW")
class Mouse(Animal):
    def speak(self):
        print("SQEAK")

dog = Dog("Scubby")
cat = Cat("Tom")
mouse = Mouse("Jerry")

print(dog.name)
print(cat.is_alive)
mouse.eat()
dog.sleep()

cat.speak()

'''
multiple inheritance = inheritance from more than one parent class
                       C(A, B)
multilevel inheritance = inheritance from a parent which iherits from another parent
                         C(B) <- B(A) <- A
'''
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Buggs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
rabbit.eat()
fish.sleep()


'''
super() = Function used in a child class to call methods from a parent class (superclass)
          Allows you to extend the functionality of the inherited methods
'''

class Shape:
    def __init__(self, colour, is_filled):
        self.colour = colour
        self.is_filled = is_filled
    def describe(self):
        print(f"It is {self.colour} and {'filled' if self.is_filled else 'not filled'}")
class Circle(Shape):
    def __init__(self, colour, is_filled, radius):
        super().__init__(colour, is_filled)
        self.radius = radius
    def describe(self):
        print(f"It is a circle with an area of {3.14 * pow(self.radius, 2)}") ## If a child has similar methd to the parent the child's method will be used instead of and or before the parent method
        super().describe()
class Square(Shape):
    def __init__(self, colour, is_filled, width, length):
        super().__init__(colour, is_filled)
        self.width = width
        self.length = length
class Triangle(Shape):
    def __init__(self, colour, is_filled, base, height):
        super().__init__(colour, is_filled)
        self.base = base
        self.height =height

circle = Circle("red", is_filled=True, radius=5)
square = Square("blue", is_filled=False, width=3, length=3)
print(circle.colour)
print(circle.radius)
print(square.is_filled)
print(square.length)
circle.describe()


'''
Polymorphism = Greek word that means to "have many forms or faces"
               Poly = Many
               Morph = Form

               TWO WAYS TO ACHIEVE POLYMORPHISM
               1. Inheritance = An object could be treated of the same type as a parent class
               2. "Duck Typing" = object must have necessary attributes/methods
'''
from abc import ABC, abstractmethod

class Shape:

    @abstractmethod

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * pow(self.radius, 2)
class Square(Shape):
    def __init__(self, side):
        self.side =side
    def area(self):
        return pow(self.side, 2)
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)


shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("peperoni", 15)]

for shape in shapes:
    print(shape.area())
    

'''
Duck typing = Another way to achieve polymorphism besides inheritance
              Object must have the minimum neccessary attributes/methods
              "If it looks like a duck and quacks like a duck, it must be a duck"
'''

class Animal:

    alive = True

class Dog(Animal):

    def speak(self):
        print("WOOF")
class Cat(Animal):

    def speak(self):
        print("MEOW")

class Car:

    alive = False
    
    def speak(self):
        print("HONK")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
### basically duck typing in attributes from other classes into unrelated classes


'''
Static methods = A method that belongs to a class rather than any object from that class (instance)
                 Usually used for general utility functions

Insatance methods = Best for operations on instances of the class (object)
Static methods = Best for utility functions that do not need access to class data
'''

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions
    
## with static method instead of employee1 = Employee() do ...
print(Employee.is_valid_position("Cook")) 

employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

print(employee1.get_info())


'''
Class methods = Allow operations related to the class itself
                Take (cls) as the first parameter, which represents the class itself
'''

class Student:
    count = 0
    total_gpa = 0

    def __init__ (self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count +=1
        Student.total_gpa += gpa

# this is an instance methos
    def get_info(self):
        return f"{self.name}: {self.gpa}"

    @classmethod

    def get_count(cls):
        return f"Total number of students {cls.count}" 
    
    @classmethod

    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"The average class gpa is: {cls.total_gpa/cls.count:.2f}"
    
    
student1 = Student("Spongebob", 3.2)
student1 = Student("Patrick", 2.0)
student1 = Student("Sandy", 5.0)

print(Student.get_count())
print(Student.get_avg_gpa())


'''
Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
                They are automatically called by many of python's built in operations.
                They allow developers to define or customize the behaviour of objects 
'''

#class Student:

#    def __init__ (self, name, gpa):
#        self.name = name
#        self.gpa = gpa

#    def __str__ (self):
#        return f"name: {self.name} gpa: {self.gpa}"
    
#    def __eq__(self, other):
#        return self.name == other.name
    
#    def __gt__(self, other):
#        return self.gpa > other.gpa
    
#student1 = Student("Spongebob",3.2)
#student1 = Student("Patrick",2.0)

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    # To give a string __init__ will only keep output in a memory path
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    # Next is eqial dunder. other here means a second input/variable to be operated on
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    # Next is the less than dunder
    def __lt__(self, other):
        return self.num_pages<other.num_pages 
    # Next,greater than
    def __gt__(self, other):
        return self.num_pages>other.num_pages
    # Next add
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    # Next to check if something is in something (iterate)
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author 
    # To check for a key within an object
    def __getitem__(self, key):
        if key == 'title':
            return self.title
        #until i set up the other keys it will not work

book1 = Book("The Hobbit", "J.R.R Tolkein", 310)
book2 = Book("Harry Poter and the philosopher stone", "J.K Rowling", 223)
book3 = Book("The lion, the witch and the wardrobe", "C.S Lewis", 176)

print(book1)
print(book1 == book2)
print(book1<book3)
print(book1+book2)
print("lion" in book3)
print(book1['title'])


'''
@property = Decorator used to define a method as a property (It can be accessed like an attribute)
            Benefit: Add additional logic when read, write, or delete attributes
            Gives you getter, setter, and deleter method
'''

class  Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        # prefixing each attribute i want to tuen to a property with underscore '_' will make them private i.e to be used only within the class
    @property
    def width (self):
        return f"{self._width:.1f}cm"
    @property
    def height (self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width): #dont allow parametr and method be the same. very bad for code syntax and readability
        if new_width>0:
            self._width = new_width
        else:
            print("Width must be greater than zero")
    @height.setter
    def height(self, new_height): #dont allow parametr and method be the same. very bad for code syntax and readability
        if new_height>0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

rectangle = Rectangle(3,4)

rectangle.width = 5


print(rectangle.width)
print(rectangle.height)
del rectangle.width


'''
Decorator = A function that extends the behaviour of another function w/o modifying bse function
            Pass the base function as an argument to the decorator

            @add_sprinkles
            get_ice_cream('vanilla')
'''
# using the @ can call a function and make it work unless i make a decorator by using the name of the decorator and a wraper def to hold the function like below
#and decorators are called before functions to make them run the called decorator  code in conjuction to the called function 

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You add sprinkles🎊")
        func(*args, **kwargs)
    return wrapper
def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge 🍫")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream 🍨")

get_ice_cream()


'''
Exception = An event that interupts the flow of a program
            (ZeroDivisionError, TypeError, ValueError)
            1.try 2.except 3.finally
'''
try:
    num = int(input("Enter a number: "))
    print(1/num)
except ZeroDivisionError:
    print("You can't divide by zero fuu!!")
except ValueError:
    print("Enrter only numbers please: ")
except Exception:
    print("You got it all wrong? Fuck me lol") # This is used to catch all exceptions. It is efficient but in case of user input it will not help because the user doees not know what went wrong
finally:
    print("Do some cleanu here")


'''
Python file detection
'''

import os #allows python interact with my operating system
# relative file path = folder/test.txt
#absolute file path = C:/Users/BroCode/Desktop/test.txt
# I can use either relative or absolute

file_path = "BRO CODE/test.txt"
file_path2 = r"C:\Users\USER\Documents\CODE\PYTHON SHIT\BRO CODE" #use r to make python read strings literally and not look for any operators

if os.path.exists(file_path):
    print(f"The location '{file_path}' esissts")
    if os.path.isfile(file_path2):
        print("That is a file")
    elif os.path.isdir(file_path2):
        print("This is a directory")
else:
    print("That location doesn't exist")


'''
Python writing files (.txt, .json, .csv)
'''
import csv
import json

txt_data = "I like pizza"
file_path = "BRO CODE/output.txt"
# I am setting them to keyword arguments with the file and mode variales

with open(file = file_path, mode = "w") as file: # 'w' to write file if it exists and 'x' if it does not exist if it exists we will recieve an error 'a' is for append and 'r' is for read
    file.write(txt_data)
    print(f"Text file {file_path} was created")
    # w will overwrite a file
#first append
with open(file = file_path, mode = "a") as file:
    file.write(" " + txt_data)
    print(f"Text file {file_path} was appended")
#second append
with open(file = file_path, mode = "a") as file:
    file.write("\n" + txt_data + "\n")
    print(f"Text file {file_path} was appended")

try:
    with open(file = file_path, mode = "x") as file:
        file.write(txt_data)
        print(f"Text file {file_path} was created")
except FileExistsError:
    print("That file already exists")

employees = ["SPongebob", "Eugeine", "Squidward", "Patrick"]

try:
    with open(file = file_path, mode = "a") as file:
        for employee in employees:
            file.write(employee + " ")
        print(f"Text file {file_path} added to")
except FileExistsError:
    print("That file already exists")

# a json file is filled with key:value pairs

dic_employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}
new_file_path = "BRO CODE/json.json" # i need to import json module if i want to use it
try:
    with open(file = new_file_path, mode = "w") as file:
        json.dump(dic_employee, file, indent=4)
        print(f"json file '{new_file_path}' was created")
except FileExistsError:
    print("That file already exists")
# need to import csv module csv file is used to store stuff like excel sheets
datastruct_employees = [["Name", "Age", "Job"],
                        ["Spongebob", 30, "Cook"],
                        ["Squidward", 45, "Cashier"],
                        ["Patrick", 27, "Janitor"]
                        ]
csv_file_path = "BRO CODE/csv.csv" 
#                                                        newline =   # is used to remove new lines from the file when writing
try:
    with open(file = csv_file_path, mode = "w", newline="") as file: 
        writer = csv.writer(file) # writer is an object
        for row in datastruct_employees:
            writer.writerow(row)
        print(f"csv {csv_file_path} added to")
except FileExistsError:
    print("That file already exists")

# if i do not iterate over all the rows it will not give outputa


'''
Reading files
'''
import json
import csv

file_path = "BRO CODE/test.txt"
file_path_json = "BRO CODE/json.json"
file_path_csv = "BRO CODE/csv.csv"

# with wrapps code within a context manager
try:
    with open(file= file_path, mode= 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permision to read that file")

try:
    with open(file= file_path_json, mode= 'r') as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permision to read that file")
# I can access data by calling the key for json files
try:
    with open(file= file_path_json, mode= 'r') as file:
        content = json.load(file)
        print(content["name"])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permision to read that file")

try:
    with open(file= file_path_csv, mode= 'r') as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permision to read that file")
# I can specify what column to print using the key:value access '[]'
try:
    with open(file= file_path_csv, mode= 'r') as file:
        content = csv.reader(file)
        for line in content:
            print(line[2])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permision to read that file")


'''
Date & Time
'''

import datetime

date = datetime.date(2025, 1, 21)
today = datetime.date.today()
time = datetime.time(12,30,0)
time_now = datetime.datetime.now()

time_now = time_now.strftime("%H:%M:%S %m-%d-%Y")

print(time_now)
print(date)
print(today)
print(time)

target_date_time = datetime.datetime(2020, 1, 2, 12, 30, 1)
current_date_time = datetime.datetime.now()

if target_date_time < current_date_time:
    print("Target date has passed")
else:
    print("Target date has not passed")


import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = r"C:\Users\USER\Documents\CODE\PYTHON SHIT\BRO CODE\HANTA VIRUS 150BPM (@splendidecko + @loot).mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(current_time)
        
        if current_time == alarm_time:
            print("Wake up!!!")
            pygame.mixer.init() # mixer is used to load and play sound files. init is the constructor
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
                
            is_running = False

        time.sleep(1)

if __name__ == '__main__':
    alarm_time = input("Enter the alarm time [Hrs: Mins: Sec]: ")
    set_alarm(alarm_time)


'''
multithreading = used to perform multiple tasks cuncurrently (multitasking)
                 Good for I/O bound tasks like reading files or fetching data from APIs
                 threading.Thread(target=my_fucntion)
'''
import threading
import time

def walk_dog(first):
    time.sleep(8)
    print("Walking the {first}...")  # Simulate time taken to walk the dog

def take_out_trash():
    time.sleep(2)
    print("Taking out the trash...")
def get_mail():
    time.sleep(5)
    print("Getting the mail...")

chore1 = threading.Thread(target=walk_dog, args=("first",))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target = get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are being done concurrently!")
#walk_dog()
#take_out_trash()
#get_mail()

    
'''
How to connect to API
'''

import requests

base_url = "https://pokeapi.co/api/v2"
#https://pokeapi.co/api/v2/pokemon/pikachu
def get_pokemon(pokemon_name):
    url = f"{base_url}/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Error: {response.status_code} - {response.reason}")
pokemon_name = input("Enter the name of the Pokemon: ")
pokemon_info = get_pokemon(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"ID: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")


'''
PyQt5 introduction
'''

import sys #mesning system module. it provides access to some variables used or maintained by the interpreter and to functions that stongly interact with the interpreter. it is always available
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import (Qt, QSize) #used for allignments

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Introduction")
        self.setGeometry(600, 300, 640, 480) #this has 4 args x, y, width, height. x and y are the coordinates of the top left corner of the window, and width and height are the dimensions of the window. The default values are 0, 0, 640, 480.
        self.setWindowIcon(QIcon(r"C:\Users\USER\Documents\CODE\PYTHON SHIT\BRO CODE\b1682d1c-7ef4-4805-9464-f0031e42157f.JPG"))
        self.setStyleSheet("background-color: pink;")
        self.initUI()

        label = QLabel("Hello, PyQt5!", self)
        label.setFont(QFont("Gothic", 30))
        label.setWordWrap(True)
        label.setGeometry(0, 0, 640, 70)
        #label.setGeometry(0, 0, 200, 200) #this has 4 args x, y, width, height. x and y are the coordinates of the top left corner of the label, and width and height are the dimensions of the label. The default values are 0, 0, 640, 480.
        label.setStyleSheet("color: red;"
                            "background-color: grey;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")  #you can use rgb values, hex values, or color names. you can also use rgba values, which allow you to set the opacity of the color. The default value is 1, which means fully opaque. The value can be between 0 and 1, where 0 is fully transparent and 1 is fully opaque.
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #Will align text vertically to the top use top, bottom, vcentre, hcentre, right, left,

        labelpic = QLabel(self)
        labelpic.setGeometry(0,70, 200, 200)

        pixmap = QPixmap(r"C:\Users\USER\Documents\CODE\PYTHON SHIT\BRO CODE\b1682d1c-7ef4-4805-9464-f0031e42157f.JPG")
        labelpic.setPixmap(pixmap) #image will set but willnot scale 
        labelpic.setScaledContents(True)

        labelpic.setGeometry((self.width()-labelpic.width()) // 2, #// is for integer divison (whole numbers) divide by two to centre any image
                              (self.height()-labelpic.height()) // 2,
                              labelpic.width(), 
                              labelpic.height()) #use label.width or label.height to set the already set size of hatever you are setting
          


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    pass

if __name__ == '__main__':
    main()


'''
PyQt5 introduction (layouts)
'''
import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QGridLayout, QHBoxLayout, QVBoxLayout, QToolBar, QWidget)
from PyQt5.QtGui import (QPixmap, QIcon, QFont)
from PyQt5.QtCore import (Qt, QSize)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("Layouts Tutorial")
        self.setGeometry(600, 300, 640, 600)
        self.setWindowIcon(QIcon (r"C:\Users\USER\Documents\CODE\PYTHON SHIT\BRO CODE\b1682d1c-7ef4-4805-9464-f0031e42157f.JPG") )
        self.setStyleSheet("background-color: pink;" )

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color: red; ")
        label2.setStyleSheet("background-color: orange; ")
        label3.setStyleSheet("background-color: yellow; ")
        label4.setStyleSheet("background-color: green; ")
        label5.setStyleSheet("background-color: blue; ") 

        #creating vertical layout manager
        ''' 
        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)

        central_widget.setLayout(vbox)
        '''
        #creating a grid layout. For grid layouts I have to call the row and column they fall into
        grid = QGridLayout()

        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 0, 2)
        grid.addWidget(label4, 1, 0)
        grid.addWidget(label5, 1, 2)

        central_widget.setLayout(grid)
    

    

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


'''
PyQt5 push buttons
'''

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QLabel, QToolBar, QGridLayout, 
                             QVBoxLayout, QHBoxLayout, QBoxLayout, QPushButton)
from PyQt5.QtGui import (QIcon, QFont, QPixmap)
from PyQt5.QtCore import (Qt, QSize)

class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.setWindowIcon (QIcon (r"C:\Users\USER\Documents\CODE\PYTHON SHIT\BRO CODE\b1682d1c-7ef4-4805-9464-f0031e42157f.JPG"))
        self.setWindowTitle("Push Buttons")
        self.setGeometry(400, 400, 600, 600)
        self.setIconSize(QSize(1000,1000))
        self.setStyleSheet("background-color: pink; "
                           )

        self.label_goodbye = QLabel("HELLO!", self)
        self.label_goodbye.setGeometry(0, 0, 200, 100)
        self.label_goodbye.setStyleSheet("background-color: red; "
                           )


    def initUi(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.button1 = QPushButton("Botton 1", self)
        self.button2 = QPushButton("Botton 2", self)
        #button1.setGeometry(50, 50, 100, 50)
        self.button1.setGeometry(0, 200, 200, 100)
        self.button1.setStyleSheet("font-size: 20px; ")
        self.button1.clicked.connect(self.on_button1_click)
        self.button2.setGeometry(150, 200, 200, 100)
        self.button2.setStyleSheet("font-size: 20px; ")
        self.button2.clicked.connect(self.on_button2_click)
        

    def on_button1_click(self):
        print("Button 1 clicked")
        self.button1.setText("CLicked!!")
        self.button1.setDisabled(True)
        self.label_goodbye.setText("GOODBYE!")

    def on_button2_click(self):
        print("Button 2 clicked")
        self.button2.setText("CLicked!!")
        self.button2.setDisabled(True)
        self.label_goodbye.setText("HELLO AGAIN!")

## Always prefix your buttons with self. if you want to access them in other functions. Otherwise, they will be local variables and won't be accessible outside the function they are defined in.
        

def main():
    App = QApplication(sys.argv)
    App_Window = MainWindow()
    App_Window.show()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()


'''
PyQt checkboxes
'''

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QLabel, QLayout, QPushButton, QCheckBox, QBoxLayout, QHBoxLayout, 
                             QVBoxLayout, QGridLayout)
from PyQt5.QtGui import (QFont, QPixmap, QIcon)
from PyQt5.QtCore import (Qt, QSize)

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CHECKBOXES")
        self.setWindowIcon(QIcon (r"C:\Users\USER\Documents\CODE\PYTHON SHIT\BRO CODE\b1682d1c-7ef4-4805-9464-f0031e42157f.JPG"))
        self.setGeometry(1000, 200, 600, 600)
        self.setStyleSheet("background-color: grey; "
                           )
        
        self.checkbox1 = QCheckBox("Do you like pizza", self)
        self.label_message = QLabel("pp", self)
        self.label_message.setGeometry(10, 100, 500, 100)

        self.initUI()

    def initUI(self):
        self.checkbox1.setGeometry(10, 0, 500, 100)
        self.checkbox1.setStyleSheet("font-size: 30px; "
                                     "font-family: Ariel; "
                                     "background-color: pink; "
                                     )
        self.checkbox1.setChecked(False)
        self.label_message.setStyleSheet("background-color: blue; "
                                         )
        self.checkbox1.stateChanged.connect(self.checkbox_changed)

        pass

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("I'll get you some pizza")
            self.label_message.setText("Have some pizza")
        else:
            print("What would you like?")
            self.label_message.setText("So, you're not just hungry?")

def main():
    App = QApplication(sys.argv)
    Window = Main_Window()
    Window.show()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()


'''
PyQt Radio Buttons
'''

import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QLayout, QPushButton, QLabel, QApplication, QRadioButton, QButtonGroup,
                             QBoxLayout, QVBoxLayout, QHBoxLayout, QGridLayout)
from PyQt5.QtGui import (QPixmap, QIcon, QFont)
from PyQt5.QtCore import (Qt, QSize)

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon (r"C:\Users\USER\Documents\CODE\PYTHON SHIT\BRO CODE\b1682d1c-7ef4-4805-9464-f0031e42157f.JPG"))
        self.setWindowTitle ("RADIO BUTTONS")
        self.setGeometry(1000, 200, 600, 600)
        self.setStyleSheet("background-color: grey; "
                           )

        #creatign radiobuttons
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("MasterCard", self)
        self.radio3 = QRadioButton("Verve", self)

        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)

        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)

        self.initUI()
        pass
    def initUI(self):
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)

        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        self.setStyleSheet("QRadioButton{"\
                           "font-size: 40px; "
                           "font-family: Times New Roman; "
                           "padding: 10px; "
                           "}")

        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)

        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)
        pass
    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")
        #print("selection made!!!")
        pass

def main():
    App = QApplication(sys.argv)
    Window = Main_Window()
    Window.show()
    sys.exit(App.exec_())
if __name__ == "__main__":
    main()


    