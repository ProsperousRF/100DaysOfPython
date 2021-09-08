# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#There are 365 days in a year, 52 weeks in a year and 12 months in a year.
estimate_age = 90 - int(age)
estimate_days = estimate_age * 365
estimate_weeks = estimate_age * 52
estimate_months = estimate_age * 12
print(f"You have {estimate_days} days, {estimate_weeks} weeks, and {estimate_months} months left.")