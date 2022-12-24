from colorama import Fore
import requests
from requests import HTTPError

from utils.Plugin.PluginABC import PluginABC
from utils.Setting.lib import mainHeader
from utils.Setting.setup_most import TokenValidator, importlib

class HypeChanger(PluginABC):
    plugin_name = "하이퍼스쿼드 변경"

    @classmethod
    def change(cls, token: str):
        url = "https://discord.com/api/v9/hypesquad/online"
        message = (f"\n[\x1b[95m1\x1b[95m\x1B[37m] {Fore.MAGENTA}용맹(Bravery){Fore.RESET}\n"
                   f"[\x1b[95m2\x1b[95m\x1B[37m] {Fore.LIGHTRED_EX}찬란함(Brilliance){Fore.RESET}\n"
                   f"[\x1b[95m3\x1b[95m\x1B[37m] {Fore.LIGHTCYAN_EX}균형(Balance){Fore.RESET}\n"
                   f"[\x1b[95m4\x1b[95m\x1B[37m] 하이퍼스쿼드 나가기")
        print(message)
        
        house = int(input("\n[\x1b[95m>\x1b[95m\x1B[37m] 하이퍼스쿼드 선택: "))
        headers = mainHeader(token)

        if house < 0 or house > 4:
            print("1 ~ 4 사이를 입력해주세요.")
            return
        
        chosenHouse = house if house in [1, 2, 3] else None

        form = {'house_id' : chosenHouse}

        if chosenHouse:
            response = requests.post(url=url, json=form, headers=headers)
        else:
            response = requests.delete(url=url, json=form, headers=headers)
            
        try:
            response.raise_for_status()
            print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] 성공! ^^7')
        except HTTPError:
            print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] 실패...")

    @classmethod
    async def main(cls):
        option = super().get_option()
        
        if option == 1:
            token = input(f"\n[\x1b[95m>\x1b[95m\x1B[37m] 토큰: ")
            
            await TokenValidator(token=token)
            
            cls.change(token=token)
            
            input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] 엔터를 눌러주세요: ')
            await importlib.import_module("main").Hydron()
        else:
            await importlib.import_module("main").Hydron()