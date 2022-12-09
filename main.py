# https://github.com/Lier0102 && https://github.com/ShinHaewon
# Coded / Dev : Lier0102 && ShinHaewon
# Copyright © Hydron_Nuker
#############################

# 프사 링크 : https://cdn.discordapp.com/attachments/1048422297385574430/1048453524268257330/images.jpeg

from utils.Setting.setup_most import * # 기본적인 설정들 로드

############### 기능들 로드하기 ###############

import utils.Plugin.ServerChecker
import utils.Plugin.AccountBomber
import utils.Plugin.DmBomber

############### 기능들 로드하기 ###############

############### 디자인 관련 상수 설정 ###############

w = Fore.WHITE
b = Fore.BLACK
lg = Fore.LIGHTGREEN_EX
ly = Fore.LIGHTYELLOW_EX
lm = Fore.LIGHTMAGENTA_EX
lc = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX

############### 디자인 관련 상수 설정 ###############

try:
    assert sys.version >= (3,9)
except AssertionError:
    print(f"{Fore.RED}님의 파이썬 버전 지원 안됨요 ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}), 파이썬 3.10이상을 다운받으셔서 저희 Hydron Nuker를 사용해주세요!{Fore.RESET}")
    sleep(5)
    print("[\x1b[95m1\x1b[95m\x1B[37m] 비상탈출!!")
    sleep(0.75)
    os._exit(0)

