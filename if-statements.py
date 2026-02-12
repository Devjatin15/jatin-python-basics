# if = do some code only if some condition is true
# else = do some code if the condition is false

age = int(input("Enter your age: "))

if age >= 18:
    print("you are eligible for a credit card")
elif age >= 100:
    print("you are eligible for a senior citizen card")
else:
    print("you are not eligible for a credit card")