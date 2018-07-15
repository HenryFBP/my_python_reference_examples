myfile = open('tacos.txt', 'r')

a = []

for line in myfile.readlines():
    line = line.strip()

    try:
        n = float(line) # Turn a string into a number
        a.append(n) # Add our number onto the end of our list
        print(n)
    except ValueError as e:
        print("'" + line + "' is a crappy value. Not converting.")

a.sort()
print(a)
