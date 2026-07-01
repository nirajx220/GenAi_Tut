from pydantic import BaseModel, field_validator

class Person(BaseModel):
    name: str
    age: int

    @field_validator('name')
    def name_must_not_be_empty(cls, value):
        if not value:
            raise ValueError('Name must not be empty')
        return value
    
class Product(BaseModel):
    price: float

    @field_validator('price', mode='before')
    def price_must_be_positive(cls, value):
        if isinstance(value, str):
            if not value:
                raise ValueError('Price must not be empty')
            return float(value.replace('$', '').replace(',', ''))
        return value
    

class DateRange(BaseModel):
    start_date: str
    end_date: str

    @field_validator('start_date', 'end_date')
    def date_must_be_valid(cls, value):
        # Add your date validation logic here
        return value    
    
date = DateRange(start_date='2023-01-01', end_date='2023-12-31')    
print(date)
