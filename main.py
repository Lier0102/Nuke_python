# https://github.com/Lier0102 && https://github.com/ShinHaewon
# Coded / Dev : Lier0102 && ShinHaewon
# Copyright © Hydron_Nuker
# WEBSITE : Lier0102
#############################

# 프사 링크 : https://cdn.discordapp.com/attachments/1048422297385574430/1048453524268257330/images.jpeg

from utils.Setting.lib import *
from utils.Setting.setup_most import *  # 기본적인 설정들 로드
from utils.Setting.update import update

############### 기능들 로드하기 ###############

from utils.Plugin import plugins

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
        time.sleep(5)
        print("[\x1b[95m1\x1b[95m\x1B[37m] 비상탈출!!")
        time.sleep(0.75)
        os._exit(0) # type: ignore


def Loader():
    l = ["|", "/", "-", "\\", " "]
    for i in l + l + l:
        sys.stdout.write(f"""\r {i}""")
        sys.stdout.flush()
        time.sleep(0.1)


def cls():
    os.system("cls")


def useragent():
    file = open("data/useragent.txt", "r")
    useragent = random.choice(list(file))  # 파일을 리스트로 나눈 후 그 줄 중 한 줄을 선택
    useragent2 = []
    useragent2.append(useragent)
    # useragent1 = []


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
    logfile.write(f"{detail_date}\tLogging into Program v{CUR_VERSION}\n")
    set_login()
    
    
    # token = open("token.txt", 'r', encoding="utf-8").read().splitlines()
    clear = lambda: os.system('cls')

    clear()
    
    logfile.write(f"{detail_date}\tColorama Initializing..\n")
    colorama.init()
    
    logfile.write(f"{detail_date}\tPlugin is setting up..\n")
    names = [plugin.plugin_name for plugin in plugins] + ["나가기"]
    choices = {i: plugin for i, plugin in enumerate(plugins, 1)}
        
    menu = "|".join(f"{lm}[{w}{i}{Fore.RESET}{lm}]{Fore.RESET} {name} {b}"for i, name in enumerate(names, 1))

    Write.Print(f"{login}\n", Colors.blue_to_cyan)
    time.sleep(0.05)
    logfile.write(f"{detail_date}\tMenu Logo Showed up\n")
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
    {menu}
    """)
    Write.Print(
        "════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════",
        Colors.blue_to_purple,
        interval=0.000,
    )
    print()
    logfile.write(f"{detail_date}\tWaiting user's choice...\n")
    choice = int(input(f"{lm}[{w}>{lm}]{w} 사용하실 기능을 입력해주세요: "))

    logfile.write(f"{detail_date}\tUser has choosed choice\n")
    chosen_plugin = choices.get(choice)
    
    
    if chosen_plugin is None:
        logfile.write(f"{detail_date}\tWrong choice or Exit.\n")
        print("프로그램을 종료합니다.")
        time.sleep(2)
        logfile.write(f"{detail_date}\tExited\n\n")
        exit(1)
    
    logfile.write(f"{detail_date}\tLoading...\n")
    LoadingAnimation()
    logfile.write(f"{detail_date}\tExecuting {chosen_plugin}Features...\n")
    await chosen_plugin.main()
    logfile.write(f"{detail_date}\tFeature process completed\n")


if __name__ == "__main__":
    import sys    
    
    logfile.write(f"{detail_date}\t[Start Message]Program is started. We are now logging...\n\n")
    check_version()
    logfile.write(f"{detail_date}\tVersion Checked.\n")


    show_logo()
    logfile.write(f"{detail_date}\tlogo showed\n")

    os.system("""if not exist "./chromedriver.exe" echo [+] 드라이버 설치중...""")
    logfile.write(f"{detail_date}\tDriver Checking...\n")
    os.system(
        """if not exist "./chromedriver.exe" curl -#fkLo "./chromedriver.exe" "https://chromedriver.storage.googleapis.com/109.0.5414.25/chromedriver_win32.zip" """
    )
    logfile.write(f"{detail_date}\tDriver Checked...\n")
    if os.path.basename(sys.argv[0]).endswith("exe"):
        logfile.write(f"{detail_date}\tChecking Update...\n")
        update()
        logfile.write(f"{detail_date}\tUpdate process completed\n")
        clear()
    else:
        logfile.write(f"{detail_date}\tChecking Update...\n")
        update()
        logfile.write(f"{detail_date}\tUpdate process completed\n")
        asyncio.run(Hydron())
