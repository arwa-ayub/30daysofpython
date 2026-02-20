#Exercise day 10

#Q:1 Iterate 0 to 10 using for loop, do the same using while loop.
numbers=[0,1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(number)

numbers=0
while numbers <= 10:
    print(numbers) 
    numbers += 1

#Q:2 Iterate 10 to 0 using for loop, do the same using while loop.
numbers=[10,9,8,7,6,5,4,3,2,1,0]
for number in numbers:
    print(number)

numbers=10
while numbers<=0:
    print(numbers)
    numbers -=1

#Q:3 Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######

i=1
while i<=7:
    print("#"*i)
    i +=1

#Q:4 Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for i in range(8):
    for j in range(8):
        print("# ", end="")
    print()

#Q:5 Print the following pattern:
"""
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100"""

for i in range (11):
    print(i,"x ",i, "=",i*i)

#Q:6 Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

libs= ['Python', 'Numpy','Pandas','Django', 'Flask']
for libraray in libs:
    print(libraray)

#Q:7 Use for loop to iterate from 0 to 100 and print only even numbers

for i in range (0,101,2):
    print(i)

#Q:8 Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(1,101,2):
    print(i)

#Q:9 Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum_even=0
sum_odd=0

for i in range(101):
    if i % 2 == 0:    
        sum_even += i
    else:             
        sum_odd += i

print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)

#Q:10 This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits=['banana', 'orange', 'mango', 'lemon']
for fruit in reversed(fruits):
    print(fruit)
