class chai_cup:
    size = 150 #150ml


    def describe(self):
        return f"A {self.size}ml cup of chai"
    
cup = chai_cup()

print(cup.describe())
print(chai_cup.describe(cup))

cup_two = chai_cup()
cup_two.size = 200
print(cup_two.describe())