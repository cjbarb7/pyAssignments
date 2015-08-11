#------------------#
# Python Variables #
#------------------#

# There are five 'data types' in Python. 'Data types' are ways of representing information. For instance, if you were describing a person, two pieces of data about a person might be their name and their age. The data type of their name would be a 'string', which is basically a word. The data type of their age would be a number. 


# 1. String assignment

name = "Bruce"

# You can combine strings with variables like this:
# Notice the difference between "name" and name inside the parentheses.
# Also notice how I have a space after the word 'is'. You gotta remember spaces!
print ("My name is " + name)

# You can put variables in the middle too!
print ("My name is " + name + " Wayne")

# Your turn! Fill in the blank
name = _____




# 2. Number assignment

# Fill in the blank with an integer (a whole number)
age = ___

# Putting it together
print(name + " is " + age + " years old ") 

# You can do math with variables too!
print("My grandfather is " + age * 3 + " years old")



# 3. Multiple Assignment

# You can have several variables equal the same thing.
height, weight, age = 20
print("I am " + age + " years old. I am " + height * 3 + " inches tall and " + weight * 5 + " pounds.") 

# You can also combine multiple variables onto one line, even if they're different kinds of data types

# This example:
event = "birthday"
date = 23

# is the same thing as: 
event, date = birthday, 23

print("My " + event + " is on September " + date)



# 4. Your turn!

# You decide the score! Put in a number for the Houston Rockets.
# Put in a variable name (like a sports team) in the second blank 
houston_rockets = ___
_______________ = 20


rockets_win = False;
if(houston_rockets > ________): 
	rockets_win = True

if(rockets_win):
	print("Whooo! Rockets win!")
else:
	print("The Houston Rockets lose!")



