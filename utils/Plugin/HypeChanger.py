from utils.Plugin.PluginABC import PluginABC
from utils.Setting.lib import mainHeader
from colorama import Fore
import requests
import time
from utils.Setting.setup_most import TokenValidator, importlib

class HypeChanger(PluginABC):
    plugin_name = "하이퍼스쿼드 변경"

    @classmethod
    def change(self, token):

        print(f'''\n[\x1b[95m1\x1b[95m\x1B[37m] {Fore.MAGENTA}용맹(Bravery){Fore.RESET}
[\x1b[95m2\x1b[95m\x1B[37m] {Fore.LIGHTRED_EX}찬란함(Brilliance){Fore.RESET}
[\x1b[95m3\x1b[95m\x1B[37m] {Fore.LIGHTCYAN_EX}균형(Balance){Fore.RESET}
[\x1b[95m4\x1b[95m\x1B[37m] 하이퍼스쿼드 나가기''')
        house = input("\n[\x1b[95m>\x1b[95m\x1B[37m] 하이퍼스쿼드 선택: ")
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
                try:
                    print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] 실패...')
                except:
                    pass

        if house == '4':
                form = {
                    'house_id': choosenHouse
                }
                req = requests.delete('https://discord.com/api/v9/hypesquad/online', headers=headers, json=form)
                if req.status_code == 204:
                    print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] 성공! ^^7')
                else:
                    pass

        else: # 그냥 지나가기!
            pass

    @classmethod
    async def main(cls):
        option = super().get_option()
        if option == 1:
            time.sleep(1)
            token = open('token.txt', 'r').read().splitlines()
            await TokenValidator(token=token[0])
            time.sleep(3)
            cls.change(token=token[0]) # 아직은 완전한 버전이 아니라서 첫번째 토큰만 바꾸기
            
            input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] 엔터를 눌러주세요: ')
            await importlib.import_module("main").Hydron()
        else:
            await importlib.import_module("main").Hydron()