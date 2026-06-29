class OutOfIngredientsError(Exception):
    pass

def make_chai(milk,sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Out of ingredients")
    print("chais ready")

make_chai(1, 1)