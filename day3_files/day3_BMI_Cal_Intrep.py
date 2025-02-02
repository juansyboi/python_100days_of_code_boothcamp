weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
bmi = float(bmi)
if bmi < 18.5:
    print("underwight")
elif bmi >= 18.5 and bmi < 25:
    print("normal weight")
elif bmi >= 25:
    print("overwight")