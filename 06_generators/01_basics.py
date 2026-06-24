def simple_generator_chai():
    yield "Cup 1: Mashala chai "
    yield "Cup 2: Green tea"

stall = simple_generator_chai()    

# for cup in stall:
#     print(cup)

def get_chai_list():
    return ["Cup 1", "Cup 2"] 
   
#generator function

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"

chai = get_chai_gen()
print(next(chai))
