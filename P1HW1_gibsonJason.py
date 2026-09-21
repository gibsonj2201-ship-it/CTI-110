# Jason Gibson
# calculating exponents and addition and subtraction

#calculate exponents 

print("-----Calculating Exponents-----")
print()

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

answer = base ** exponent

print()
print(f"{base} raised to the power of {exponent} is {answer} !!")

print()
print("-----Addition and Subtraction-----")
print()

starting = int(input("Enter a starting integer: "))
add = int(input("Enter an integer to add: "))
subtract = int(input("Enter an integer to subtract: "))

result = starting + add - subtract

print()
print(f"{starting} + {add} - {subtract} is equal to {result}")
