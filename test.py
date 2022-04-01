import asyncio


async def a():
    await asyncio.sleep(1000)

asyncio.run(a())
print(1)
