#it is a callback example. customer in a restaurant put an order an the waiter delivers the order when it is ready

def checkFoodExistance(food_name:str):
    #              0       1        2
    arr_foods = ["pizza","pasta","salad"]
    arr_length = len(arr_foods)
    print(f"we have {arr_length} foods in our menu")

def orderFood(food_name:str,checkFoodExistance):
    print(f"your {food_name} will be ready soon")
    checkFoodExistance(food_name)

#actual programm use upper defined methods
order_string = input("What do you want to order?")
orderFood(order_string,checkFoodExistance)