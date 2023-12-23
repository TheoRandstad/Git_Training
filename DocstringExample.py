'''Use of the docstring'''
def greet(name, region):
    """Returns welcome message for a customer by customer name and location
    	param name - Name of the customer
	param region - location
	return - Welcome message"""
    message = get_message(region)
    return message + " " + name


def get_message(region):
    """Returns welcome message by location
    	param region - location"""
    if region == 'USA':
        return 'Hello'
    return 'Namaste'

print(greet('Jessa', 'USA'))
