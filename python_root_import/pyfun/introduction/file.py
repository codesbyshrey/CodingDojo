# file.py with Shreyas :)

num1 = 42
# this is an inline comment that will only exist for a single line
num2 = 2.3
# this is declaring a variable with the assignment operator
# not an equals operator - initializes num2 as a decimal number
"""
this is a multiline comment
this can help me present the rest of this text
goal is to comment in same line of code about corresponding concept from the file.txt that was also provided
"""

boolean = True # booleans can be true or false

#strings must be presented within quotation marks. Is there a particular difference between single quotes and double quotes? Perhaps not
string = 'Hello World'

# here we're initializing an array, with comments in between the string values and using brackets to identify that it is an array
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

#whoa we have a class below, where we have assigned values etc.
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit)) #here we can print very specifically the kind of placeholder we're looking for

#here we're looking for to print the first indexed value at the array
""" arrays start indexing at 0,
so this print statement will actually print sausage"""
print(pizza_toppings[1])
pizza_toppings.append('Mushrooms')
print(person['name'])

#below we are changing the modifiers for each of the values in our key value pairs, specifically the ones attached to name and eye color. with eye color, we're technically adding a new one. Notice how this comment, even though it is multilined in VScode, is actually a single line of code on line 32
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])

# welcome to conditionals, we are kicking it off with if statements
"""
there are else statements that are also included, and else if is also an option. elif is sometimes how it's understood in other languages syntax"""

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

"""
here we have lengths of strings being considered
python has some built in functions as libraries
we'll later learn how to refer and import to these library functions
in order to have much greater ability to access tools"""
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

#below here we're looking at for and while loops. for loops repeat based on certain criteria provided, and repeat. Without a specific counter value to increase by, they will default to increasing by one. Our third for loop here has a counter of 3 as the last parameter, so it will print 2-5-8 but not 10
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0

#while loops repeat as long as a certain condition continues to be met, meaning that by default it is likely to run. there is a risk here of an infinite loop
while(x < 5):
    print(x)
    x += 1

#pop and push functions allow us to add values to an array as needed
pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

#here we are looking at nested loops, where we are trying to determine pure equality. a single = normally is considered an assignment operator, where the right side value is applied to the left side variable (or whatever else)
"""
double equals helps you check for pure equality, sometimes across types (string and number being the same in some regards)
tripe equals means checking for a complete match, which will exclude some natural type conversion accomodation"""
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

#here we are DEFining a function, with underscores in between. Rather odd
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

#here we are calling the function specifically outside of the function definition. without doing this, the function will simply exist but not be acted upon. sometimes this is useful / can be missed if there are not return values or print functions that it provides
print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)