import re

def validate_us_phone_number(number):
    # Regular expression for validating US phone numbers
    pattern = re.compile(r'^\(\d{3}\) \d{3}-\d{4}$')

    return bool(re.match(pattern, number))

# Example usage:
phone_number_to_validate = "(555) 123-4567"
if validate_us_phone_number(phone_number_to_validate):
    print(f"{phone_number_to_validate} is a valid US phone number.")
else:
    print(f"{phone_number_to_validate} is not a valid US phone number.")
