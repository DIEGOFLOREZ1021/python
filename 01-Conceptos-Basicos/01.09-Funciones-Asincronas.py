import asyncio

async def main():
    asyncio.gather(func1(),func2())

async def func1():
    print("Hola...")
    await asyncio.sleep(5)
    print("....Mundo")

async def func2():
    for i in range (11):
        print(i)

print("Inicio")
asyncio.run(main())
print("Fin")

