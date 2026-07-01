from pydantic import BaseModel, Field
from typing import Optional
import re


class Employee(BaseModel):
    id: int
    name: str = Field(
        ..., 
        min_length=3, 
        max_length=50, 
        description="Employee name must be between 3 and 50 characters"
    )
    department: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Employee department must be between 2 and 100 characters"
    )
    age: Optional[int] = Field(
        None,
        ge=0,
        description="Employee age must be a non-negative integer"
    )
    salary: Optional[float] = Field(
        ...,
        ge=0.0,
    )


class User(BaseModel):
    email: str = Field(
        ...,
        regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        description="Email must be a valid email address"
    )
    phone_number: Optional[str] = Field(
        ...,
        regex=r'^\+?[1-9]\d{1,14}$',
        description="Phone number must be a valid phone number"
    )
    age: int = Field(
        ...,
        ge=18,
        le=65,
        description="Age must be between 18 and 65"
    )
    discount: float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Discount must be between 0.0 and 100.0"
    )