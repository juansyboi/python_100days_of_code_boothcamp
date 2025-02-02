print("Welcome to Checker for Even and Odd. \nGuide: Use only Integer, and input 1st and 2nd Number to check if the Result is Even or Odd")
num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

checker_evod = (num1 / num2) % 2
checker_mod = num1 % num2

if checker_evod == 0:
    print(f"Result is Even, and Modulo of {checker_mod}")
else:
    print(f"Result is Odd, Modulo of  {checker_mod}")