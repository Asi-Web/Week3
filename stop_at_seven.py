## Asiwome Agbleze
## CMSC 1111
## Spring 2026
## Assignment Loop from 1 to 100

# Loop through numbers from 1 to 100 
for number in range(1, 101):
    # Check if the number is divisible by 7
    if number % 7 == 0:
        # Print the first number divisible by 7 and stop the loop
        print("First number divisible by 7 is:", number)
        break

