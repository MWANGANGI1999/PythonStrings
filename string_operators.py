#String operators
#+,*,r,%,format(),in,not in
#its creates a path
a="Hello"
b="world"
print(r"c:\'documents'\python")
print("c://'documents'/python")
#it combines two strings together
a="Hello"
b="world"
print(a+b)
#it duplicates the string a four times
a="Hello"
b="world"
print(a*4)
#takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
a="Hello"
b="world"
print("hi{}".format(b))
#Evaluates to true if it finds a variable in the specified sequence and false otherwise.
a="Hello"
b="world"
print('h' in a)
print('l' in b)
#Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.
a="Hello"
b="world"
print('n' not in a )
print('l' not in b)
