# Using this knowledge, implement the get_min(a: int, b: int) -> int 
# function in the code editor. It should return the minimum of a and b. 
# If they are equal, it doesn't matter which value you return.

def get_min(a: int, b: int) -> int:
    if a < b:
        return a
    else:
        return b
    
    return min(a, b)

    
# don't modify code below this line
print(get_min(10, 11))
print(get_min(5, -7))
print(get_min(20, 20))
