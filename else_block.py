
print("Enter two numbers and divide them. ")

x = float(input("first number"))
y = float(input("second number"))



try:
    result = x / y
except :
    print("You can't divide by zero")

else:
    print(result)

#if x > y:
#    print("First number is greater than")
