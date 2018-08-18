
#Creation of a basic list:

l = ['lettuce', 'beef', 'tomato', 'onion', 'guac', 'salsa']


#Select the first item in the list:

first_item = l[0]
print(first_item)
#This will print first item in list of 'l':

#Select the last item in the list:

last_item = l[-1]
print (last_item)
#This will print last item in list of 'l':

#Two ways to loop through this list:

# Using indices, aka numerical positions! i.e. 0, 1, 2, 3, ...
for i in range(0, len(l)):
    print(i, l[i])
#output
'''(0, 'lettuce')
(1, 'beef')
(2, 'tomato')
(3, 'onion')
(4, 'guac')
(5, 'salsa')'''

# Using 'iteration', no numerical indexes are used here.
# The variable 'item' is set six times, each time it takes
# on the next value inside of 'l'.
for item in l:
    print(item)

#output
'''lettuce
beef
tomato
onion
guac
salsa'''

#Adding items to our list:

l.append('sour_cream')
print (l)
#output
#['lettuce', 'beef', 'tomato', 'onion', 'guac', 'salsa', 'sour_cream']

#Inserting data into our list at a particular position

#Insert takes two values, the first is where you want "it", I.e. the begining would be 0, the second argument is what your adding to the location, I.e. the data itself.
l.insert(0, 'chicken')

print (l)
#['chicken', 'lettuce', 'beef', 'tomato', 'onion', 'guac', 'salsa', 'sour_cream']


#What exactly can be added to lists? How complex can a list be? Lists within lists?

#This list is an example of adding new types of meats to our original "taco list",
# however we also add in 'l' the above list we originally created, and a number(int)
#This is a list that contains a mixed data structure
new_list = ['fish', 'bison', 'shrimp', l, 4]
print (new_list)
#output
#['fish', 'bison', 'shrimp', ['chicken', 'lettuce', 'beef', 'tomato', 'onion', 'guac', 'salsa', 'sour_cream'], 4]

# Adding data to original list makes "new_list" APPEAR as though it has changed.
# It doesn't change 'new_list' itself, it only changes how 'new_list' appears
l.append('lengua')
print (new_list)
#output
#['fish', 'bison', 'shrimp', ['chicken', 'lettuce', 'beef', 'tomato', 'onion', 'guac', 'salsa', 'sour_cream', 'lengua'], 4]

#Math inside of a list:

math_list = [4 * 4, 7 ** 2]
print (math_list)
#output [16, 49]

math_list2 = [6 * 6]

#Concatenation of lists:
concat_list = math_list + math_list2
print (concat_list)
#output  [16, 49, 36]

#Slicing a list:
#Print the first two items in our original 'l' list
first_two = l[:2]
print (first_two)

#Copy a lists

# Difference between shallow and deep copies of data structures
x = l # Shallow copy of l. That is, x refers to l, and is NOT a new list.

l[1] = 'slugs' # This appears to modify x.

print(x) # We see slugs.
#output
#['chicken', 'slugs', 'beef', 'tomato', 'onion', 'guac', 'salsa', 'sour_cream', 'lengua']

#Deep copy of a lists

x = l[:]

del l[1] # Remove slugs from list 'l'

print(x)
#X doesn't have slugs removed:
#['chicken', 'slugs', 'beef', 'tomato', 'onion', 'guac', 'salsa', 'sour_cream', 'lengua']
print(l)
#However list 'l' does have 'slugs' removed
# ['chicken', 'beef', 'tomato', 'onion', 'guac', 'salsa', 'sour_cream', 'lengua']
