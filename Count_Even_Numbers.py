

nums = [1,2,3,4,5,6,7,8,9,10]


def num_even(numbers):

    x = 0
    print(numbers)

    for n in numbers:

        a = n % 2

        if a == 0: # We've seen a single even number
            x = (x + 1)
            print(a)

    return x

num_even(nums) #Calling num_even with nums as an argument.

#is the output of (num_even gets nums) equal to 5?

assert(num_even(nums) == 5)




beef = [1,2,3,4,5]

def taco(lettuce):

    x = 0

    for y in lettuce:

        r = y % 2

    if r == 0:
        x = (x + 1)


    return x
