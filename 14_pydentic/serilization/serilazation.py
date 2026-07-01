from pydantic import BaseModel, ConfigDict, Field
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):    
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime 
    address: Address
    tags: List[str] = Field(default_factory=list)

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
        }
    )

user = User(
    id=1,
    name="John Doe",
    email="john.doe@example.com",
    created_at=datetime(2024, 6, 1, 12, 30),
    address=Address(street="123 Main St", city="New York", postal_code="10001"),
    is_active=False,
    tags=["developer", "python"]
)


python_dict = user.model_dump()
print(python_dict)
