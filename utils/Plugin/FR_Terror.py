from utils.Setting.setup_most import *
from utils.Plugin.PluginABC import PluginABC
from utils.Setting.lib import mainHeader

class FR_Terror(PluginABC): # token.txt에 있는 모든 토큰으로 특정 유저에게 친추를 보냄
    plugin_name = "친구 요청 테러"

    @classmethod
    def be_friend(self, token, user):
        try:
            user = user.split('#')
            headers = mainHeader(token)
            form = {
                "username" : user[0],
                "discriminator" : user[1]
            }
            src = requests.post('https://discord.com/api/v9/users/@me/relationships', headers=headers,
                                    json=form)
            if src.status_code == 204 or 200:
                    print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] {user[0]}#{user[1]}에게 친추 요청을 보냈습니다! ")
        except Exception as e:
            print(e)

    @classmethod
    async def main(cls):
        option = super().get_option()
        if option == 1:

            user = input(f"\n[\x1b[95m>\x1b[95m\x1B[37m] 유저이름 + 유저태그: ")
            tokens = open("token.txt", "r", encoding='utf-8').read().splitlines()
            delay = float(input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] 지연시간: '))

            for token in tokens:
                time.sleep(delay)
                cls.be_friend(token, delay)
            
            time.sleep(3)
            input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] 엔터를 눌러주세요: ')
            await importlib.import_module("main").Hydron()
        else:
            await importlib.import_module("main").Hydron() # 비동기가 아니여서 await 없앰 ㅠ