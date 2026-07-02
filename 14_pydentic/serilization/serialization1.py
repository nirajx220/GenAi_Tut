from pydantic import BaseModel
from typing import Optional, List, Dict

class Cart(BaseModel):
    user_id: int
    items: List[str] 
    quantity: Dict[str, int]
    status: Optional[str] = None  # Optional field with default value None
    stock: Optional[Dict[str, int]] = None  # Optional field with default value None

class Customer(BaseModel):
    name: str
    email: str
    address: Optional[str] = None  # Optional field with default value None
    cart: Optional[Cart] = None  # Optional field with default value None

cart_data = {
    'user_id': 101,
    'items': ['Laptop', 'Smartphone'],
    'quantity': {'Laptop': 1, 'Smartphone': 2},
    'status': 'Pending',
    'stock': {'Laptop': 5, 'Smartphone': 10}
}    

customer_data = {
    'name': 'John Doe',
    'email': 'john.doe@example.com',
    'address': '123 Main St'
}

cart = Cart(**cart_data)
customer = Customer(**customer_data, cart=cart)

print(cart)