#Exercise day 03

#Q:1 Declare your age as integer variable
age=17

#Q:2 Declare your height as a float variable
height=5.11

#Q:3 Declare a variable that store a complex number
z=3+4j

#Q:4 Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base=float(input("enter the base:"))
height=float(input("enter the height:"))

area=0.5*base*height
print("The area of triangle is:",area)

#Q:5 Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a=float(input("enter side a:"))
side_b=float(input("enter side b:"))
side_c=float(input("enter side c:"))

perimeter= side_a+side_b+side_c
print("the perimeter of triangle is:",perimeter)

#Q:6 Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length=float(input("enter the length:"))
width=float(input("enter the width:"))

area_of_rectangle=length*width
perimeter_of_rectangle=(length+width)*2

print("area of rectangle is:",area_of_rectangle)
print("perimeter of rectangle is:",perimeter_of_rectangle)

#Q:7 Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius=float(input("enter the radius:"))
pi=3.14

area_of_circle=pi*radius*radius
circumference=2*pi*radius

print("Area of circle is:",area_of_circle)
print("Circumference of circle is",circumference)

#Q:8 Calculate the slope, x-intercept and y-intercept of y = 2x -2

#given equation : y=2x-2
m=2 #slope
c=-2
y_intercept=c
x_intercept=-c/m

print("Slope:",m)
print("x-intercept:",x_intercept)
print("y-intercept:",y_intercept)

#Q:9 Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math
x1=2
y1=2
x2=6
y2=10

m=float(y2-y1)/(x2-x1)
euclidean_distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("slope =",m)
print("euclidean distance=",euclidean_distance)

#Q:10 Compare the slopes in tasks 8 and 9.
slope9=2
slope8=2

if slope9 == slope8:
    print("slopes are equal")
else:
    print("slopes are not equal")   

#Q:11 Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
for x in range(-10,11): 
    y=x**2+6*x+9
print(f"x={x},y={y}")

if y==0:
        print(f"\n y is 0 when x={x}")

#Q:12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len("python"))
print(len("dragon"))

print(len("python")>len("dragon"))

#Q:13 Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "python"and "on" in "dragon")

#Q:14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence="I hope this course is not full of jargon"
print("jargon" in sentence)

#Q:15 There is no 'on' in both dragon and python
print(not("on" in "python" and "on" in "dragon"))

#Q:16 Find the length of the text python and convert the value to float and convert it to string
print(len("python"))
print(float(len("python")))
print(str(len("python")))

#Q:17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number=100
if number%2 == 0:
    print("number is even")
else :
    print("number is not even")

#Q:18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_div=7//3
int_value=int(2.7)
result=(floor_div == int_value)
print(result)

#Q:19 Check if type of '10' is equal to type of 10
type("10")
type(10)
print(type("10") == type(10))

#Q:20 Check if int('9.8') is equal to 10
result=int(float("9.8"))==10
print(result)

#Q:21 Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours=float(input("enter hours:"))
rate_per_hour=float(input("enter rate per hour:"))
pay=hours*rate_per_hour
print("pay:",pay)

#Q:22 Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live.
years=float(input("enter number of years:"))
seconds=years*365*24*60*60
print("you have lived",seconds,"seconds")


#Q:23 Write a Python script that displays the following table
"""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125  """

print("n 1 n n**2 n**3")
for n in range(1,6):
    print(n, 1, n, n**2, n**3) 

     
