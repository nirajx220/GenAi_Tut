import asyncio

async def brew_chai():
    print("Start brewing chai...")
    await asyncio.sleep(3)
    print("End brewing chai...")

asyncio.run(brew_chai())    
