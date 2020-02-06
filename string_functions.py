#Built-in string functions
#returns the string in sentence case
a="Hello Kenya"
b=a.capitalize()
print(b)
#returns the string in sentence case
a="hello Kenya"
print(a.capitalize())
#returns the string in upper case
a="Hello Kenya"
print(a.upper())
#returns the string in lower case
a="Hello Kenya"
print(a.lower())
#returns a string where all the characters are lower case.
a = "Hello Kenya"
b = a.casefold()
print(b)
#will center align the string, using a specified character (space is default) as the fill character.
a= "Hello Kenya"
b= a.center(20)
print(b)
#Join all items in a tuple into a string, using a umderscore character as separator:
a= "Hello Kenya"
b= "_".join(a)
print(b)
#Split a string into a list where each word is a list item:
a= "Hello Kenya"
b= a.split()
print(b)
#Make the lower case letters upper case and the upper case letters lower case:
a= "Hello Kenya"
b= a.swapcase()
print(b)

