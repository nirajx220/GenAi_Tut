from pydantic import BaseModel, field_validator, model_validator


class User(BaseModel):
    name: str
    email: str

    @field_validator('username')
    def username_length(cls, value):
        if len(value) < 3:
            raise ValueError('Username must be at least 3 characters long')
        return value
    
class SignupForm(BaseModel):
    
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def passwords_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('Passwords do not match')
        return values

