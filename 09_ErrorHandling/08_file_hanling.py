# file = open("sample.txt", "w")


# try:
#     file.write("hello hchai")
# finally:
#     file.close()




with open("sample.txt", "w") as file:
    file.write("hello hchai")