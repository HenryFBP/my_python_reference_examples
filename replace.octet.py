def replace_octet(address, pos, replacement): # Function takes three arguments.

    # We turn the address into a list.
    l = address.split('.') #'1.2.3.4' -> ['1', '2', '3', '4']

    # We replace the item at position 'pos' with our replacement.
    l[pos] = replacement

    #
    # Let's say pos = 1, replacement = 100.
    #
    # l = ['1', '2', '3', '4']
    #       0    1    2    3
    #
    # l[1] = 100
    #
    # l = ['1', '100', '3', '4']

    # Return our list joined by periods.
    return '.'.join(l)

print(replace_octet('1.2.3.4', 2, '100'))
