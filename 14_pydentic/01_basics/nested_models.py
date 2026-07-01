from typing import List, Optional
from pydantic import BaseModel, Field


class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int    
    name: str
    address: Address

address = Address(street="123 Main St", city="New York", postal_code="10001")    
user = User(id=1, name="John Doe", address=address)
print(user)

user_data = {
    "id": 2,
    "name": "Jane Smith",
    "address": {
        "street": "456 Elm St",
        "city": "Los Angeles",
        "postal_code": "90001"
    }
}

user_from_dict = User(**user_data)
print(user_from_dict)