#Exercise day 07

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Q:1 Find the length of the set it_companies
print(len(it_companies))

#Q:2 Add 'Twitter' to it_companies
it_companies.add("twitter")
print(it_companies)

#Q:3 Insert multiple IT companies at once to the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.update(("emporion Soft","Codev","Splunk"))
print(it_companies)

#Q:4 Remove one of the companies from the set it_companies
it_companies.remove("Google")
print(it_companies)

#Q:5 Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C=A.union(B)
print(C)

#Q:6 Find A intersection B
diff=A.intersection(B)
print(diff)

#Q:7 Are A and B disjoint sets
common=A.isdisjoint(B)
print(common)

#Q:8 Join A with B and B with A
first=A.union(B)
print(first)
second=B.union(A)
print(second)

#Q:9 What is the symmetric difference between A and B
sysdiff=B.symmetric_difference(A)
print(sysdiff)

#Q:10 Is A subset of B
subset=A.issubset(B)
print(subset)

#Q:11 Delete the sets completely
del A
del B

#Q:12 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
st=set(age)
if len(age)>len(st):
    print("Age is bigger")
else:
    print("List is bigger")

#Q:13 "I am a teacher and I love to inspire and teach people". How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
words=sentence.split()
print(words)
unique_words=set(words)
print(unique_words)
print("Number of unique words:",len(unique_words))