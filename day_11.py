#Exercise day 11

#Q:1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_num(num1,num2):
    return num1+num2 
print(add_two_num(3,5))

#Q:2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    π=3.14
    area=π*r*r
    return area
print(area_of_circle(10))

#Q:3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    total=0
    for num in args:
        if not isinstance(num,(int,float)):
            return "Error:All arguments must be numbers"
        total += num
    return total
print(add_all_nums(2,3,6))
print(add_all_nums(2, 3, "hello"))

#Q:4 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
#  Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(C):
    fahrenheit =C *9/5 + 32
    return fahrenheit
print(convert_celsius_to_fahrenheit(300))

#Q:5 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month=month.lower()
    if month in ["december", "january", "february"]:
        return "Winter"
    elif month in ["march", "april", "may"]:
        return "Spring"
    
    elif month in ["june", "july", "august"]:
        return "Summer"
    
    elif month in ["september", "october", "november"]:
        return "Autumn"
    
    else:
        return "Invalid month name"

print(check_season("March"))
print(check_season("July"))
print(check_season("abc"))

#Q:6 Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1,y1,x2,y2):
    if x2-x1 ==0:
        return "Slope is undefined"
    slope =(y2-y1)/(x2-x1)
    return slope
print(calculate_slope(1,2,3,5))

#Q:7 Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
import math
def sol_of_quad_eq(a,b,c):
    eq=(b**2)-(4*a*c)
    if eq<0:
        return "No real solution"
    x1=(-b+math.sqrt(eq))/(2*a)
    x2=(-b-math.sqrt(eq))/(2*a)
    return x1,x2
print(sol_of_quad_eq(1,2,1))

#Q:8 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(my_list):
    for item in my_list:
        print(item)
print_list(([1,2,5,"apple"]))

#Q:9 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(array):
    reversed_array=[]

    for i in range(len(array)-1,-1,-1):
        reversed_array.append(array[i])
    return reversed_array

print(reverse_list([1, 2, 3, 4, 5]))
    
#Q:10 Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items.
def capitalize_list_items(my_list):
    capitalize_list=[]
    for item in my_list:
        capitalize_list.append(item.capitalize())
    return capitalize_list
print(capitalize_list_items(["apple","orange","kiwi"]))

#Q:11 Declare a function named add_item. It takes a list and an item parameters.
#  It returns a list with the item added at the end.
def add_item(my_list,item):
    my_list.append(item)
    return my_list

fruits = ["apple", "orange", "kiwi"]
print(add_item(fruits, "banana"))

#Q:12 Declare a function named remove_item. It takes a list and an item parameters.
#  It returns a list with the item removed from it.
def remove_item(my_list,item):
    my_list.remove(item)
    return(my_list)
fruits = ["apple", "orange", "kiwi"]
print(remove_item(fruits, "kiwi"))

#Q:13 Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(n):
    total=0
    for i in range(1,n+1):
        total +=i
    return total 
print(sum_of_numbers(10))

#Q:14 Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    total=0
    for i in range(1,n+1):
            if i%2 !=0:
             total +=i
    return total
print(sum_of_odds(51))

#Q:15 Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.
def sum_of_even(n):
    total=0
    for i in range(0,n+1):
            if i%2 ==0:
                total +=i
    return total
print(sum_of_even(63))

#Q:16 Declare a function named evens_and_odds .
#  It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(n):
    even_count=0
    odd_count=0
    for digit in str(n):
        if int(digit)%2==0:
            even_count +=1
        else:
            odd_count +=1
    return even_count,odd_count
print(evens_and_odds(123456))

#Q:17 Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    if n<0:
        return "Factorial is not valid for negative numbers"
    result=1
    for i in range(1,n+1):
        result *=i
    return result
print(factorial(5))

#Q:18 Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(value):
    if not value:
        return True
    else:
        return False
    
print(is_empty(""))       
print(is_empty([1,2,3]))

#Q:19 Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
def show_args(**args):
    for key, value in args.items():
        print(key,"=",value)

show_args(name="Arwa", age=17, country="Pakistan")


#Q:20 Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n<=1:
        return False
    for i in range (2,n):
        if n %i ==0:
            return False 
    return True
print(is_prime(7))
print(is_prime(10))


#Q:21 Write a functions which checks if all items are unique in the list.
def all_unique(items):
    for item in items:
        if items.count(item)>1:
            return False
        return True

print(all_unique([1, 2, 3, 4]))
print(all_unique([1, 2, 2, 4]))

#Q:22 Write a function which checks if all the items of the list are of the same data type.
def same_type(items):
    first_type=type(items[0])

    for item in items:
        if type(item) != first_type:
            return False
        return True
print(same_type([1, 2, 3]))
print(same_type([1, "2", 3]))

#Q:23 Write a function which check if provided variable is a valid python variable
import keyword
def is_valid_variable(name):
    if name.isidentifier() and not keyword.iskeyword(name):
        return True
    return False

print(is_valid_variable("my_var"))
print(is_valid_variable("2name"))


