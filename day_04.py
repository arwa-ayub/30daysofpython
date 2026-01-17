#Exercise day 04

#Q:1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
result="Thirty"+" "+"Days" + "  "+"Of"+" "+"Python"
print(result)

#Q:2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
result="Coding"+" "+"For"+" "+"All"
print(result)

#Q:3 Declare a variable named company and assign it to an initial value "Coding For All".
company="Coding For All"

#Q:4 Print the variable company using print().
print(company)

#Q:5 Print the length of the company string using len() method and print().
print(len(company))

#Q:6 Change all the characters to uppercase letters using upper() method.
print(company.upper())

#Q:7 Change all the characters to lowercase letters using lower() method.
print(company.lower())

#Q:8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Q:9 Cut(slice) out the first word of Coding For All string.
text="Coding For All"
first_word=text[:6]
print(first_word)

#Q:10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find("Coding"))
print("Coding" in company)
print(company.index("Coding"))

#Q:11 Replace the word coding in the string 'Coding For All' to Python.
company="Coding For All"
print(company.replace("Coding","Python"))

#Q:12 Change "Python for All" to "Python for Everyone" using the replace method or other methods.
company="Python For All"
print(company.replace("All","Everyone"))

#Q:13 Split the string 'Coding For All' using space as the separator (split()) .
company="Coding For All"
print(company.split())

#Q:14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
text='Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(text.split(","))

#Q:15 What is the character at index 0 in the string Coding For All.
company="Coding For All"
print(company[0])

#Q:16 What is the last index of the string Coding For All.
company="Coding For All"
print(len(company)-1)

#Q:17 What character is at index 10 in "Coding For All" string.
company="Coding For All"
print(company[10])

#Q:18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
text="Python For Everyone"
words=text.split()
acronym=""
for word in words:
  acronym=acronym + word[0]
acronym=acronym.upper()
print(acronym)

#Q:19 Create an acronym or an abbreviation for the name 'Coding For All'.
text="Coding For All"
worsd=text.split()
acronym=""
for word in words:
  acronym=acronym + word[0]
acronym=acronym.upper() 
print(acronym)

#Q:20 Use index to determine the position of the first occurrence of C in Coding For All.
company="Coding For All"
print(company.index("C"))

#Q:21 Use index to determine the position of the first occurrence of F in Coding For All.
company="Coding For All"
print(company.index("F"))

#Q:22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
company="Coding For All"
print(company.rfind("l"))

#Q:23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
text='You cannot end a sentence with because because because is a conjunction'
print(text.find("because"))
print(text.index("because"))

#Q:24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
text='You cannot end a sentence with because because because is a conjunction'
print(text.rindex("because"))

#Q:25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
text='You cannot end a sentence with because because because is a conjunction'
result=text[31:54]
print(result)

text='You cannot end a sentence with because because because is a conjunction'
start=text.find("because because because")
end=start+len("because because because")
phrase=text[start:end]
print(phrase)

#Q:26 Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
text='You cannot end a sentence with because because because is a conjunction'
print(text.find("because"))

#Q:27 Does 'Coding For All' start with a substring Coding?
text="Coding For All"
print(text.startswith("Coding"))

#Q:28 Does 'Coding For All' end with a substring coding?
text="Coding For All"
print(text.endswith("Coding"))

#Q:29 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
text='   Coding For All      '
print(text.strip(''))

#Q:30 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ('Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon')
result="#".join(libraries)

#Q:31 Use the new line escape sequence to separate the following sentences.
"""I am enjoying this challenge.
I just wonder what is next."""
print("I am enjoying this challenge.\nI just wonder what is next.")

#Q:32 Use a tab escape sequence to write the following lines.
"""Name      Age     Country   City
Asabeneh  250     Finland   Helsinki"""
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

#Q:33 Use the string formatting method to display the following:
"""radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square."""
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {:.2f}.".format(radius,area))

#Q:34 Make the following using string formatting methods:
"""8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144"""
a=8
b=6
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
