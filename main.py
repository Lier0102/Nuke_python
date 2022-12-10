# https://github.com/Lier0102 && https://github.com/ShinHaewon
# Coded / Dev : Lier0102 && ShinHaewon
# Copyright © Hydron_Nuker
#############################

# 프사 링크 : https://cdn.discordapp.com/attachments/1048422297385574430/1048453524268257330/images.jpeg

from utils.Setting.setup_most import * # 기본적인 설정들 로드
from utils.Setting.lib import *

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
    input(f"\n[\x1b[95m#\x1b[95m\x1B[37m] Successfully Logged in as: [{lm}{login}{w}]\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER to Continue: ")
    pass # 여기서 딱 엔터 뙇! 치면 멋있게 시작하는 거지~

with open('data/login.json') as f: # 재확인 후 로드
        config = json.load(f)
login = config.get('Login') # 불러오기

languages = { # 디스코드 언어
    'da'    : 'Danish, Denmark',
    'de'    : 'German, Germany',
    'en-GB' : 'English, United Kingdom',
    'en-US' : 'English, United States',
    'aud'   : 'English, Austrlia',
    'es-ES' : 'Spanish, Spain',
    'fr'    : 'French, France',
    'hr'    : 'Croatian, Croatia',
    'lt'    : 'Lithuanian, Lithuania',
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

regions = [ # 국가
    'brazil',
    'hongkong',
    'india',
    'japan',
    'rotterdam',
    'russia',
    'singapore',
    'southafrica',
    'sydney',
    'us-central',
    'us-east',
    'us-south',
    'us-west'
]

def Hydron():
    setTitle("")

    token = open("token.txt", 'r').read().splitlines()
    clear = lambda: os.system('cls')

    clear()
    colorama.init()
    Write.Print(f'{login}\n', Colors.blue_to_cyan)

    print('\n\n\n')
    Write.Print('               $$\   $$\                 $$\                               ', Colors.blue_to_red, interval=0.0)
    Write.Print('               $$ |  $$ |                $$ |                              ', Colors.blue_to_red, interval=0.0)
    Write.Print('               $$ |  $$ |$$\   $$\  $$$$$$$ | $$$$$$\   $$$$$$\  $$$$$$$\  ', Colors.blue_to_red, interval=0.0)
    Write.Print('               $$$$$$$$ |$$ |  $$ |$$  __$$ |$$  __$$\ $$  __$$\ $$  __$$\ ', Colors.blue_to_red, interval=0.0)
    Write.Print('               $$  __$$ |$$ |  $$ |$$ /  $$ |$$ |  \__|$$ /  $$ |$$ |  $$ |', Colors.blue_to_red, interval=0.0)
    Write.Print('               $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |', Colors.blue_to_red, interval=0.0)
    Write.Print('               $$ |  $$ |\$$$$$$$ |\$$$$$$$ |$$ |      \$$$$$$  |$$ |  $$ |', Colors.blue_to_red, interval=0.0)
    Write.Print('               \__|  \__| \____$$ | \_______|\__|       \______/ \__|  \__|', Colors.blue_to_red, interval=0.0)
    Write.Print('                         $$\   $$ |                                        ', Colors.blue_to_red, interval=0.0)
    Write.Print(f' >> [v{CUR_VERSION}]                        \$$$$$$  |                                        ', Colors.blue_to_red, interval=0.0)
    Write.Print('                          \______/                                         ', Colors.blue_to_red, interval=0.0)

    print(f'''{lm}'''.replace('$', f'{lm}${w}') + f'''
    {lm}[{w}1{Fore.RESET}{lm}]{Fore.RESET} 서버 체커   {b}|{Fore.RESET}{lm}[{w}9{Fore.RESET}{lm}]{Fore.RESET}  친삭 테러   {b}|{Fore.RESET}{lm}[{w}17{Fore.RESET}{lm}]{Fore.RESET} Dm 테러{Fore.RESET}  
    ''')
    Write.Print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.blue_to_purple, interval=0.000)
    choice = input(f'{lm}[{w}>{lm}]{w} 사용하실 기능을 입력해주세요: ')

    os.system("pause")