import threading
import time

def boil_milk():
    priint(f"boil milk started...")
    time.sleep(2)

    print(f"boil milk finished...")

def toast_bread():
    print(f"toast bread started...")
    time.sleep(3)

    print(f"toast bread finished...")

    start = time.time()

    t1 = threading.Thread(target=boil_milk)
    t2 = threading.Thread(target=toast_bread)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time.time()
    print(f"Total time taken: {end-start:.2f} seconds")