#!/usr/bin/python3
"""
Module for converting temperatures between Celsius and Fahrenheit.
"""


# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    """
    Main function to handle user input and perform conversion.
    """
    # Prompt for temperature input
    temp_input = input("Enter the temperature to convert: ")

    # Validate temperature is numeric
    try:
        temperature = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Prompt for unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    unit = unit.strip().upper()

    if unit == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")

    elif unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")

    else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")


if __name__ == "__main__":
    main()