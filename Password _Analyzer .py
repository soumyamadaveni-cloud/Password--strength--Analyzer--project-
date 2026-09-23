import string
import  math
print("==================================")
print("PASSWORD STRENGTH ANALYSER")
print("==================================")
password = input("Enter a test password:")
score = 0
if len(password) >= 8:
	score += 1
if any(c.islower( ) for c in password):
	score += 1
if any(c.isupper( ) for c in password):
	score += 1
if any(c.isdigit( ) for c in password):
	score += 1
if any(c in string.punctuation for c in password):
	score += 1
if score <= 2:
	strength="WEAK"
elif score <= 4:
	strenth="MEDIUM"
else :
     strength="STRONG"
print( )
print("password length:", len(password))
print("strength:",strength)
print("score:",score,"\5")
if len(password) < 8:
	print("Suggestion: Add at least 8 characters")
if not any(c.islower( ) for c in password):
	print("Suggestion:  Add lower case letters.")
if not any(c.isupper( ) for c in password):
	print("Suggestion: Add upper case letters.")
if not any(c.isdigit( )for c in password):
	print("Suggestion: Add numbers.")
if not any(c in string.punctuation for c in password):
	print("Suggestion:Add special characters.")
print("==================================")
print( )
print("==================================")
print("CUSTOM WORDLIST GENERATOR ")
print("==================================")
name=input(" Enter a test name:")
pet=input("Enter a test pet name:")
year=input("Enter a test year name:")
wordlist=[ name,
                 pet,
                 year,
                 name + year,
                 pet + year,
                 name + pet,
                 name + "123",
                 pet + "123",
                 name + "@" + year,
                 pet + "@" + year
                 ]
filename ="custom_wordlist.txt"
with open(filename,"w") as file:
	for word in wordlist:
		file.write(word + "\n")
print( )
print("Wordlist generated successfully!")
print("Total words:",len(wordlist))
print("saved as:",filename)
print("==================================")