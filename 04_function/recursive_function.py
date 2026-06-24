def pour_chai(n):
    if n == 0:
        return
    print("Pouring chai...")
    return pour_chai(n - 1)


print(pour_chai(5))