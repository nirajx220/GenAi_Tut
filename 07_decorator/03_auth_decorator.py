from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied. Admins only.")
            return func(user_role)
        
    return wrapper  

@require_admin

def acce_tea_inventory(role):
    print("Accessing tea inventory...")

acce_tea_inventory("user")  
acce_tea_inventory("admin")