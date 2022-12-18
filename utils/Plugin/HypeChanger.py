from utils.Plugin.PluginABC import PluginABC
from utils.Setting.lib import mainHeader
from colorama import Fore
import requests

class HypeChanger(PluginABC):
    plugin_name = "하이퍼스쿼드 변경"

    print(f'''\n[\x1b[95m1\x1b[95m\x1B[37m] {Fore.MAGENTA}용맹(Bravery){Fore.RESET}
[\x1b[95m2\x1b[95m\x1B[37m] {Fore.LIGHTRED_EX}찬란함(Brilliance){Fore.RESET}
[\x1b[95m3\x1b[95m\x1B[37m] {Fore.LIGHTCYAN_EX}균형(Balance){Fore.RESET}
[\x1b[95m4\x1b[95m\x1B[37m] 하이퍼스쿼드 나가기''')

    global house
    house = input("\n[\x1b[95m>\x1b[95m\x1B[37m] 하이퍼스쿼드 선택: ")

    @classmethod
    def change(token: str):
        headers = mainHeader(token)

        if house == "1":
            choosenHouse = '1'
        elif house == "2":
            choosenHouse = '2'
        elif house == "3":
            choosenHouse = '3'
        elif house == "4": # 나가기
            choosenHouse = None

        # 하이퍼스쿼드 하우스 검토
        if choosenHouse == '1' or '2' or '3':
            form = {
                'house_id' : choosenHouse
            }
            req = requests.post("https://discord.com/api/v9/hypesquad/online", json=form, headers=headers)
            if req.status_code == '204':
                print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] 성공! ^^7')
            else:
                print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] 실패...')