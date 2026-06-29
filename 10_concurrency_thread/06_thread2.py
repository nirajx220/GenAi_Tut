import threading
import time

def prepare_tea(type_of_tea,wait_time):
    print(f"Preparing {type_of_tea}...")
    time.sleep(wait_time)
    print(f"{type_of_tea} is ready!")

t1 = threading.Thread(target=prepare_tea, args=("Green Tea", 2))    
t2 = threading.Thread(target=prepare_tea, args=("Black Tea", 3))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
