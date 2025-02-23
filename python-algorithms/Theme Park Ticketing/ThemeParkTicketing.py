# Write your code below this line 👇

# print("\nWelcome to Python Pizza Deliveries!")
#
# while True:
#     size = input("What size pizza do you want? S($15), M($20) or L($25): ")
#     if size.upper() in ["S","M","L"]:
#         if size.upper() == "S":
#             bill = 15
#         elif size.upper() == "M":
#             bill = 20
#         else:
#             bill = 25
#         break
#     else:
#         print("Oops, invalid input! Please try again: \n(S, M or L)")
#
# while True:
#     want_pepperoni = input("Do you want pepperoni on your pizza? ($2 for 'S' and $3 for 'M'&'L') -- Y or N: ")
#     if want_pepperoni.upper() in ["Y", "N"]:
#         if want_pepperoni.upper() == "Y" and size.upper() == "S":
#             bill += 2
#         elif want_pepperoni.upper() == "Y" and (size.upper() == "M" or size.upper() == "L"):
#             bill += 3
#         break
#     else:
#         print("Oops, invalid input! Please try again: \n(Y / N)")
#
# while True:
#     extra_cheese = input("Do you want extra cheese? ($1) -- Y or N: ")
#     if extra_cheese.upper() in ["Y", "N"]:
#         if extra_cheese.upper() == "Y":
#             bill += 1
#         break
#     else:
#         print("Oops, invalid input! Please try again: \n(Y / N)")
#
# print(f"Your final bill is: ${bill}.")

is_special_guest = False
print("Welcome!")
while True:
    height = input("What's your height in cm?")
    try:
        height = int(height)
        break
    except ValueError:
        print("Oops, invalid number! Please try again: ")

if height >= 120:
    print("Great!")
    while True:
        age = input("And what's your age? ")
        try:
            age = int(age)
            break
        except ValueError:
            print("Oops, invalid number! Please try again: ")

    if 45 <= age <= 55:
        print("Congratulations! You're so special to get ALL FREE to play everything in our land!\nEnjoy your days!")
        total_bill = 0
        is_special_guest = True
    elif age > 18:
        print("Adult tickets are: $12")
        total_bill = 12
    elif 12 <= age <= 18:
        print("Youth tickets are: $7")
        total_bill = 7
    else:
        print("Child tickets are: $5")
        total_bill = 5

    if not is_special_guest:

        while True:
            wants_photo = input("Do you want to have a photo take? (costs: $3)\n(Type 'y' for Yes and 'n' for No) ")
            if wants_photo.lower() == "y":
                total_bill += 3
                break
            elif wants_photo.lower() == "n":
                break
            else:
                print("Oops, invalid number! Please try again: ")

    print(f"Your total bill would be: ${total_bill}")

else:
    print("Sorry, but it's dangerous for you to play in the Michell Island...")
    print("But don't worry! You still can go to Fredy's Part to have fun!")

# print("Welcome to the tip calculator!")
#
# total_bill = input("What was the total bill? $")
# while not (total_bill.replace(".", "", 1).isdigit() and float(total_bill) > 0):
#     total_bill = input("Invalid bill. Please try again: $")
# total_bill = float(total_bill)
#
# tip_percentage = input("How much tip would you like to give? 10, 12, or 15? ")
# while not (tip_percentage.isdigit() and int(tip_percentage) in [10, 12, 15]):
#     tip_percentage = input("Invalid tip choice. Please try again (10, 12, or 15): ")
# tip_percentage = int(tip_percentage)
#
# number_of_people = input("How many people to split the bill? ")
# while not (number_of_people.isdigit() and int(number_of_people) > 0):
#     number_of_people = input("Invalid number of people. Please try again: ")
# number_of_people = int(number_of_people)
#
# each_should_pay = total_bill * (1 + tip_percentage / 100) / number_of_people
#
# print(f"Each person should pay: ${round(each_should_pay, 2):,}")
