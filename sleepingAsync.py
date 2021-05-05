import asyncio
import time


def sleeper(name, startTime):
    elapsedTime = format(time.time() - startTime, '.1f')
    print(elapsedTime + 's: ' + name + ' zZzZzZ')
    time.sleep(2)
    elapsedTime = format(time.time() - startTime, '.1f')
    print(elapsedTime + 's: ' + name + ' awake')


async def asyncSleeper(name, startTime):
    elapsedTime = format(time.time() - startTime, '.1f')
    print(elapsedTime + 's: ' + name + ' zZzZzZ')
    await asyncio.sleep(2)
    elapsedTime = format(time.time() - startTime, '.1f')
    print(elapsedTime + 's: ' + name + ' awake')


async def main(startTime):

    # Synchronous sleep
    names = ['a', 'b', 'c', 'd', 'e']
    for name in names:
        sleeper(name, startTime)
    # Asynchronous sleep
    tasks = []
    for name in names:
        tasks.append(asyncSleeper(name, startTime))
    print('Created tasks')
    await asyncio.gather(*tasks)
# Create event loop
loop = asyncio.get_event_loop()
startTime = time.time()
loop.run_until_complete(main(startTime))
loop.close()
