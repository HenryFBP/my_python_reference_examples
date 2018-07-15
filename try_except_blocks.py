
user_response = raw_input("Enter a number? ")
print(user_response)

try:
    x = int(user_response)
except:
    print("You didn't enter a number.")
