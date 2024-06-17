



def main():
    """Convert temperatures between Celsius and Fahrenheit"""
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = convert_celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit}°F")

    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = convert_fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F = {celsius}°C")


def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return celsius * 9.0 / 5.0 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5.0 / 9.0


if __name__ == "__main__":
    main()
