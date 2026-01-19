def check_equal(x, y) -> bool:
    return x == y

def check_not_equal(x, y) -> bool:
    return x != y

def check_less_than(x, y) -> bool:
    return x < y

def check_greater_than(x, y) -> bool:
    return x > y

def check_less_than_or_equal(x, y) -> bool:
    return x <= y

def check_greater_than_or_equal(x, y) -> bool:
    return x >= y


# Don't change below this line
print("2 is equal to 2:", check_equal(2, 2))
print("-2 is equal to 2:", check_equal(-2, 2))

print("-2 is not equal to 2:", check_not_equal(-2, 2))
print("2 is not equal to 2:", check_not_equal(2, 2))

print("2 is less than 3:", check_less_than(2, 3))
print("3 is less than 3:", check_less_than(3, 3))

print("3 is greater than 2:", check_greater_than(3, 2))
print("3 is greater than 2:", check_greater_than(3, 3))

print("3 is less than or equal to 3:", check_less_than_or_equal(3, 3))
print("4 is less than or equal to 3:", check_less_than_or_equal(4, 3))

print("3 is greater than or equal to 3:", check_greater_than_or_equal(3, 3))
print("2 is greater than or equal to 3:", check_greater_than_or_equal(2, 3))