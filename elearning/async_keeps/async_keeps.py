import asyncio


async def t1():
    print("1")
    await asyncio.sleep(1)
    print("2")

async def t2():
    print("3")
    await asyncio.sleep(1)
    print("4")

async def main():
    tarefa1 = asyncio.create_task(t1())
    tarefa2 = asyncio.create_task(t2())

    await tarefa1
    await tarefa2

# asyncio.run(main())