

device_status = input("enter the device status: active/offline")
temp = input("enter the tempreture in celsius:")
if device_status == "active":
    if temp > 35:
        print("Device is overheating.")
    else:
        print("Device temperature is normal.")
else:
    print("Device is offline.")