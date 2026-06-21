import asyncio
import time
text="""
Async Programming: Generate numbers asynchronously
Write an async function that counts down from 0 to 100 asynchronously and appends to a list named
"numbers" and returns the list.

The program can sleep asynchronously for 0.01 seconds in each iteration. [Optional]
"""

async def countdown():
    numbers=[]
    for i in range(101):
        numbers.append(i)
        await asyncio.sleep(0.01)
    return numbers

numbers=asyncio.run(countdown())
print(numbers)