is_special_guest = False

print("\nWelcome to Michell Island!")
while True:
    height = input("What's your height in cm?\n")
    try:
        height = int(height)
        break
    except ValueError:
        print("Oops, invalid number! Please try again: ")

if height >= 120:
    print("Great!")
    while True:
        age = input("And what's your age?\n")
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
            wants_photo = input("Do you want to have a photo take? (costs: $3)\n(Type 'y' for Yes and 'n' for No)\n")
            if wants_photo.lower() == "y":
                total_bill += 3
                break
            elif wants_photo.lower() == "n":
                break
            else:
                print("Oops, invalid number! Please try again: ")

    print(f"\n~~ Your total bill would be: ${total_bill} ~~")

else:
    print("\nSorry, but it's dangerous for you to play in the Michell Island...")
    print("But don't worry! You can go north to the Fredy's Park and have fun!")