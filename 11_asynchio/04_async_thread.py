import asyncio
import time
import concurrent.futures

def check_stock(item):
    print(f"Checking stock for {item}...")
    time.sleep(2)
    return f"{item} is in stock!: 42"

async def main():
    loop = asyncio.get_running_loop()

    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "masala chai")
        print(result)
        
asyncio.run(main())
