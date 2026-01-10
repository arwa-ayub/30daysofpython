#day_02: 30 days oof python programming

#Exercises: Level 1

#Q1:Declare a first name variable and assign a value to it
first_name="Arwa"

#Q2:Declare a last name variable and assign a value to it
last_name="Ayub"

#Q3:Declare a full name variable and assign a value to it
full_name="Arwa Ayub"

#Q4:Declare a country variable and assign a value to it
country="Pakistan"

#Q5:Declare a city variable and assign a value to it
city="Muzaffarabad"

#Q6:Declare an age variable and assign a value to it
age=17

#Q7:Declare a year variable and assign a value to it
year=2007

#Q8:Declare a variable is_married and assign a value to it
is_married=False

#Q9:Declare a variable is_true and assign a value to it
is_true=True

#Q10:Declare a variable is_light_on and assign a value to it
is_light_on="yes"

#Q11:Declare multiple variable on one line
name, age, country = "Arwa", 18, "Pakistan"

#Exercises: Level 2

#Q1:Check the data type of all your variables using type() built-in function

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#Q2:Using the len() built-in function, find the length of your first name
print(len(first_name))

#Q3:Compare the length of your first name and your last name
if len(first_name) > len(last_name):
    print("First name is longer than last name")
elif len(first_name) < len(last_name):
    print("first name is shorter than last name")
else:
    print("first name and last name have equal length")     

#Q4:Declare 5 as num_one and 4 as num_two
num_one=5
num_two=4

#Q5:Add num_one and num_two and assign the value to a variable total
total= num_one+num_two
print(total)

#Q6:Subtract num_two from num_one and assign the value to a variable diff
diff=num_one - num_two
print(diff)

#Q7:Multiply num_two and num_one and assign the value to a variable product
product=4*5
print(product)

#Q8:Divide num_one by num_two and assign the value to a variable division
division= num_one/num_two
print(division)

#Q9:Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder= num_one%num_two
print(remainder)

#Q10:Calculate num_one to the power of num_two and assign the value to a variable exp
variable_exp=num_one**num_two
print(variable_exp)

#Q11:Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division= num_one//num_two
print(floor_division)

#Q12:The radius of a circle is 30 meters.
"""
i.Calculate the area of a circle and assign the value to a variable name of area_of_circle
ii.Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
iii.Take radius as user input and calculate the area."""

import math
radius=30
#i&ii
area_of_circle=math.pi*radius**2
circum_of_circle=2*math.pi*radius
#iii
radius=float(input("enter the radius"))
area_of_circle_input=math.pi*radius**2

print(area_of_circle)
print(circum_of_circle)
print(area_of_circle_input)

#Q13:Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name=input("enter your first name:")
last_name=input("enter your last name:")
country=input("enter your country:")
age=int(input("enter your age"))

print("First name:", first_name)
print("Last name:", last_name)
print("Country:",country)
print("Age:",age)


#Q14:Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help("keywords")