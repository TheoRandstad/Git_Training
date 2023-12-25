"""Multiply or sum based of condition"""
def multiplication_or_sum(num1, num2):
    """calculate product of two number"""
    product = num1 * num2
    # check if product is less then 1000
    if product <= 1000:
        return product
    return num1 + num2


RESULT = multiplication_or_sum(20, 30)
print("The result is", RESULT)

RESULT = multiplication_or_sum(40, 30)
print("The result is", RESULT)
