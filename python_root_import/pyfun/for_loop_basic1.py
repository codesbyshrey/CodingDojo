# For Loop Basic 1 - Core Assignment
# ----------------------------------

# Basic - print all integers from 0-150 (printed including 150)
for n in range (0, 151):
     print (n)

print ("basic exercise complete here //////////")

# Multiples of 5 - Print all the multiples of 5 from 5 to 1000 - remember that when setting up for loops, your third number is a step counter
for n in range (5, 1000, 5):
     print (n)

print ("multiples assignment done here //////////")

# Counting the Dojo Way - Print integers from 1-100. If divisible by 5, print "Coding", and if by 10, print "Coding Dojo"
     #basically just fizzbuzz from js but now in python syntax

for n in range (1, 100): #technically printed without including 100
     if n%10 ==0: print ("Coding Dojo")
     elif n%5 ==0: print ("Coding")
     else: print (n)

print ("codingdojo assignment done here //////////")

# Whoa. That Sucker's Huge - add odd integers from 0-500K, and print the final sum - easier to define variable at the start, repeat within the for loop, print outside the function at the end
totalOdd = 0
for i in range (1, 500000, 2):
     totalOdd = totalOdd + i
print (totalOdd)
print ("whoa, that suckers huge //////////")

# Countdown by 4s - Print positive numbers starting from 2018 and counting down by 4s
for i in range (2018, 0, -4):
     print (i)

print ("countdown by 4s done here ///////////")


# Flexible Counter - set lowNum, highNum, and mult. Range of values are low and high, print integers that are multiples of mult on successive lines

lowNum = 4
highNum = 420
mult = 6

for n in range (lowNum, highNum, mult):
     print (n)

print ("flexible counter done here")