import colorama
from time import sleep
from colorama import Fore

from utils.Setting.setup_most import *
from utils.Setting.lib import colorama, time, aiohttp

colorama.init(autoreset=True)


def menu():
    print()
    print("[\x1b[95m1\x1b[95m\x1B[37m] 서버 체커")
    print("[\x1b[95m2\x1b[95m\x1B[37m] 나가기")


async def main():
    menu()
    option = int(input(f"[\x1b[95m>\x1b[95m\x1B[37m] 옵션: "))
    if option == 1:
        sleep(1)

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7",
            "Authorization": input(f"\n[\x1b[95m>\x1b[95m\x1B[37m] 토큰: "),
        }

        guildId = input(f"[\x1b[95m>\x1b[95m\x1B[37m] 서버 ID: ")

        base_url = f"https://discord.com/api/guilds/{guildId}"
        params = {"with_counts": "True"}
        async with (
            aiohttp.ClientSession() as session,
            session.get(url=base_url, headers=headers, params=params) as response,
        ):
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
    [{Fore.LIGHTMAGENTA_EX}아이콘{Fore.RESET}]         $:   https://cdn.discordapp.com/icons/{guildId}/{response['icon']}.webp?size=128
    """
        )

        sleep(6)
        await __import__("main").Hydron()
    elif option == 2:
        await __import__("main").Hydron()
