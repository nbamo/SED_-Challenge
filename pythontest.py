import re

def is_valid_number(number):
    # Check if the number matches the required pattern
    if not re.match(r'^[456](\d{3}-?\d{4}){3}$', number):
        return False

    # Remove hyphens if present
    number = number.replace('-', '')

    # Check for consecutive repeating digits
    for i in range(len(number) - 3):
        if number[i] == number[i+1] == number[i+2] == number[i+3]:
            return False

    return True

# Test the function
numbers = [
    "4123-4567-8901-2345",
    "4123456789012345",
    "5123-4567-8901-2345",
    "5123456789012345",
    "6123-4567-8901-2345",
    "6123456789012345",
    "4123-4444-4444-4445",
    "4123-4567-8901-23456",
    "41234567890123",
    "4123-4567-8901-234",
    "3123456789012345"
]

for number in numbers:
    if is_valid_number(number):
        print(f"{number}: Valid")
    else:
        print(f"{number}: Invalid")
