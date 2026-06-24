cup = input("Enter the size of the chai cup(small/medium/large): ").lower()

if cup == "small":
    print("Price is 20 ruppees.")
elif cup == "medium":
    print("Price is 30 ruppees.")
elif cup == "large":
    print("Price is 40 ruppees.")
else:
    print("Invalid cup size. Please choose small, medium, or large.")