class ChaiOrder:
    def __inti__(self,type_,size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai"
    

order  = ChaiOrder("masala", 150)
print(order.summary())


order_two = ChaiOrder("green", 200)
print(order_two.summary())