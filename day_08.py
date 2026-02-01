#Exercise day 08

#Q:1 Create an empty dictionary called dog
dog=dict()

#Q:2 Add name, color, breed, legs, age to the dog dictionary
dog={
"Name:Tom",
"Color:White",
"Breed:German",
"Legs:4",
"Age:5"}
print(dog)

#Q:3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student_dict={"first_name":"Arwa","last_name":"Ayub","Gender":"Female","Age":"17","marital status": "Unmarried","Skills": ["Python","SQl"],
"Country":"Pakistan","City":"MZD"}
print(student_dict)

#Q:4 Get the length of the student dictionary
print(len(student_dict))

#Q:5 Get the value of skills and check the data type, it should be a list
skills=student_dict["Skills"]
print(skills)
print(type(skills))

#Q:6 Modify the skills values by adding one or two skills
student_dict["Skills"].append("HTML")
print(student_dict["Skills"])

#Q:7 Get the dictionary keys as a list
keys_list=list(student_dict.keys())
print(keys_list)

#Q:8 Get the dictionary values as a list
val_list=list(student_dict.values())
print(val_list)

#Q:9 Change the dictionary to a list of tuples using items() method
print(student_dict.items())

#Q:10 Delete one of the items in the dictionary
student_dict.pop("Country")
print(student_dict)

#Q:11 Delete one of the dictionaries
del student_dict