import asyncio
import datetime
import time
import importlib

import aiohttp
from colorama import Fore

from utils.Setting.setup_most import heads, languages, TokenValidator
from utils.Plugin.PluginABC import PluginABC

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class TokenInfo(PluginABC):
    plugin_name = "토큰 체커"

    @classmethod
    def get_user_created_at(cls, id: str) -> str:
        KST = datetime.timezone(datetime.timedelta(hours=9))
        timestamp = ((int(id) >> 22) + 1420070400000) / 1000
        return datetime.datetime.fromtimestamp(timestamp, tz=KST).strftime("%Y-%m-%d %H:%M:%S")

    @classmethod
    async def get_token_info(cls, token: str):
        premium_types = {
            0: None,
            1: "Nitro Classic",
            2: "Nitro",
            3: "Nitro Basic"
        }
        avatar_base_url = "https://cdn.discordapp.com/avatars/{id}/{hash}.webp?size=256"
        url = "https://discord.com/api/v10/users/@me"

        async with (
            aiohttp.ClientSession() as session,
            await session.get(url=url, headers=heads(token=token)) as response
        ):
            response = await response.json()

        user_nitro_type = premium_types[response.get("premium_type", 0)]
        if response["avatar"] is not None:
            user_avatar_link = avatar_base_url.format(id=response["id"], hash=response["avatar"])
        else:
            user_avatar_link = None
        created_at = cls.get_user_created_at(response["id"])

        message = (f"\n{Fore.RESET}{Fore.GREEN}####### 토큰 정보 #######{Fore.RESET}\n"
                   f"[{Fore.LIGHTMAGENTA_EX}ID{Fore.RESET}]               $:   {response['id']}\n"
                   f"[{Fore.LIGHTMAGENTA_EX}토큰{Fore.RESET}]             $:   {token}\n"
                   f"[{Fore.LIGHTMAGENTA_EX}이메일{Fore.RESET}]           $:   {response.get('email')}\n"
                   f"[{Fore.LIGHTMAGENTA_EX}전화번호{Fore.RESET}]         $:   {response.get('phone')}\n"
                   f"[{Fore.LIGHTMAGENTA_EX}계정 생성일{Fore.RESET}]      $:   {created_at}\n"
                   f"[{Fore.LIGHTMAGENTA_EX}지역 및 언어{Fore.RESET}      $:   {languages.get(response.get('locale'))}\n"
                   f"[{Fore.LIGHTMAGENTA_EX}니트로 구매 여부{Fore.RESET}] $:   {user_nitro_type}\n"
                   f"[{Fore.LIGHTMAGENTA_EX}이차인증 여부{Fore.RESET}]    $:   {response.get('mfa_enabled')}\n"
                   f"[{Fore.LIGHTMAGENTA_EX}아바타 주소{Fore.RESET}]      $:   {user_avatar_link}\n")

        print(message)

    @classmethod
    async def main(cls):
        option = super().get_option()

        if option == 1:
            time.sleep(1)
            token = input(f"\n[\x1b[95m>\x1b[95m\x1B[37m] 토큰: ")
            await TokenValidator(token)
            await cls.get_token_info(token)

            input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] 엔터를 눌러주세요: ')
            await importlib.import_module("main").Hydron()
        else:
            await importlib.import_module("main").Hydron()
