import threading
import time

def monitor_tea_temperature():
    while True:
        print("Monitoring tea temperature...")
        time.sleep(2)

threading.Thread(target=monitor_tea_temperature, daemon=True).start()

print("Main thread is doing other work...")