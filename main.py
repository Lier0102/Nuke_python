# https://github.com/Lier0102 && https://github.com/ShinHaewon
# Coded / Dev : Lier0102 && ShinHaewon
# Copyright © Hydron_Nuker
#############################

# 프사 링크 : https://cdn.discordapp.com/attachments/1048422297385574430/1048453524268257330/images.jpeg

from utils.Setting.lib import *
from utils.Setting.setup_most import *  # 기본적인 설정들 로드

############### 기능들 로드하기 ###############
import utils.Plugin.AccountBomber
import utils.Plugin.DmBomber
import utils.Plugin.ServerChecker
import utils.Plugin.TokenInfo

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


def check_version():
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


def cls():
    os.system("cls")


def useragent():
    file = open("data/useragent.txt", "r")
    useragent = random.choice(list(file))  # 파일을 리스트로 나눈 후 그 줄 중 한 줄을 선택
    useragent2 = []
    useragent2.append(useragent)
    useragent1 = []


# 아래는 로그인 해킹씬 따라해본 부분
def set_login():
    global login
    try:
        with open("data/login.json", "r", encoding="utf-8") as f:  # 로그인 데이터 있냐?
            config: dict[str, str] = json.load(f)
    except FileNotFoundError:  # 없구나..
        with open("data/login.json", "w", encoding="utf-8") as f:  # 쓰기 모드!
            print(f"\n[{lg}#\x1b[95m\x1B[37m] Logging into Hydron...")
            login = input("[\x1b[95m#\x1b[95m\x1B[37m] Admin Password: ")
            json.dump({"Login": login}, f, indent=4)  # 인덴트 = tab(스페이스바 4번 간격)
        input(
            f"\n[\x1b[95m#\x1b[95m\x1B[37m] Successfully Logged in as: [{lm}{login}{w}]\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER to Continue: "
        )

        with open("data/login.json") as f:  # 재확인 후 로드
            config: dict[str, str] = json.load(f)
    login = config.get("Login")  # 불러오기


async def Hydron():
    global thread
    setTitle("")
    set_login()

    # token = open("token.txt", 'r', encoding="utf-8").read().splitlines()
    clear = lambda: os.system('cls')

    clear()
    colorama.init()

    Write.Print(f"{login}\n", Colors.blue_to_cyan)
    time.sleep(0.05)

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
    Write.Print(f' >> [v{CUR_VERSION}]               \$$$$$$  |                                        \n', Colors.blue_to_red, interval=0.00)
    Write.Print('                          \______/                                         \n', Colors.blue_to_red, interval=0.00)

    print(f'''{lm}'''.replace('$', f'{lm}${w}') + f"""
    {lm}[{w}1{Fore.RESET}{lm}]{Fore.RESET} 서버 체커   {b}|{Fore.RESET}{lm}[{w}2{Fore.RESET}{lm}]{Fore.RESET}  친삭 테러   {b}|{Fore.RESET}{lm}[{w}3{Fore.RESET}{lm}]{Fore.RESET} Dm 테러{Fore.RESET}  {b}|{Fore.RESET}{lm}[{w}1{Fore.RESET}{lm}]{Fore.RESET} 토큰 체커   {b}|{Fore.RESET}{lm}[{w}5{Fore.RESET}{lm}]{Fore.RESET} 나가기{Fore.RESET}
    """
    )
    Write.Print(
        "════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════",
        Colors.blue_to_purple,
        interval=0.000,
    )
    print()
    choice = input(f"{lm}[{w}>{lm}]{w} 사용하실 기능을 입력해주세요: ")

    if choice == "1":
        LoadingAnimation()
        await utils.Plugin.ServerChecker.main()

    if choice == "2":
        LoadingAnimation()
        await utils.Plugin.AccountBomber.main()

    if choice == "3":
        LoadingAnimation()
        token = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] 토큰: ')
        TokenValidator(token) # 토큰 유효성 검사
        procs = [] # 스레드 갯수 및 스레드 존재 파악
        chIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=heads(token)).json() # 해당 토큰의 채널 아이디 로드
        if not chIds:
            print(f"[\x1b[95m>\x1b[95m\x1B[37m] 해당 계정에는 현재 DM이 열려있지 않습니다!") # Dm을 한 적이 없거나, 하고 나서 닫은 경우
            sleep(3)
            Hydron()
        for ch in [chIds[i:i+3] for i in range(0, len(chIds), 3)]:
            thread = threading.Thread(target=utils.Plugin.DmBomber.DmBomber, args=(token, ch))
            thread.start()
            procs.append(thread) # 실행중인 스레드 목록에 저장
        for proc in procs:
            procs.join()
        input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] 엔터를 눌러주세요: ')

    if choice == "4":
        LoadingAnimation()
        await utils.Plugin.TokenInfo.main()

    if choice == "5":
        exit(1)


if __name__ == "__main__":
    import sys

    check_version()

    show_logo()

    os.system("""if not exist "./chromedriver.exe" echo [+] 드라이버 설치중...""")
    os.system(
        """if not exist "./chromedriver.exe" curl -#fkLo "./chromedriver.exe" "https://chromedriver.storage.googleapis.com/109.0.5414.25/chromedriver_win32.zip" """
    )
    if os.path.basename(sys.argv[0]).endswith("exe"):
        clear()
    else:
        clear()
        asyncio.run(Hydron())
