def createline(n):
    """Return a mixed string of stars ('*',) and dashes ('-',).
    set every star followed by a dash on a total length of n."""
    line = ''
    for i in range(n):
        if i % 2 == 0:
            line += '*'
        else:
            line += '-'
    return line[:n]
n = int(input("Enter the total length of the line: "))
print(createline(n))
