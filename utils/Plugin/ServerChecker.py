import requests
import os
import sys
import os.path
import colorama
import webbrowser
from time import sleep
from colored import fg, attr
from requests.api import options
from colorama import Fore, Back, Style, init

from utils.Setting.setup_most import *

colorama.init(autoreset=True)


def menu():  # UI
    print(
        f"""
        [\x1b[95m1\x1b[95m\x1B[37m] 서버 체크
        [\x1b[95m2\x1b[95m\x1B[37m] 나가기
        """)
menu()

option = int(input(f"[\x1b[95m>\x1b[95m\x1B[37m] 선택 ㄱ: "))


def fetch():
    menu()
if option == 1:
    sleep(1)

    headers = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7",
            "Authorization": input(f"\n[\x1b[95m>\x1b[95m\x1B[37m] 토큰 입력: "),
    }

    guildId = input(f"[\x1b[95m>\x1b[95m\x1B[37m] 서버 ID 입력: ")

    response = requests.get(
            f"https://discord.com/api/v10/guilds/{guildId}",
            headers=headers,
            params={"with_counts": True},
    ).json()

    owner = requests.get(
            f"https://discord.com/api/v10/guilds/{guildId}/members/{response['owner_id']}",
            headers=headers,
    ).json()

    print(
            f"""
        {Fore.RESET}{Fore.GREEN}####### 서버 정보 #######{Fore.RESET}
        [{Fore.LIGHTMAGENTA_EX}서버 이름{Fore.RESET}]      $:   {response['name']} 
        [{Fore.LIGHTMAGENTA_EX}서버 ID{Fore.RESET}]        $:   {response['id']}
        [{Fore.LIGHTMAGENTA_EX}서버 주인{Fore.RESET}]      $:   {owner['user']['username']}#{owner['user']['discriminator']} 
        [{Fore.LIGHTMAGENTA_EX}서버 주인 ID{Fore.RESET}]   $:   {response['owner_id']}
        [{Fore.LIGHTMAGENTA_EX}멤버수{Fore.RESET}]         $:   {response['approximate_member_count']}
        [{Fore.LIGHTMAGENTA_EX}지역{Fore.RESET}]           $:   {response['region']}
        [{Fore.LIGHTMAGENTA_EX}아이콘{Fore.RESET}]         $:   https://cdn.discordapp.com/icons/{guildId}/{response['icon']}.webp?size=128
    """
    )
    sleep(6)
    Hydron()

elif option == 2:
    Hydron()

if __name__ == "__main__":
    fetch()
