#start
print("Hello,my name is Addi,i add numbers for you.\nWhat is your first number?")
while True:
    try:
        num1 = int(input())
        break
    except ValueError:
        print("Please enter a valid number.")

print("Thank you.\nWhat is your second number?")
while True:
    try:
        num2 = int(input())
        break
    except ValueError:
        print("Please enter a valid number.")

result = num1 + num2
print("Awesome! The result is " + str(result))
#end