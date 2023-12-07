# Function to check if every element in a list is an integer or string
check_elements = lambda lst: all(isinstance(element, (int, str)) for element in lst)

# Example usage
my_list = [1, 'hello', 3, 'world', 5]
result = check_elements(my_list)

if result:
    print("All elements are either integers or strings.")
else:
    print("Some elements are not integers or strings.")
