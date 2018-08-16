''' The purpose of this script is to count up how many inhabitants each location
has.

Example output:

Hell:       1
Nevada:     3
Illinois:   5
'''

myfile = open('location_data.txt')

a = {}


for line in myfile.readlines():
    b = line.split(',')
    #print(b)

    b = b[1]
    b = b.strip() # Remove newline
    #This index at 1
    print(b)

    # If location not in dictionary, initialize it to zero.
    if b not in a:
        a[b] = 0

    # If location IS in dictionary, we want to add one to it.
    a[b] += 1

    print(a)


    #Result - The first colum in the .txt file 'Name' was removed as a result.

    #print(line.split(','))
    #print(line.strip(','))

#dog = {'color': 'brown', 'count': 4}

#d = {
    #'Illinois': 3,
    #'Nevada': 2,
    #'Hell': 1,
#}


#dog['count'] += 1 #add one to dog['count']

'''
Random Examples:
    ',,a,a,,,'.strip(',')       -> 'a,a'
    ',,a,a,,,'.replace(',', '') -> 'aa'

'''
