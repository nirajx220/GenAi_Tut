def pure_chai(cups):
    return cups*10

total_chai = 0


#not recomanded to use global variables, but for the sake of
def impure_chai(cups):
    global total_chai
    total_chai += cups * 10


