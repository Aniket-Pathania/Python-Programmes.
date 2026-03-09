from temperature.celsius_to_fahrenheit import celsius_to_fahrenheit
from temperature import celsius_to_kelvin
from temperature import fahrenheit_to_celsius

def main():

    print("1 -> Celsius to Fahrenheit")
    print("2 -> Fahrenheit to Celsius")
    print("3 -> Celsius to Kelvin")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        c = float(input("Enter Celsius: "))
        print("Fahrenheit:", celsius_to_fahrenheit(c))

    elif choice == 2:
        f = float(input("Enter Fahrenheit: "))
        print("Celsius:", fahrenheit_to_celsius(f))

    elif choice == 3:
        c = float(input("Enter Celsius: "))
        print("Kelvin:", celsius_to_kelvin(c))

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()