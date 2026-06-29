import threading
import time

def take_order():
    for i in range(1,4):
        print(f"Taking order for#{i}")
        time.sleep(1)


def brew_Chai():
    for i in range(1,4):
        print(f"Brewing Chai for#{i}")
        time.sleep(2)       

#creating threads

thread1 = threading.Thread(target=take_order)
thread2 = threading.Thread(target=brew_Chai)

#starting threads

thread1.start()
thread2.start()

#waiting for threads to complete

thread1.join()
thread2.join()

print("All orders are completed")