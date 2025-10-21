def ageMachine(age: int):
    if age > 50:
        print("Du bist alt geworden!")
    else:
        print("werd erwachsen.")
    print("This is the age machine.")
#Definition immer zuerst, dann Aufruf

"""
this function only accepts two integers and returns their sum as an integer
and then returns it
"""

def addTwoNumbers(first_number: int, second_number: int)-> int:
    return first_number + second_number




print("Wie alt bist du?")
"""
input function return is always a string 
input function is something like async await in javascript 
"""
age_from_user = input()
age_from_user = int(age_from_user)
      
ageMachine(age_from_user)
