# Write your code below this line 👇

print("Welcome to the tip calculator!")

total_bill = input("What was the total bill? $")
while not (total_bill.replace(".", "", 1).isdigit() and float(total_bill) > 0):
    total_bill = input("Invalid bill. Please try again: $")
total_bill = float(total_bill)

tip_percentage = input("How much tip would you like to give? 10, 12, or 15? ")
while not (tip_percentage.isdigit() and int(tip_percentage) in [10, 12, 15]):
    tip_percentage = input("Invalid tip choice. Please try again (10, 12, or 15): ")
tip_percentage = int(tip_percentage)

number_of_people = input("How many people to split the bill? ")
while not (number_of_people.isdigit() and int(number_of_people) > 0):
    number_of_people = input("Invalid number of people. Please try again: ")
number_of_people = int(number_of_people)

each_should_pay = total_bill * (1 + tip_percentage / 100) / number_of_people

print(f"Each person should pay: ${round(each_should_pay, 2):,}")
