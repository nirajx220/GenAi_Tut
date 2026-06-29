def process_order(item, quantity: int):
    try:
        price = {"mashala": 30}[item]
        cost = price * quantity
        print(f"total cost is {cost}")


    except KeyError:
        print("chai is not in menu")
    except TypeError:
        print("quantity should be a number")

process_order("ginger", 2)        
process_order("mashala", "two")