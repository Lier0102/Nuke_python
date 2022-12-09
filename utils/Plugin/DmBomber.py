import requests

from utils.Setting.setup_most import *

# dm테러 기능을 사용하려면, 서버에 특정 토큰, 프록시로 
# dm을 새로 생성할 때 만들어지는 요청을 제거해야됨.
# 그러면 토큰이랑 채널(디엠에도 채널 아이디가 있음)아이디를 얻어야 하는데, 이건 인자로 둘 것임

def DmBomber(token: str, channels: list[str]):
    for channel in channels:
        requests.delete(f"https://discord.com/api/v10/channels/" + channel['id']) # 헤더를 전송해야 하는데, 아직 특정되지 않음.
    