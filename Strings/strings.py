
#Basic string

sentence = "Tacos are really cool and tasty"
#           0,1,2,3
# You can index strings just like lists.

print(sentence[2]) # 'c' in tacos.
#output c

print(sentence[0:5])
#output tacos

print(sentence.split(' '))
#The split method's argument defaults to a string with a space in itself.
#output  - ['tacos', 'are', 'really', 'cool', 'and', 'tasty']


#Concatenation of strings:
add_string = ", baby!"

print(sentence + add_string)
#output - tacos are really cool and tasty, baby!


#Commonly used functions
print (sentence.upper())
#TACOS ARE REALLY COOL AND TASTY

print (sentence.lower())
#tacos are really cool and tasty

print (sentence.title())
#Tacos Are Really Cool And Tasty

#replace takes two arguments, will replace first argument with second argument
# e.g. "hello".replace('l', 'x') -> 'hexxo'

print(sentence.replace('a', 'eoa'))
#ouput Teoacos eoare reeoally cool eoand teoasty

#Method Chaining of strings
print (sentence.replace('Tacos', 'Pizza').replace('are', 'is'))
#output - Pizza is really cool and tasty
