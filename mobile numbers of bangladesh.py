import re

def validate_bangladeshi_mobile_number(number):
    pattern = re.compile(r'^(?:\+88)?01[3-9]\d{8}$')
    return bool(re.match(pattern, number))

# Example usage:
mobile_number_to_validate = "+8801712345678"
if validate_bangladeshi_mobile_number(mobile_number_to_validate):
    print(f"{mobile_number_to_validate} is a valid Bangladeshi mobile number.")
else:
    print(f"{mobile_number_to_validate} is not a valid Bangladeshi mobile number.")
