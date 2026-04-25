# nested dictionaries and lists

# UPDATE VALUES IN DICTIONARIES AND 
# dictionary[row]['key'].append('value')
# dictionary[row]['key'].pop(position)

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# print (x[1][0])
x[1][0] = 15
print (x[1][0])

# print(students[0]["last_name"])
students[0]["last_name"] = "Bryant"
print(students[0]["last_name"])

# print(sports_directory["soccer"][0])
sports_directory["soccer"][0] = "Andres"
print(sports_directory["soccer"][0])

# print (z[0]["y"])
z[0]["y"] = 30
print (z[0]["y"])

     # change the value 10 in x to 15
     # change the last_name of the first student from Jordan to Bryant
     # in the sports_directory, change Messi to Andres
     # change the value 20 in z to 30

#ITERATE THROUGH A LIST OF DICTIONARIES
     #create a function that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value

students = [
          {'first_name':  'Michael', 'last_name' : 'Jordan'},
          {'first_name' : 'John', 'last_name' : 'Rosales'},
          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
          {'first_name' : 'KB', 'last_name' : 'Tonel'}
     ]
def iterateDictionary(students):
     print ('List of keys')
     for key, val in students[0].items(): # now we have to make this a loop because this only does one person
          print ("{} : {}".format(key, val))
     for key in students:
          print (key)

iterateDictionary(students)

"""
def iterateDictionary(incoming_list):
     for diction in incoming)list
          print(f"First Name: {diction['first_name']} : Last Name {diction['last_name']}")
          for key in diction:
               print(f"{key} : {diction[key]})
"""

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#GET VALUES FROM A LIST OF DICTIONARIES
def iterateDictionary2(key_name, some_list):
#      key_name = 
#      some_list = 
     for dic in some_list:
          if key_name in dic:
               print(dic[key_name])
          else:
               print("key not found")

# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

#ITERATE THROUGH A DICTIONARY WITH LIST VALUES

dojo = {
      'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC',  'Burbank'],
      'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
 }

def printInfo(some_dict):
     #some_dict = 0
     for key in some_dict:
          print(f"{len(some_dict[key])} : {key.upper()}")
          for value in range(len(some_dict[key])):
               print(some_dict[key][value])
          print("")

printInfo(dojo)




#      #create a function who's values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. for example:

# printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon