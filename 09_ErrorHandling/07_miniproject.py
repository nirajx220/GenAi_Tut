class InvalidChaiError(Exception):
    pass

def bill(flavour,cups):
    menu = {"mashala": 30, "ginger": 25, "elaichi": 35}

    try:
        if flavour not in menu:
            raise InvalidChaiError(f"{flavour} is not in menu")
        
        if not isinstance(cups, int):
            raise TypeError("cups should be an integer")
        total_cost = menu[flavour] * cups
        print(f"total cost is {total_cost}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Thank you for visiting our chai shop")


bill("mashala", 2)
bill("ginger", "two")
bill("cumin", 2)
