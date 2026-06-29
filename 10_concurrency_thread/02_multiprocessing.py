import multiprocessing
import time

def brew_chai(name):
    print(f"start of chai brewing for {name}")
    time.sleep(3)
    print(f"end of chai brewing for {name}")

if __name__ == "__main__": 
    chai_makers = [
        multiprocessing.Process(target=brew_chai, args=(f"chai_maker_{i+1}",))
        for i in range(3)
    ]

    # starting processes
    for p in chai_makers:
        p.start()



    # waiting for processes to complete
    for p in chai_makers:
        p.join()


    print("All chai brewing is completed")
