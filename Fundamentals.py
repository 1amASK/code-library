#VARIABLES
age = 20 #an int
age = 21.0 #a floating interger
first_name = "John" #a string
is_new = True #a boolean
"""
    -Examples of several different, basic variables.
        -The variable is declared.
        -The '=' then points it to the value you want.
            -Which itself is stored somewhere on the computer's memory.
"""

#VARIABLE COVERTORS
str() #turns the variable/value within the parenthesis into a string

int() #turns the variable/value within the parenthesis into an interger

float() #turns the variable/value within the parenthesis into a floating interger; for examples 3 becomes 3.0

bool() #turns the variable/value within the paranthesis into a boolean

#Output & Input
print("Hello World!") #a function which prints the result of all items within the parenthesis
first_name = input("What is your name?\n") #a function which takes the result of prompting a user for an input and returns the value as a string. -In this case, it is given immediately to the variable 'first_name'.
print("Hello " + first_name.capitalize()) #concatenates (joins the strings) and prints the result

#ADDITION PROGRAM
first_number = float(input("First#: "))
second_number = float(input("Second#: "))
sum = first_number + second_number
sum = str(sum)
print("Sum: " + sum)

#IF & ELSE STATEMENTS
"""
name = input("Say my name!\n")

if name.lower() == "heisenberg":
	print ("You're goddamn right!")
else:
	print("Fuck off! I'm the one whoo knocks!")

The 'if' and 'else' statement which can be used to make simple, conditional triggers for the compiler to run specific codes. If there's a need for more conditions, you can also use 'elif' statements.
"""

#WHILE LOOP
name = input("Say my name!\n")
while name.lower() != "heisenberg":
    print("Fuck off! I'm the one who knocks!")
    name = input("Say my actual name!\n")
print("You're goddamn right!")
#The ‘while’ statement which can be used to loop a certain set of conditional code until a specific result is achieved. -In this instance, the while loop prompts the user until the correct name is entered.

#BASIC STRING FUNCTIONS
example1 = "String"

example1.upper() #turns the entire string uppercase; does not modify the original string, only returns a new string
example1.lower() #turns the entire string lowercase; does not modify the original string, only returns a new string
example1.capitalize() #capitalizes the first letter of a string and turns the remaining ones into lower case letters
example1.title() #capitalizes the first letter of each word, while the rest remain lowercase

#example1.find(0) #checks if the string contains a character or sequence of characters; it returns the index of the first accurence of characer(s); if it doesn't find the character(s), -1 will be returned as an index

#example1.replace("Str", "W") #replaces a character(s) with something else; nothing will change if it doesn't find that character(s); does not modify the original string

#example1.join() #joins an array of strings

"""
    -List of String Functions.
        -Strings are considered as objects and, for that reason, can be manipulated without directly modifying the original value unless told to.
        -The index of a string object begins with 0 being the first letter. And counts backwards from -1.
"""

#EXAMPLE CODES
example1 = "String Test"
print(example1.lower()) #=> "string test"
print(example1)
print(example1.upper()) #=> "STRING TEST"
print(example1)
print(example1.capitalize()) #=> "String test"
print(example1)
print(example1.title()) #=> "String Test"

x = "-".join(["Coding", "is", "awesome"])
print(x) #=> "Coding-is-awesome"
x = " ".join(["Coding", "is", "awsome."])
print(x) #=> "Coding is awesome."

example1 = "Python for Beginners"
print(example1.find("y")) #this will return a 1; which is the index of the first occurance of 'y'
print(example1.replace("for", "4")) #=> 'Python 4 Beginners'
print(example1) #this will return the original string; as the original string was not modified

print("Python" in example1) #this checks to see if we have the word 'Python' in the variable 'example1'; this returns the boolean value 'True'
