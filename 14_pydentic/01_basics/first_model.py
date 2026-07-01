from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {'id': 101, 'name': 'Niraj', 'is_active': True}
user = User(**input_data)  #unpack data using ** operator


print(user)





##import basemodel
#type annotations
#unpack data using ** operator   model init
#automatic data validation