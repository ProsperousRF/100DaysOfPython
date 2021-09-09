# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

combine_name = name1.lower() + name2.lower()
first = 0
first += combine_name.count("t")
first += combine_name.count("r")
first += combine_name.count("u")
first += combine_name.count("e")

second = 0
second += combine_name.count("l")
second += combine_name.count("o")
second += combine_name.count("v")
second += combine_name.count("e")

score = first * 10 + second

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
