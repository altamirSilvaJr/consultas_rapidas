import aiohttp

async def fetch_data(session, offset):
    url = f"http://example.com?offset={offset}"
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        offset = 0
        while True:
            data = await fetch_data(session, offset)
            # do something with the data
            offset += 10000

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
