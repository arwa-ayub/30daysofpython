#Exercise day 09

#Q:1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age=int(input("Enter your age:"))
if age >= 18:
    print("You are old enough to drive")
else:
    print("You need 3 more years to learn to drive ")   

#Q:2 Compare the values of my_age and your_age using if … else.
#  Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
#  You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences,
#  and a custom text if my_age = your_age. Output:

my_age=18
your_age=int(input("Enter your age:"))
if my_age>your_age:
    difference=my_age-your_age  
    if difference==1:
       print(f"I am{difference} year older than you")
    else:
        print(f"I am {difference} years older than you")
elif my_age<your_age:
    difference=your_age-my_age
    if difference == 1:
        print(f"You are {difference} year older than me.")
    else:
        print(f"You are {difference} years older than me.")
else:
     my_age == your_age
     print("We are same age")

#Q:3 Get two numbers from the user using input prompt.
#  If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.     
a=int(input("enter a number:"))
b=int(input("enter a number:"))
if a>b:
    print("a is greator than b")
elif a<b:
    print("a is smaller than b")
else:
    print("a is equal to b")     
    
#Q:4 Write a code which gives grade to students according to theirs scores:

"""90-100, A
80-89, B
70-79, C
60-69, D
0-59,  F"""

Grade=int(input("Enter your scores:"))
if 90<=Grade>=100:
    print("Grade:A")
elif 80<=Grade>=89:
    print("Grade:B")
elif 70<=Grade>=79:
    print("Grade:C")
elif 60 <= Grade <= 69:
    print("Grade: D")
elif 0 <= Grade <= 59:
    print("Grade: F")
else:
    print("Invalid score")  

#Q:5 Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. December, January or February,
# the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer. 
month=input("Enter the month:").capitalize()
if month in ("September", "October", "November"):
    print("The season is Autum")
elif month in ("December", "January", "February"):
    print("The season is Winter")
elif month in ("March", "April", "May"):
    print("The season is Spring")
elif month in ("June", "July", "August"):
    print("The season is Summer")
else:
    print("Invalid month")

#Q:6 The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
#If the fruit exists print('That fruit already exist in the list')
new_fruit=input("enter the fruit:").lower()
if new_fruit not in fruits:
    fruits.append(new_fruit)
    print("Fruit Added")
else:
    print("Fruit already exist")

print("Updated list:", fruits)

#Q:7 Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
#Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#If a person skills has only JavaScript and React, print('He is a front end developer'), 
#if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
#if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
#else print('unknown title') - for more accurate results more conditions can be nested!

#Check if skills key exists and print middle skill
if "skills" in person:
    skills=person["skills"]
    middle_index=len(skills)//2
    print("Middle skill:", skills[middle_index])

#Check if Python is in skills
if 'skills' in person:
    if 'Python' in person['skills']:
        print("He has Python skill.")
    else:
        print("He does not have Python skill.")

#Determine job title    

skills = person['skills']

if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
    print("He is a front end developer")

elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print("He is a backend developer")

elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print("He is a fullstack developer")

else:
    print("Unknown title")    