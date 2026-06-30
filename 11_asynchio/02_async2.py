import asyncio

async def brew(name):
    print(f"Start brewing chai for {name}...")
    await asyncio.sleep(3)
    print(f"End brewing chai for {name}...")

async def main():
    await asyncio.gather(
        brew("chai_maker_1"),
        brew("chai_maker_2"),
        brew("chai_maker_3")
    )

def chai_makers():
    asyncio.run(main())

chai_makers()
