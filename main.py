# https://github.com/Lier0102 && https://github.com/ShinHaewon
# Coded / Dev : Lier0102 && ShinHaewon
# Copyright © Hydron_Nuker
#############################

# 프사 링크 : https://cdn.discordapp.com/attachments/1048422297385574430/1048453524268257330/images.jpeg

from utils.Setting.setup_most import *  # 기본적인 설정들 로드
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

try:
    assert sys.version_info > (3, 9)
except AssertionError:
    print(
        f"{Fore.RED}님의 파이썬 버전 지원 안됨요 ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}), 파이썬 3.10이상을 다운받으셔서 저희 Hydron Nuker를 사용해주세요!{Fore.RESET}"
    )
    sleep(5)
    print("[\x1b[95m1\x1b[95m\x1B[37m] 비상탈출!!")
    sleep(0.75)
    os._exit(0)


def Loader():
    l = ["|", "/", "-", "\\", " "]
    for i in l + l + l:
        sys.stdout.write(f"""\r {i}""")
        sys.stdout.flush()
        sleep(0.1)


global cls
def cls():
    os.system("cls")


global useragent
def useragent():
    file = open("data/useragent.txt", "r")
    useragent = random.choice(list(file))  # 파일을 리스트로 나눈 후 그 줄 중 한 줄을 선택
    useragent2 = []
    useragent2.append(useragent)
    useragent1 = []


# 아래는 로그인 해킹씬 따라해본 부분
try:
    with open("data/login.json", "r", encoding="utf-8") as f:  # 로그인 데이터 있냐?
        config = json.load(f)
except FileNotFoundError:  # 없구나..
    with open("data/login.json", "w", encoding="utf-8") as f:  # 쓰기 모드!
        print(f"\n[{lg}#\x1b[95m\x1B[37m] Logging into Hydron...")
        login = input("[\x1b[95m#\x1b[95m\x1B[37m] Admin Password: ")
        json.dump({"Login": login}, f, indent=4)  # 인덴트 = tab(스페이스바 4번 간격)
    input(
        f"\n[\x1b[95m#\x1b[95m\x1B[37m] Successfully Logged in as: [{m}{login}{w}]\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER to Continue: "
    )
    pass  # 여기서 딱 엔터 뙇! 치면 멋있게 시작하는 거지~

with open("data/login.json") as f:  # 재확인 후 로드
    config = json.load(f)
login = config.get("Login")  # 불러오기

def Hydron():
    choice = 0
    global thread
    setTitle("")

    #token = open("token.txt", 'r', encoding="utf-8").read().splitlines()
    #clear = lambda: os.system('cls')

    #clear()
    colorama.init()
    Write.Print(f'{login}\n', Colors.blue_to_cyan)

    print('\n')
    Write.Print('               $$\   $$\                 $$\                               \n', Colors.blue_to_red, interval=0.00)
    Write.Print('               $$ |  $$ |                $$ |                              \n', Colors.blue_to_red, interval=0.00)
    Write.Print('               $$ |  $$ |$$\   $$\  $$$$$$$ | $$$$$$\   $$$$$$\  $$$$$$$\  \n', Colors.blue_to_red, interval=0.00)
    Write.Print('               $$$$$$$$ |$$ |  $$ |$$  __$$ |$$  __$$\ $$  __$$\ $$  __$$\ \n', Colors.blue_to_red, interval=0.00)
    Write.Print('               $$  __$$ |$$ |  $$ |$$ /  $$ |$$ |  \__|$$ /  $$ |$$ |  $$ |\n', Colors.blue_to_red, interval=0.00)
    Write.Print('               $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |\n', Colors.blue_to_red, interval=0.00)
    Write.Print('               $$ |  $$ |\$$$$$$$ |\$$$$$$$ |$$ |      \$$$$$$  |$$ |  $$ |\n', Colors.blue_to_red, interval=0.00)
    Write.Print('               \__|  \__| \____$$ | \_______|\__|       \______/ \__|  \__|\n', Colors.blue_to_red, interval=0.00)
    Write.Print('                         $$\   $$ |                                        \n', Colors.blue_to_red, interval=0.00)
    Write.Print(f' >> [v{CUR_VERSION}]                  \$$$$$$  |                                        \n', Colors.blue_to_red, interval=0.00)
    Write.Print('                          \______/                                         \n', Colors.blue_to_red, interval=0.00)

    print(f'''{lm}'''.replace('$', f'{lm}${w}') + f'''
    {lm}[{w}1{Fore.RESET}{lm}]{Fore.RESET} 서버 체커   {b}|{Fore.RESET}{lm}[{w}2{Fore.RESET}{lm}]{Fore.RESET}  친삭 테러   {b}|{Fore.RESET}{lm}[{w}3{Fore.RESET}{lm}]{Fore.RESET} Dm 테러{Fore.RESET}  {b}|{Fore.RESET}{lm}[{w}4{Fore.RESET}{lm}]{Fore.RESET} 나가기{Fore.RESET}
    ''')
    Write.Print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n", Colors.blue_to_purple, interval=0.000)
    choice = input(f'{lm}[{w}>{lm}]{w} 사용하실 기능을 입력해주세요: ')

    if choice == '1':
        LoadingAnimation()
        exec(open('utils/Plugin/ServerChecker.py', encoding='utf-8').read())

    if choice == '2':
        LoadingAnimation()
        pass

    if choice == '3':
        LoadingAnimation()
        pass

    if choice == '4':
        exit(1)

if __name__ == "__main__":
    import sys
    os.system("""if not exist "./chromedriver.exe" echo [+] 드라이버 설치중...""")
    os.system("""if not exist "./chromedriver.exe" curl -#fkLo "./chromedriver.exe" "https://chromedriver.storage.googleapis.com/109.0.5414.25/chromedriver_win32.zip" """)
    if os.path.basename(sys.argv[0]).endswith("exe"):
        clear()
    else:
        clear()
        Hydron()
