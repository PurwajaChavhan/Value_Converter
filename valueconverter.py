def convert_temperature():
    print("\nWhich conversion do you want to choose:-")
    print("1. Celsius to Faranheit")
    print("2. Faranheit to Celsius")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        temp = float(input("Enter temperature in celsius: "))
        print(f"{temp} degree celsius is equal to {(temp*9/5)+32} degree faranheit.\n")
    elif choice == 2:
        temp = float(input("Enter temperature in faranheit: "))
        print(f"{temp} degree faranheit is equal to {(temp-32)*5/9} degree celsius.\n")
    else:
        print("Invalid input...please try again\n")

def convert_currency():
    print("\nWhich conversion do you want to choose:-")
    print("1. Dollar to pound")
    print("2. Pound to Dollar")
    print("3. Dollar to INR")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = float(input("Enter currency in dollars: "))
        print(f"{value} dollars in pounds will be {value*0.73}\n")
    elif choice == 2:
        value = float(input("Enter currency in pounds: "))
        print(f"{value} pounds in dollars will be {value/0.73}\n")
    elif choice==3:
        value = float(input("Enter currency in dollar: "))
        print(f"{value} dollar in INR will be {value*74.94}\n")


def convert_lengths():
    print("\nWhich conversion do you want to choose:-")
    print("1. Centimeter to foot and inches")
    print("2. Foot and inches to centimeter")
    print("3. Centimeter to meter")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = float(input("Enter length in cm: "))
        inches = value/2.54
        feet = inches/12
        print(f"{value} centimeter is equal to {feet} feet and {inches} inch\n")
    elif choice == 2:
        feet = float(input("Enter length in feet: "))
        inches = float(input("Enter length in inches: "))
        length = (feet*12 + inches)*2.54
        print(f"{feet} feet and {inches} inches in centimeter will be {length}\n")
    if choice == 3:
        value = float(input("Enter length in cm: "))
        meter = value*0.01
        print(f"{value} centimeter is equal to {meter} meter \n")

print("===== Welcome to Value Converter =====")
while 1:
    print("Which option would you like to choose:-")
    print("1. Convert temperature")
    print("2. Convert currency")
    print("3. Convert lengths")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        convert_temperature()
    elif choice == 2:
        convert_currency()
    elif choice == 3:
        convert_lengths()
    elif choice == 4:
        print("Exiting...\n ######  Thanks for using Value Converter  ######")
        exit(0)
