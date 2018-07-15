
d = {
    'apple': 'tasty',
    'banana': 'super tasty',
    'two': 'number',
    'food': ['yougurt', 'taco', 'bread',]
}

l = ['tasty','super tasty', 'number']
#where 'apple' = 0, 'banana' = 1, 'two' = 2

print(d)

print(d['apple'])

            # 1 to 2, NOT including 1
print(d['food'][1:2])

if 'taco' in d['food']:
    print("we got a taco in our food!")

# add entry for 'slugs' as 'cute'
d['slugs'] = 'cute'

# add chips at the end.
d['food'].append('chips')


#insert 'pizza' inbetween taco and bread.
d['food'].insert(2, 'pizza')

print(d)

# for key, value in d.items():
#     print(str(key) + " : " + str(value))
