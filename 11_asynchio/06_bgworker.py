import asyncio
import threading
import time

def background_worker():
    while True:
        time.sleep(1)
        print("LOgging from background worker...")

async def fetch_data():
    await asyncio.sleep(3)
    print("Fetching data...")


threading.Thread(target=background_worker, daemon=True).start()

asyncio.run(fetch_data())