height = int(input("What is your height? "))

if height > 120:
    age = int(input("Nice! Now Tell us your age? "))
    if age <= 12:
        print("price is $2")
    elif age <= 18 and age >= 13:
        print("Price is $3")
    elif age >= 60:
        print("price is $1.50")
    else:
        print("Price is $5")

    isPhoto = input("Do you want a photo? 'y' for 'Yes' and 'n' for 'NO'")
    if isPhoto == "y":
        print("additional cost is $3")
    if isPhoto == "n":
        print("Thank you!")

else:
    print("Your Free to Enter")