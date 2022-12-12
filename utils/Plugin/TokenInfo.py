import aiohttp
import asyncio
import datetime
from time import *

from colorama import Fore

from utils.Setting.setup_most import heads, languages

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def menu():
    print('')
    print('')
    print("[\x1b[95m1\x1b[95m\x1B[37m] 토큰 체커")
    print("[\x1b[95m2\x1b[95m\x1B[37m] 나가기")

def get_user_created_at(id: str) -> str:
    KST = datetime.timezone(datetime.timedelta(hours=9))
    timestamp = ((int(id) >> 22) + 1420070400000) / 1000
    return datetime.datetime.fromtimestamp(timestamp, tz=KST).strftime("%Y-%m-%d %H:%M:%S")

async def get_token_info(token: str):
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
        
    user_nitro_type = premium_types[response["premium_type"]]
    if response["avatar"] is not None:
        user_avatar_link = avatar_base_url.format(id=response["id"], hash=response["avatar"]) 
    else:
        user_avatar_link = None
    created_at = get_user_created_at(response["id"])    
    print(
            f"""
{Fore.RESET}{Fore.GREEN}####### 토큰 정보 #######{Fore.RESET}
[{Fore.LIGHTMAGENTA_EX}이름{Fore.RESET}]             $:   {response['username']}#{response['discriminator']} 
[{Fore.LIGHTMAGENTA_EX}ID{Fore.RESET}]               $:   {response['id']}
[{Fore.LIGHTMAGENTA_EX}토큰{Fore.RESET}]             $:   {token}
[{Fore.LIGHTMAGENTA_EX}이메일{Fore.RESET}]           $:   {response["email"]}
[{Fore.LIGHTMAGENTA_EX}전화번호{Fore.RESET}]         $:   {response["phone"]}
[{Fore.LIGHTMAGENTA_EX}계정 생성일{Fore.RESET}]      $:   {created_at}
[{Fore.LIGHTMAGENTA_EX}지역 및 언어{Fore.RESET}      $:   {languages[response['locale']]}
[{Fore.LIGHTMAGENTA_EX}니트로 구매 여부{Fore.RESET}] $:   {user_nitro_type}
[{Fore.LIGHTMAGENTA_EX}이차인증 여부{Fore.RESET}]    $:   {response["mfa_enabled"]}
[{Fore.LIGHTMAGENTA_EX}아바타 주소{Fore.RESET}]      $:   {user_avatar_link}
    """
    )

async def main():
    menu()
    option = int(input(f"[\x1b[95m>\x1b[95m\x1B[37m] 옵션: "))
    if option == 1:
        sleep(1)
        token = input(f"\n[\x1b[95m>\x1b[95m\x1B[37m] 토큰: ")
        get_token_info(token)
        sleep(6)
        await __import__("main").Hydron()
    elif option == 2:
        await __import__("main").Hydron()
