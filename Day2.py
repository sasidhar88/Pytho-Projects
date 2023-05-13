print("Hello" [4])

print(len(int(12345)))

num_char  = len(input("What iss your name: "))

print (type(num_char))

Type Casting
------------

num_char  = len(input("What iss your name: "))
new_num_char = str(num_char)
print ("your name has"+ " " + new_num_char + " " + "Characters")

Project-1
---------
user_input = input("type a two difit num: ")

first = int(user_input[-2])
second = int(user_input[-1])

addition = first + second

print(addition)


Mathematical operators
----------------------
2 + 2
2 - 2

2 * 2
print(2 ** 2) power off

print(3 * 3 + 3 / 3 - 3) == 7.0

print (3 / (3 + 3) * 3 - 3)

Project-2
---------

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


hts = int(height)
wt = int(weight)

print (hts/wt**wt)



height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


hts = float(height)
wt = int(weight)

bmi = wt / hts ** 2

bmi_int = int(bmi)

print(bmi_int)


Number manipulation
-------------------
round()

print(round(8 / 3)) --- it will round the number


print(round(8 / 3, 2))  rounds to upto two decimals

print (8 // 3)

F-string
--------

score = 0
height = 1.8
male = True


print(f"your height is {height}, score is {score}, male {male}")


Project
-------

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_a = 90 - int(age) 

days = age_a * 365
weeks = age_a * 52
months = age_a * 12

print (f"You have {days} days, {weeks} weeks, and {months} months left.")


Day-2-Project
-------------

print("Welcome to the tip calculator!")

bill = input("What was the total bill? $")
bill_int = int(bill)

tip = input("How much tip would you like to give?")

tip_int = int(tip)

people = input("How many people to split the bill? ")

people_int = int(people)



amount = bill_int * tip / 100

actuall_amt = bill_int + amount

each person should pay

Each person should pay:

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give?"))

people = int(input("How many people to split the bill? "))

tip_value = bill * tip / 100
total_bill = bill + tip_value
split = total_bill / people
final_amount = round(split, 2)
print (f"each should pay : ${final_amount}")
