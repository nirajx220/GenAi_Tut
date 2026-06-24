def serve_chai():
    chai_type = "masala" #local scope
    print(f"Serving {chai_type} chai")   #inside the functon variable


chai_type = "lemon"
serve_chai()    
print(f"Serving {chai_type} chai") # outside the function variable


def chai_counter():
    chai_order = "lemon" #enclosoing scope

    def print_order():
        chai_order = "ginger" #local scope
        print(f"Serving {chai_order} chai") 

    print_order()    

    print("outer", chai_order)    