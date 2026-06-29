order = {"mashala": 30, "ginger": 25}

#indx error when index dont exist
try:
    order["cumin"]
except KeyError:
    print("Key not found")


print("hello hchai")