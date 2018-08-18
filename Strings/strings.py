
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

#Tells you if something is inside the string. I.e. Tacos are inside the string called 'sentence'
print('Tacos' in sentence)
#output: True

# Tells you where some smaller string, a 'substring', is found inside of the original string.
print(sentence.index('are'))
# output: 6

# visual aid:
# t a c o s   a r e
# 0 1 2 3 4 5 6 7 8

# Tells you how many times a substring is found inside of the original string.
print(sentence.count('a'))


# String formating
x = 'taco'
y = 'dog'

print "my {} likes {}".format(x, y)
#output my taco likes dog
#Examples of string formating - https://pyformat.info/



for i in range(10):
    print("{:2d}^2 = {:3d}".format(i, i**2))

#output
'''
0^2 =   0
1^2 =   1
2^2 =   4
3^2 =   9
4^2 =  16
5^2 =  25
6^2 =  36
7^2 =  49
8^2 =  64
9^2 =  81
'''
