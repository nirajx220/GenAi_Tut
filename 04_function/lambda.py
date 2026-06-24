chai_types = ["masala", "mashala", "cardamom", "tulsi"]

strong_chai = list(filter(lambda chai: chai != "mashala", chai_types))

print(strong_chai)