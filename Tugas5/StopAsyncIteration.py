import asyncio

async def my_async_generator():
    for i in range(5):
        yield i
        await asyncio.sleep(1)

async def main():
    async for value in my_async_generator():
        print(value)
    raise StopAsyncIteration

asyncio.run(main())
