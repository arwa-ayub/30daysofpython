#Exercise day 05

#Q:1 Declare an empty list
my_list=[]

#Q:2 Declare a list with more than 5 items
fruits=["apple","mango","kiwi","banana","orange"]

#Q:3 Find the length of your list
print(len(fruits))

#Q:4 Get the first item, the middle item and the last item of the list
fruits=["apple","mango","kiwi","banana","orange"]
first_item=fruits[0]
middle_index=len(fruits)// 2
middle_item=fruits[middle_index]
last_item=fruits[-1]

print("First item:",first_item)
print("Middle item:", middle_item)
print("Last item:" ,last_item)

#Q:5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=["arwa", "17", "5'11", "single"," Pakistan"]

#Q:6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=["Facebook", "Google", "Microsoft"," Apple","IBM", "Oracle", "Amazon"]

#Q:7 Print the list using print()
print(it_companies)

#Q:8 Print the number of companies in the list
print(len(it_companies))

#Q:9 Print the first, middle and last company
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
first=it_companies[0]
print("First company:",first)

middle=len(it_companies) // 2
middle_index=it_companies[middle]
print("Middle company:",middle_index)

Last=it_companies[-1]
print("Last company:",Last)

#Q:10 Print the list after modifying one of the companies
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies[0]="Meta"
print(it_companies)

#Q:11 Add an IT company to it_companies
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.append("Emporion.soft")
print(it_companies)

#Q:12 Insert an IT company in the middle of the companies list
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.insert(len(it_companies)//2 ,"Codev") 
print(it_companies)

#Q:13 Change one of the it_companies names to uppercase (IBM excluded!)
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies[3]=it_companies[3].upper()

#Q:14 Join the it_companies with a string '#;  '
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
joined_strings="#; ".join(it_companies)
print(joined_strings)

#Q:15 Check if a certain company exists in the it_companies list.
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
does_exit="Google" in it_companies
print(does_exit)

#Q:16 Sort the list using sort() method
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort()
print(it_companies)

#Q:17 Reverse the list in descending order using reverse() method
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.reverse()
print(it_companies)

#Q:18 Slice out the first 3 companies from the list
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
first_three=it_companies[0:3]
print(first_three)

#Q:19 Slice out the last 3 companies from the list
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
last_three=it_companies[-3:]
print(last_three)

#Q:20 Slice out the middle IT company or companies from the list
middle_index=len(it_companies)//2
middle_company=it_companies[middle_index:middle_index+1]
print("Middle company: ",middle_company)

#Q:21 Remove the first IT company from the list
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.remove("Facebook")
print(it_companies)

#Q:22 Remove the middle IT company or companies from the list
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
middle_index=len(it_companies)//2
it_companies.pop(middle_index)
print(it_companies)

#Q:23 Remove the last IT company from the list
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.pop(-1)
print(it_companies)

#Q:24 Remove all IT companies from the list
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.clear()
print(it_companies)

#Q:25 Destroy the IT companies list
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
del it_companies

#Q:26 Join the following lists:
"""front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
"""
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
combine=front_end+back_end
print(combine)

#Q:27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

full_stack=combine.copy()
print(full_stack)
index_redux=full_stack.index("Redux")
full_stack.insert(index_redux+1, "Python")
full_stack.insert(index_redux+2,"SQL")
print(full_stack)


"""The following is a list of 10 students ages:"""
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Q:28 Sort the list and find the min and max age
ages.sort()
print("Sorted ages:",ages)
min_age=min(ages)
max_age=max(ages)
print("min age:",min_age)
print("max age:",max_age)

#Q:29 Add the min age and the max age again to the list
ages.extend([19,26])
print(ages)

#Q:30 Find the median age (one middle item or two middle items divided by two)
ages.sort()
print("Sorted ages:",ages)
 
n=len(ages)
if n % 2 == 0:
      # even number of items → average the two middle numbers
      middle1=ages[n//2 -1]
      middle2=ages[n//2]
      median_age=(middle1+middle2)/2
else:
      # odd number of items → middle number
      median_age = ages[n//2]
    
print("Median age:", median_age)

#Q:31 Find the average age (sum of all items divided by their number )
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
total=sum(ages)
count=len(ages)
average_age=total/count
print("Average age:",average_age)

#Q:32 Find the range of the ages (max minus min)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
min_age=min(ages)
max_age=max(ages)

range=max_age-min_age
print(range)

#Q:33 Compare the value of (min - average) and (max - average), use abs() method
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24, 19, 26]

average_age = sum(ages) / len(ages)
min_age = min(ages)
max_age = max(ages)

min_diff=abs(min_age-average_age)
max_diff = abs(max_age - average_age)

print("Distance from average to min:", min_diff)
print("Distance from average to max:", max_diff)

if min_diff > max_diff:
    print("Min age is farther from average than max age")
elif max_diff > min_diff:
    print("Max age is farther from average than min age")
else:
    print("Min and max ages are equally far from average")



#Q:34 Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
    
n=len(countries)
if n % 2 == 0:
    # Even number of countries → take two middle
     middle_countries = countries[n//2 - 1 : n//2 + 1]
else:
    # Odd number of countries → take one middle
     middle_countries = [countries[n//2]]

print("Middle country(ies):", middle_countries)

#Q;35 Divide the countries list into two equal lists if it is even if not one more country for the first half.
n=len(countries)
mid = (n + 1) // 2   # gives first half one extra if n is odd

first_half = countries[:mid]
second_half = countries[mid:]

print("First half:", first_half)
print("Second half:", second_half)
mid = (n + 1) // 2   # gives first half one extra if n is odd

first_half = countries[:mid]
second_half = countries[mid:]

print("First half:", first_half)
print("Second half:", second_half)

#Q:36 ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'].
#  Unpack the first three countries and the rest as scandic countries.
countries=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic_countries = countries

print(first)
print(second)
print(third)
print(scandic_countries)