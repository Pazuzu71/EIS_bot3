import asyncio
import aioftp
from config import host, port, login, password
import os


print(os.getcwd())
print(os.path.join(os.getcwd(), 'temp'))
async def get_list(host, port, login, password):
    async with aioftp.Client.context(host, port, login, password) as client:
        x = await client.list('/fcs_regions/Tulskaja_obl/contracts/currMonth', recursive=False)
        await client.download('/fcs_regions/Tulskaja_obl/contracts/currMonth', os.path.join(os.getcwd(), 'temp'), write_into=True)
    # for path, info in x:
    #     print(path)

        # for path, info in (await client.list(recursive=True)):
        #     if info["type"] == "file" and path.suffix == ".mp3":
        #         await client.download(path)


async def main():
    tasks = [
        asyncio.create_task(get_list(host, port, login, password))
    ]
    await asyncio.wait(tasks)

asyncio.run(main())
