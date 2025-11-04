def dreieck(n):
    """Return a string that represents a triangle of height n using asterisks."""
    result = ""
    for i in range(1, n + 1):
        result += '*' * i + '\n'
    return result  
n = int(input("Enter the height of the triangle: "))
print(dreieck(n))
