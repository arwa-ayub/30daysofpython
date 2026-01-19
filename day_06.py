#Exercise day 06

#Q:1 Create an empty tuple
empty_tuple=()

#Q:2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters=("aqsa","maryum")
brother=("ahmed")

#Q:3 Join brothers and sisters tuples and assign it to siblings
siblings=(sisters)+(brother,)
print(siblings)

#Q:4 How many siblings do you have?
total_siblings=len(siblings)
print("Siblings:",total_siblings)

#Q:5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
modify=list(siblings)
modify.insert(0,"M.Ayub")
modify.insert(1,"Maria")
print(modify)
family_members=tuple(modify)
print("family members:",modify)

#Q:6 Unpack siblings and parents from family_members
family_members=['M.Ayub', 'Maria', 'aqsa', 'maryum', 'ahmed']
father,mother,*siblings=family_members
print("father:",father)
print("mother:",mother)
print("siblings:",siblings)

#Q:7 Create fruits, vegetables and animal products tuples.Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=("apple","kiwi")
vegtables=("cabbage","potato")
animal_product=("cat food","dog food")

food_stuff_tp=fruits+vegtables+animal_product
print(food_stuff_tp)

#Q:8 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_it=list(food_stuff_tp)
print(food_stuff_it)

#Q:9 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_it=('apple', 'kiwi', 'cabbage', 'potato', 'cat food', 'dog food')
n=len(food_stuff_it)
if n % 2 == 0:
  middle_item= food_stuff_it[n//2 - 1 : n//2 + 1]

else: 
    middle_item=food_stuff_it //2

print(middle_item)  

#Q:10 Slice out the first three items and the last three items from food_stuff_lt list
food_stuff_it=('apple', 'kiwi', 'cabbage', 'potato', 'cat food', 'dog food')
first_three_items=food_stuff_it[0:3]
print(first_three_items)
last_three_items=food_stuff_it[-3:]
print(last_three_items)

#Q:11 Delete the food_stuff_tp tuple completely
del food_stuff_it

#Q:12 Check if an item exists in tuple:
"""Check if 'Estonia' is a nordic country

Check if 'Iceland' is a nordic country"""

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)


