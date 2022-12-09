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


def Loader():
	l = ['|', '/', '-', '\\', ' ']
	for i in l+l+l:
		sys.stdout.write(f"""\r {i}""")
		sys.stdout.flush()
		sleep(0.1)

global cls
def cls():
    os.system('cls')

global useragent
def useragent():
    file = open('data/useragent.txt', 'r')
    useragent = (random.choice(list(file))) # 파일을 리스트로 나눈 후 그 줄 중 한 줄을 선택
    useragent2 = []
    useragent2.append(useragent)
    useragent1 = []

# 아래는 로그인 해킹씬 따라해본 부분
try:
    with open('data/login.json') as f: # 로그인 데이터 있냐?
        config = json.load(f)
except: # 없구나.. 
    with open('data/login.json', 'w') as f: # 쓰기 모드!
        print(f"\n[{lg}#\x1b[95m\x1B[37m] Logging into Hydron...")
        login = input("[\x1b[95m#\x1b[95m\x1B[37m] Admin Password: ")
        json.dump({"Login": login}, f, indent=4) # 인덴트 = tab(스페이스바 4번 간격)
    input(f"\n[\x1b[95m#\x1b[95m\x1B[37m] Successfully Logged in as: [{m}{login}{w}]\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER to Continue: ")
    pass # 여기서 딱 엔터 뙇! 치면 멋있게 시작하는 거지~

with open('data/login.json') as f: # 재확인 후 로드
        config = json.load(f)
login = config.get('Login') # 불러오기

