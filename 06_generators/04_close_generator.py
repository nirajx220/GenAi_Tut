def loacl_chai():
    yield "masala chai"
    yield "green tea"


def imported_chai():
    yield "cardamom chai"
    yield "tulsi chai"


def full_menu():
    yield from loacl_chai()
    yield from imported_chai()


for chai in full_menu():
    print(chai)


def chai_stall():
    try:
        order = yield("waiting for order")
    except:
        print("Order not received")

stall = chai_stall()
print(next(stall))