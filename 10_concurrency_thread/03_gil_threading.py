import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} starting brewing...")
    count =0
    for _ in range(100_00_00):
        count+=1
    print(f"{threading.current_thread().name} finished brewing...")


thread1 = threading.Thread(target=brew_chai, name="Thread-1")
thread2 = threading.Thread(target=brew_chai, name="Thread-2")


#start th thread


start = time.time()
thread1.start()
thread2.start()
#wait for thread to complete
thread1.join()
thread2.join()

end = time.time()

print(f"Total time taken: {end-start:.2f} seconds")