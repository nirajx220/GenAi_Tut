import asyncio
import aiohttp
import time

async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"fetched {url} with status {response.status}")


async def main():
    urls = [
        "https://httpbin.org/delay/2"]*3
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch_url(session, url) for url in urls])
        tasks = [fetch_url(session, url) for url in urls]

asyncio.run(main())