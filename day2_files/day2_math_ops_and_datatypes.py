# using variable, and math operator, then checking data types
# concatenate using str() the data types

num1 = 5
num2 = 10

addition = num1 + num2
subtraction = num2 - num1
multiplication = num1 * num2
division = num2 / num1
modulus = num1 % num2
exponential = num1 ** num2
floor_division = num2 // num1

print("Result for addition: " +str(addition)) # addition
print("Result for subtraction: " +str(subtraction)) # subtraction
print("Result for multiplication: " +str(multiplication)) # multiplication
print("Result for division: " +str(division)) # division
print("Result for modulus: " +str(modulus)) # modulus
print("Result for exponential: " +str(exponential)) # exponential
print("Result for floor_division: " +str(floor_division)) # floor_division
print("")
print("addition is " + str(type(addition)))
print("subtraction is " + str(type(subtraction)))
print("multiplication is " + str(type(multiplication)))
print("division is " + str(type(division)))
print("modulus is " + str(type(modulus)))
print("exponential is " + str(type(exponential)))
print("floor_division is " + str(type(floor_division)))