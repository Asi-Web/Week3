## Asiwome Agbleze
## CMSC 11/1
## Spring 2026
## Week 3 - personal_info.py

# Collect and display basic personal information using corret data types.

# Ask the user for thier name (string)
name = input("What is your name? ")

# Ask for age; input() gives a string, so we concert it to an integer with int()
age = int(input("How old are you? "))

# Ask for the vlaue of pi; convert the string inout to a float so it can store decimals
pi_value = float(input("What do you think the value of pi is? "))

# Ask if the user is human.
# input() returns a string, so we compare it to the string "True" to create a boolean vlaue.
is_human = input("Are you human? (True/False) ") == "True"

# Construct one sentence that uses all four values.
# We use an f-string so we can insert variabbles directly inside the string.
sentence = (
    f"My name is {name}, I am {age} years old, the value of pi is {pi_value}, "
    f"and it is {is_human} that I am human."
)
# Print the first sentence
print(sentence)


