import asyncio

import aiohttp
from aiohttp import ClientResponseError

from utils.Setting.setup_most import *
from utils.Plugin.PluginABC import PluginABC
from utils.Setting.lib import mainHeader, tokens

class FR_Terror(PluginABC): # token.txt에 있는 모든 토큰으로 특정 유저에게 친추를 보냄
    plugin_name = "친구 요청 테러"

    @classmethod
    async def friend_request(cls, token: str, user: str, delay: float):
        url = "https://discord.com/api/v10/users/@me/relationships"
        try:
            username, discriminator = user.split('#')
            headers = mainHeader(token)
            form = {
                "username": username,
                "discriminator": discriminator
            }
            
            async with (
                aiohttp.ClientSession() as session,
                session.get(url=url, headers=headers, json=form) as response
            ):
                response.raise_for_status()
            
            print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] {user[0]}#{user[1]}에게 친추 요청을 보냈습니다! ")
            
        except ClientResponseError:
            print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] 실패...")
        
        await asyncio.sleep(delay)
            
    @classmethod
    async def main(cls):
        option = super().get_option()
        
        if option == 1:
            user = input(f"\n[\x1b[95m>\x1b[95m\x1B[37m] 유저이름 + 유저태그: ")
            delay = float(input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] 지연시간: '))

            asyncio.gather(*(cls.friend_request(token=token, user=user, delay=delay) for token in tokens))
            
            input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] 엔터를 눌러주세요: ')
            await importlib.import_module("main").Hydron()
        else:
            await importlib.import_module("main").Hydron() 