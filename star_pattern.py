# Asiwome Agbleze
# CMSC 111
# Spring 2026
# Assignment 2 - Nested Loops Star pattern
for row in range(1, 6): # row will take values 1, 2, 3, 4, 5
# Inner loop controls the number of stars per row
 for star in range(row):
    # Print a star without moving to a new line yet
     print("*", end=" ")
# Move to the next line after printing stars for this row
print()

