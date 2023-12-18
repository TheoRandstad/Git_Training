"""mama"""
# Returns welcome message for a customer by customer name and location
# param name - Name of the customer
# param region - location
# return - Welcome message

def greet(name, region):
    """mama"""
    message = get_message(region)
    return message + " " + name


# Returns welcome message by location
# param region - location
def get_message(region):
    """mama"""
    if region == 'USA':
        return 'Hello'
    return 'Namaste'

print(greet('Jessa', 'USA'))
