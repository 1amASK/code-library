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

#VARIABLE CHANGERS
str() #turns the variable called upon or the value within the paranthesis into a string

int() #turns the variable called upon or the value within the paranthesis into an interger

float() #turns the variable called upon or the value within the paranthesis into a floating interger; for examples 3 becomes 3.0

first_name.lower() #turns the entire string lowercase
first_name.upper() #turns the entire string uppercase


#OUTPUT & INPUT
print("Hello World!") #a function which prints the result of all items within the parenthesis

first_name = input("What is your name?\n") #a function which takes the result of prompting a user for an input and returns the value as a string. -In this case, it is given immediately to the variable 'first_name'.

print("Hello " + first_name.upper()) #concatenates (joins the strings) and prints the result

#If & Else Statements
"""
name = input("Say my name!\n")

if name.lower() == "heisenberg":
	print ("You're goddamn right!")
else:
	print("Fuck off! I'm the one whoo knocks!")

The ‘if’ and ‘else’ statement which can be used to make simple, conditional triggers for the compiler to run certain, specific codes.
"""

#WHILE LOOP
name = input("Say my name!\n")
while name.lower() != "heisenberg":
    print("Fuck off! I'm the one who knocks!")
    name = input("Say my actual name!\n")
print("You're goddamn right!")
#The ‘while’ statement which can be used to loop a certain set of conditional code until a specific result is achieved. -In this instance, the while loop prompts the user until the correct name is entered.