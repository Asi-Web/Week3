## Asiwome Agbleze
## CMSC 1111
## Spring 2026
# Assignment 4 - Skip multiples of 5


# Loop through the numbers from 1 to 50
for number in range(1, 51):
    # If the number is divisible by 5, skip the rest of the iteration
    # continue jumps to the next number in the loop without printing
    if number % 5 == 0:
        continue

    # This line only runs for number NOT divisible by 5
    print(number)