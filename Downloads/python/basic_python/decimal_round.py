def round_float(number, decimal_places):
    format_string = "{:.{}f}".format(number, decimal_places)
    rounded_number = float(format_string)
    return rounded_number

# Example usage:
number = float(input('Enter a float number: '))
decimal_places = int(input('Enter number of decimal places to be rounded off: '))
rounded_number = round_float(number, decimal_places)
print(f"Original number: {number}")
print(f"Rounded number to {decimal_places} decimal places: {rounded_number}")