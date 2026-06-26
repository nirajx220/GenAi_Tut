class chai:
    origin = "India"

print(chai.origin)

chai.is_hot = True
print(chai.is_hot)

#creating objaects fromt the class

mashala = chai()
print(mashala.origin)
print(mashala.is_hot)

mashala.is_hot = False

print("class: ",chai.is_hot)
print(f"mashala {mashala.is_hot}")

