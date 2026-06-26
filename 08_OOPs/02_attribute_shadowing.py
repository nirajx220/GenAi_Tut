class chai:
    temperature = "hot"
    strengrh = "strong"

cutting = chai()
print(cutting.temperature)


cutting.temperature = "cold"
print("after modification:", cutting.temperature)
print("direct look into the class:", chai.temperature)

del cutting.temperature
print(cutting.temperature)