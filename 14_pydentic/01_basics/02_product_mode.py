from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


product_one = Product(id=1, name='Laptop', price=1000.07, in_stock=True)

product_two = Product(id=2, name='Smartphone', price=500.90)

print(product_one)
print(product_two)



#alwas use type annotations int, float , bool 
#set sensible dafault

