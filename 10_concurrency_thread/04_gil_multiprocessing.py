import multiprocessing
import time

def crunch_numbers():
    print(f"started the process ....")
    count = 0
    for _ in range(100_00_00):
        count+=1
    print(f"finished the process ....")

if __name__ == "__main__":
    start = time.time()

    process1 = multiprocessing.Process(target=crunch_numbers)
    process2 = multiprocessing.Process(target=crunch_numbers)

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end = time.time()

    print(f"Total time taken: {end-start:.2f} seconds")
