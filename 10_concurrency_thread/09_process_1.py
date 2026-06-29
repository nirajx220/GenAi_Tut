import threading
import time

def cpu_heavy():
    print(f"Starting CPU heavy task...")
    total = 0
    for _ in range(10**7):
        total += 1
    print(f"Finished CPU heavy task...")  

start = time.time()    
threads = [threading.Thread(target=cpu_heavy) for _ in range(4)]
[t.start() for t in threads]
[t.join() for t in threads]
end = time.time()
print(f"Total time taken: {end - start}")