import importlib

import aiohttp
import colorama
from colorama import Fore

from utils.Plugin.PluginABC import PluginABC
from utils.Setting.setup_most import TokenValidator

colorama.init(autoreset=True)

class ServerChecker(PluginABC):
    plugin_name = "서버 체커"
    
    @classmethod
    async def get_server_info(cls, token: str, guild_id: str):
        headers = {
                "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7",
                "Authorization": token,
        }

        base_url = f"https://discord.com/api/guilds/{guild_id}"
        params = {"with_counts": "True"}
        async with (
            aiohttp.ClientSession() as session,
            session.get(url=base_url, headers=headers, params=params) as response):
            
            response = await response.json()
            owner_id = response["owner_id"]
            owner_url = f"{base_url}/members/{owner_id}"
            async with session.get(
                url=owner_url, headers=headers, params=params
            ) as owner:
                owner = await owner.json()

        print(
            f"""
{Fore.RESET}{Fore.GREEN}####### 서버 정보 #######{Fore.RESET}
[{Fore.LIGHTMAGENTA_EX}서버이름{Fore.RESET}]       $:   {response['name']} 
[{Fore.LIGHTMAGENTA_EX}서버ID{Fore.RESET}]         $:   {response['id']}
[{Fore.LIGHTMAGENTA_EX}서버 주인{Fore.RESET}]      $:   {owner['user']['username']}#{owner['user']['discriminator']} 
[{Fore.LIGHTMAGENTA_EX}서버 주인 ID{Fore.RESET}]   $:   {response['owner_id']}
[{Fore.LIGHTMAGENTA_EX}멤버수{Fore.RESET}]         $:   {response['approximate_member_count']}
[{Fore.LIGHTMAGENTA_EX}지역{Fore.RESET}]           $:   {response['region']}
[{Fore.LIGHTMAGENTA_EX}아이콘{Fore.RESET}]         $:   https://cdn.discordapp.com/icons/{guild_id}/{response['icon']}.webp?size=128
"""
)

    @classmethod
    async def main(cls):        
        option = super().get_option()
        if option == 1:
            token = input(f"\n[\x1b[95m>\x1b[95m\x1B[37m] 토큰: ")
            TokenValidator(token)
            guild_id = input(f"[\x1b[95m>\x1b[95m\x1B[37m] 서버 ID: ")
            await cls.get_server_info(token=token, guild_id=guild_id)
            
            input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] 엔터를 눌러주세요: ')
            await importlib.import_module("main").Hydron()
        else:
            await importlib.import_module("main").Hydron()
    
    